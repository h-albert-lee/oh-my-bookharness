const state = {
  currentChapterId: null,
  renderMode: "rendered",
  chapterFilter: "",
  statusFilter: "all",
  artifactFilter: "",
  selectedArtifact: null,
  allChapters: [],
  autoRefresh: true,
  autoRefreshTimer: null,
};

const stages = [
  "brief_generation",
  "source_collection",
  "source_analysis",
  "outline_design",
  "human_approval_a",
  "draft_writing",
  "automated_review",
  "revision_plan_synthesis",
  "draft_revision",
  "human_approval_b",
];

async function api(path, options = {}) {
  const response = await fetch(path, {
    headers: { "Content-Type": "application/json" },
    ...options,
  });
  if (!response.ok) {
    throw new Error(await response.text());
  }
  return response.json();
}

function notify(message, isError = false) {
  const toast = document.getElementById("toast");
  toast.classList.remove("hidden");
  toast.textContent = message;
  toast.style.borderColor = isError ? "var(--danger)" : "var(--border)";
  setTimeout(() => toast.classList.add("hidden"), 2400);
}

function showView(name) {
  document.querySelectorAll(".view").forEach((view) => view.classList.remove("active"));
  document.querySelectorAll(".nav-button").forEach((button) => button.classList.remove("active"));
  document.getElementById(`view-${name}`).classList.add("active");
  const nav = document.getElementById(`nav-${name}`);
  if (nav) nav.classList.add("active");
}

function badge(status) {
  const text = String(status || "unknown");
  const css =
    text.includes("approved") || text.includes("completed")
      ? "success"
      : text.includes("failed") || text.includes("rejected")
        ? "danger"
        : "warning";
  return `<span class="badge ${css}">${text}</span>`;
}

function escapeHtml(text) {
  return String(text)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;");
}

function formatDateTime(value) {
  if (!value) return "-";
  const date = new Date(value);
  return Number.isNaN(date.getTime()) ? value : date.toLocaleString("ko-KR");
}

function stageProgress(chapter) {
  const idx = Math.max(stages.indexOf(chapter.current_stage), 0);
  const pct = Math.round(((idx + 1) / stages.length) * 100);
  return `<div><div class="badge stage">${idx + 1}/${stages.length}</div><div class="stage-progress-bar"><div class="stage-progress-fill" style="width:${pct}%"></div></div></div>`;
}

function applyChapterTableFilters() {
  const filtered = state.allChapters.filter((chapter) => {
    const keyword = state.chapterFilter.trim().toLowerCase();
    const searchHit =
      !keyword ||
      chapter.chapter_id.toLowerCase().includes(keyword) ||
      chapter.title.toLowerCase().includes(keyword);
    const statusHit = state.statusFilter === "all" || chapter.status === state.statusFilter;
    return searchHit && statusHit;
  });

  document.getElementById("chapter-table").innerHTML = filtered.length
    ? filtered
        .map(
          (chapter) => `<tr>
        <td><strong>${chapter.chapter_id}</strong><br /><span class="subtle">${chapter.title}</span></td>
        <td>${badge(chapter.status)}</td>
        <td>${stageProgress(chapter)}</td>
        <td>${chapter.latest_draft || "-"}</td>
        <td><button data-open-chapter="${chapter.chapter_id}">열기</button></td>
      </tr>`
        )
        .join("")
    : `<tr><td colspan="5" class="subtle">조건에 맞는 chapter가 없습니다.</td></tr>`;

  document.querySelectorAll("[data-open-chapter]").forEach((button) => {
    button.onclick = () => openChapter(button.dataset.openChapter);
  });
}

function setDashboardMeta(project) {
  document.getElementById("project-title").textContent = project.title;
  document.getElementById("dashboard-updated").textContent = `최근 갱신: ${new Date().toLocaleTimeString("ko-KR")}`;
  document.getElementById("global-status").textContent = `${project.metrics.chapter_count} chapters · ${project.metrics.pending_approval_count} approvals 대기`;

  document.getElementById("metrics").innerHTML = [
    ["전체 Chapter", project.metrics.chapter_count, "작성 파이프라인 관리 대상"],
    ["최종 승인 완료", project.metrics.approved_count, "release-ready 후보"],
    ["승인 대기", project.metrics.pending_approval_count, "human decision 필요"],
    ["최근 Job", project.metrics.recent_run_count, "agent 실행 추적"],
  ]
    .map(([label, value, hint]) => `<div class="metric-card"><div class="label">${label}</div><div class="value">${value}</div><div class="hint">${hint}</div></div>`)
    .join("");
}

function populateStatusFilter(chapters) {
  const select = document.getElementById("chapter-status-filter");
  const statuses = [...new Set(chapters.map((chapter) => chapter.status))].sort();
  select.innerHTML = `<option value="all">모든 상태</option>${statuses
    .map((status) => `<option value="${status}">${status}</option>`)
    .join("")}`;
  select.value = state.statusFilter;
}

async function loadDashboard() {
  try {
    const project = await api("/api/project");
    state.allChapters = project.chapters;
    setDashboardMeta(project);
    populateStatusFilter(project.chapters);
    applyChapterTableFilters();

    document.getElementById("pending-approvals").innerHTML = project.pending_approvals.length
      ? project.pending_approvals
          .map(
            (item) => `<div class="approval-card">
              <strong>${item.chapter_id}</strong> ${badge(item.status)}
              <p>${item.title}</p>
              <p class="subtle">expected: ${item.approval_key}</p>
              <button data-open-chapter="${item.chapter_id}">검토하기</button>
            </div>`
          )
          .join("")
      : `<p class="subtle">대기 중인 approval이 없습니다.</p>`;

    document.getElementById("recent-runs").innerHTML = project.recent_runs.length
      ? project.recent_runs
          .map(
            (run) => `<div class="job-card">
              <strong>${run.job_type}</strong> ${badge(run.status)}
              <div>${run.chapter_id || "-"}</div>
              <div class="subtle">actor: ${run.actor} · ${formatDateTime(run.created_at)}</div>
            </div>`
          )
          .join("")
      : `<p class="subtle">실행 이력이 없습니다.</p>`;

    document.querySelectorAll("[data-open-chapter]").forEach((button) => {
      button.onclick = () => openChapter(button.dataset.openChapter);
    });
  } catch (error) {
    notify(`대시보드 로딩 실패: ${error.message}`, true);
  }
}

async function loadApprovalQueue() {
  try {
    const items = await api("/api/approvals/pending");
    document.getElementById("approval-queue").innerHTML = items.length
      ? items
          .map(
            (item, idx) => `<div class="approval-card">
              <div class="button-row" style="justify-content: space-between; align-items: center;">
                <div>
                  <strong>#${idx + 1} · ${item.chapter_id}</strong> ${badge(item.status)}
                  <p>${item.title}</p>
                  <p class="subtle">approval key: ${item.approval_key}</p>
                </div>
                <button data-open-chapter="${item.chapter_id}">열기</button>
              </div>
            </div>`
          )
          .join("")
      : `<div class="panel"><p class="subtle">현재 승인 대기 항목이 없습니다.</p></div>`;

    document.querySelectorAll("[data-open-chapter]").forEach((button) => {
      button.onclick = () => openChapter(button.dataset.openChapter);
    });
  } catch (error) {
    notify(`Approval Queue 로딩 실패: ${error.message}`, true);
  }
}

async function openChapter(chapterId) {
  state.currentChapterId = chapterId;
  state.selectedArtifact = null;
  showView("chapter");
  await loadChapter(chapterId);
}

function renderStageNavigator(chapter) {
  const currentIdx = Math.max(stages.indexOf(chapter.current_stage), 0);
  const pct = Math.round(((currentIdx + 1) / stages.length) * 100);
  document.getElementById("stage-progress").innerHTML = `
    <p class="subtle">현재 단계: <strong>${chapter.current_stage}</strong></p>
    <div class="stage-progress-bar"><div class="stage-progress-fill" style="width:${pct}%"></div></div>
    <p class="subtle">${currentIdx + 1} / ${stages.length} 단계</p>
    <div class="stage-progress-track">
      ${stages
        .map(
          (stage, idx) => `<div class="stage-card ${idx === currentIdx ? "active" : ""}">
            <span>${idx + 1}. ${stage}</span>
            ${idx < currentIdx ? '<span class="badge success">done</span>' : idx === currentIdx ? '<span class="badge warning">current</span>' : '<span class="badge">todo</span>'}
          </div>`
        )
        .join("")}
    </div>
  `;
}

function renderArtifactList(artifacts) {
  const keyword = state.artifactFilter.trim().toLowerCase();
  const filtered = artifacts.filter((artifact) => !keyword || artifact.name.toLowerCase().includes(keyword) || artifact.path.toLowerCase().includes(keyword));

  document.getElementById("artifact-list").innerHTML = filtered.length
    ? filtered
        .map(
          (artifact) => `<div class="artifact-card"><button data-artifact="${artifact.path}" class="${state.selectedArtifact === artifact.path ? "active" : ""}">${artifact.name}</button></div>`
        )
        .join("")
    : `<p class="subtle">조건에 맞는 artifact가 없습니다.</p>`;

  document.querySelectorAll("[data-artifact]").forEach((button) => {
    button.onclick = () => {
      state.selectedArtifact = button.dataset.artifact;
      loadArtifact(button.dataset.artifact);
      renderArtifactList(artifacts);
    };
  });
}

function renderRuns(runs) {
  document.getElementById("chapter-runs").innerHTML = runs.length
    ? runs
        .map((run) => {
          const hasLog = Array.isArray(run.log) && run.log.length;
          return `<div class="job-card">
            <strong>${run.job_type}</strong> ${badge(run.status)}
            <div class="subtle">actor: ${run.actor}</div>
            <div class="subtle">created: ${formatDateTime(run.created_at)}</div>
            <div class="subtle">finished: ${formatDateTime(run.finished_at)}</div>
            ${run.error ? `<pre>${escapeHtml(run.error)}</pre>` : ""}
            ${hasLog ? `<details><summary>로그 ${run.log.length}개 보기</summary><pre>${escapeHtml(run.log.join("\n"))}</pre></details>` : ""}
          </div>`;
        })
        .join("")
    : `<p class="subtle">이 장의 job이 없습니다.</p>`;
}

function renderAudit(audit) {
  document.getElementById("chapter-audit").innerHTML = audit.length
    ? audit
        .map(
          (item) => `<div class="audit-card">
            <strong>${item.event_type}</strong>
            <div class="subtle">${item.actor} · ${formatDateTime(item.timestamp)}</div>
            <details>
              <summary>상세 details</summary>
              <pre>${escapeHtml(JSON.stringify(item.details, null, 2))}</pre>
            </details>
          </div>`
        )
        .join("")
    : `<p class="subtle">감사 로그가 없습니다.</p>`;
}

async function loadChapter(chapterId = state.currentChapterId) {
  try {
    const detail = await api(`/api/chapters/${chapterId}`);
    const chapter = detail.state;
    document.getElementById("chapter-heading").textContent = `${chapter.chapter_id} · ${chapter.title}`;
    document.getElementById("chapter-meta").innerHTML = `${badge(chapter.status)} current stage: ${chapter.current_stage}`;

    renderStageNavigator(chapter);

    document.getElementById("stage-actions").innerHTML = stages.map((stage) => `<button data-stage="${stage}">${stage}</button>`).join("");
    document.querySelectorAll("[data-stage]").forEach((button) => {
      button.onclick = async () => {
        try {
          await api(`/api/chapters/${chapterId}/run-stage`, {
            method: "POST",
            body: JSON.stringify({ stage: button.dataset.stage, actor: "ui-editor" }),
          });
          notify(`${button.dataset.stage} 실행을 큐에 등록했습니다.`);
          setTimeout(() => loadChapter(chapterId), 300);
        } catch (error) {
          notify(`stage 실행 실패: ${error.message}`, true);
        }
      };
    });

    renderArtifactList(detail.artifacts);

    const draftArtifacts = detail.artifacts.filter((artifact) => artifact.name.startsWith("draft_") || artifact.name === "final_candidate.md");
    const diffOptions = draftArtifacts.map((artifact) => `<option value="${artifact.path}">${artifact.name}</option>`).join("");
    document.getElementById("diff-left").innerHTML = diffOptions;
    document.getElementById("diff-right").innerHTML = diffOptions;

    document.getElementById("review-cards").innerHTML = detail.review_reports.length
      ? detail.review_reports
          .map((report) => `<div class="review-card"><strong>${report.path}</strong><pre>${escapeHtml(report.content)}</pre></div>`)
          .join("")
      : `<p class="subtle">리뷰 산출물이 아직 없습니다.</p>`;

    renderRuns(detail.runs);
    renderAudit(detail.audit);

    if (detail.artifacts.length) {
      state.selectedArtifact = state.selectedArtifact || detail.artifacts[0].path;
      await loadArtifact(state.selectedArtifact);
      renderArtifactList(detail.artifacts);
    } else {
      document.getElementById("artifact-viewer").innerHTML = `<p class="subtle">표시할 문서가 없습니다.</p>`;
      document.getElementById("active-artifact").textContent = "";
    }
  } catch (error) {
    notify(`chapter 로딩 실패: ${error.message}`, true);
  }
}

async function loadArtifact(path) {
  try {
    const artifact = await api(`/api/artifacts?path=${encodeURIComponent(path)}`);
    const container = document.getElementById("artifact-viewer");
    document.getElementById("active-artifact").textContent = artifact.path;
    if (state.renderMode === "rendered" && artifact.rendered_html) {
      container.innerHTML = artifact.rendered_html;
    } else {
      container.innerHTML = `<pre>${escapeHtml(artifact.content)}</pre>`;
    }
  } catch (error) {
    notify(`artifact 로딩 실패: ${error.message}`, true);
  }
}

async function loadDiff() {
  const left = document.getElementById("diff-left").value;
  const right = document.getElementById("diff-right").value;
  if (!left || !right) return;
  try {
    const diff = await api(`/api/artifacts/diff?left=${encodeURIComponent(left)}&right=${encodeURIComponent(right)}`);
    const changed = diff.changed
      .map((entry) => `<div class="badge ${entry.type === "added" ? "success" : "danger"}">${entry.type}</div><pre>${escapeHtml(entry.line)}</pre>`)
      .join("");

    const onlyLeft = diff.left_only.length ? `<p class="subtle">left only: ${escapeHtml(diff.left_only.join(", "))}</p>` : "";
    const onlyRight = diff.right_only.length ? `<p class="subtle">right only: ${escapeHtml(diff.right_only.join(", "))}</p>` : "";
    document.getElementById("diff-viewer").innerHTML = `${onlyLeft}${onlyRight}${changed || `<p class="subtle">차이가 없습니다.</p>`}`;
  } catch (error) {
    notify(`diff 로딩 실패: ${error.message}`, true);
  }
}

async function submitApproval(event) {
  event.preventDefault();
  const form = new FormData(event.target);
  const notes = String(form.get("notes") || "")
    .split("\n")
    .map((line) => line.trim())
    .filter(Boolean);

  try {
    await api(`/api/chapters/${state.currentChapterId}/approve`, {
      method: "POST",
      body: JSON.stringify({
        approval_key: form.get("approval_key"),
        result: form.get("result"),
        notes,
        actor: form.get("actor") || "editor_in_chief",
      }),
    });
    notify("승인 요청을 제출했습니다.");
    setTimeout(() => loadChapter(state.currentChapterId), 300);
  } catch (error) {
    notify(`승인 제출 실패: ${error.message}`, true);
  }
}

async function submitCreateChapter(event) {
  event.preventDefault();
  const form = new FormData(event.target);
  const dependencies = String(form.get("dependencies") || "")
    .split(",")
    .map((item) => item.trim())
    .filter(Boolean);

  try {
    await api("/api/chapters", {
      method: "POST",
      body: JSON.stringify({
        chapter_id: form.get("chapter_id"),
        title: form.get("title"),
        dependencies,
        actor: form.get("actor") || "editor",
      }),
    });
    notify("새 chapter를 생성했습니다.");
    await loadDashboard();
    showView("dashboard");
  } catch (error) {
    notify(`chapter 생성 실패: ${error.message}`, true);
  }
}

function setupAutoRefresh() {
  if (state.autoRefreshTimer) clearInterval(state.autoRefreshTimer);
  if (!state.autoRefresh) return;
  state.autoRefreshTimer = setInterval(() => {
    const activeView = document.querySelector(".view.active")?.id;
    if (activeView === "view-dashboard") loadDashboard();
    if (activeView === "view-approvals") loadApprovalQueue();
    if (activeView === "view-chapter" && state.currentChapterId) loadChapter(state.currentChapterId);
  }, 15000);
}

async function globalRefresh() {
  await loadDashboard();
  if (state.currentChapterId) await loadChapter(state.currentChapterId);
  await loadApprovalQueue();
  notify("전체 화면을 새로고침했습니다.");
}

function attachEvents() {
  document.getElementById("nav-dashboard").onclick = () => {
    showView("dashboard");
    loadDashboard();
  };
  document.getElementById("nav-approval").onclick = () => {
    showView("approvals");
    loadApprovalQueue();
  };
  document.getElementById("nav-create").onclick = () => showView("create");
  document.getElementById("refresh-approvals").onclick = loadApprovalQueue;
  document.getElementById("refresh-chapter").onclick = () => loadChapter();
  document.getElementById("back-dashboard").onclick = () => {
    showView("dashboard");
    loadDashboard();
  };
  document.getElementById("toggle-render").onclick = () => {
    state.renderMode = state.renderMode === "rendered" ? "raw" : "rendered";
    if (state.selectedArtifact) loadArtifact(state.selectedArtifact);
  };
  document.getElementById("load-diff").onclick = loadDiff;
  document.getElementById("approval-form").onsubmit = submitApproval;
  document.getElementById("create-chapter-form").onsubmit = submitCreateChapter;

  document.getElementById("chapter-search").oninput = (event) => {
    state.chapterFilter = event.target.value;
    applyChapterTableFilters();
  };
  document.getElementById("chapter-status-filter").onchange = (event) => {
    state.statusFilter = event.target.value;
    applyChapterTableFilters();
  };

  document.getElementById("artifact-search").oninput = (event) => {
    state.artifactFilter = event.target.value;
    loadChapter();
  };

  document.getElementById("global-refresh").onclick = globalRefresh;
  document.getElementById("auto-refresh-toggle").onchange = (event) => {
    state.autoRefresh = event.target.checked;
    setupAutoRefresh();
    notify(state.autoRefresh ? "자동 새로고침을 켰습니다." : "자동 새로고침을 껐습니다.");
  };
}

attachEvents();
setupAutoRefresh();
loadDashboard();
