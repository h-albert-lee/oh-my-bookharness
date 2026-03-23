const state = {
  currentChapterId: null,
  renderMode: "rendered",
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

function showView(name) {
  document.querySelectorAll(".view").forEach((view) => view.classList.remove("active"));
  document.querySelectorAll(".nav-button").forEach((button) => button.classList.remove("active"));
  document.getElementById(`view-${name}`).classList.add("active");
  const nav = document.getElementById(`nav-${name}`);
  if (nav) nav.classList.add("active");
}

function badge(status) {
  const css = status.includes("approved") ? "success" : status.includes("failed") || status.includes("rejected") ? "danger" : "warning";
  return `<span class="badge ${css}">${status}</span>`;
}

function escapeHtml(text) {
  return text
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;");
}

async function loadDashboard() {
  const project = await api("/api/project");
  document.getElementById("project-title").textContent = project.title;
  document.getElementById("metrics").innerHTML = Object.entries(project.metrics)
    .map(([label, value]) => `<div class="metric-card"><div class="label">${label}</div><div class="value">${value}</div></div>`)
    .join("");

  document.getElementById("chapter-table").innerHTML = project.chapters
    .map(
      (chapter) => `<tr>
        <td><strong>${chapter.chapter_id}</strong><br /><span class="subtle">${chapter.title}</span></td>
        <td>${badge(chapter.status)}</td>
        <td>${chapter.latest_draft || "-"}</td>
        <td><button data-open-chapter="${chapter.chapter_id}">열기</button></td>
      </tr>`
    )
    .join("");

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
            <div class="subtle">actor: ${run.actor}</div>
          </div>`
        )
        .join("")
    : `<p class="subtle">실행 이력이 없습니다.</p>`;

  document.querySelectorAll("[data-open-chapter]").forEach((button) => {
    button.onclick = () => openChapter(button.dataset.openChapter);
  });
}

async function loadApprovalQueue() {
  const items = await api("/api/approvals/pending");
  document.getElementById("approval-queue").innerHTML = items.length
    ? items
        .map(
          (item) => `<div class="approval-card">
            <div class="button-row" style="justify-content: space-between; align-items: center;">
              <div>
                <strong>${item.chapter_id}</strong> ${badge(item.status)}
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
}

async function openChapter(chapterId) {
  state.currentChapterId = chapterId;
  showView("chapter");
  await loadChapter(chapterId);
}

async function loadChapter(chapterId = state.currentChapterId) {
  const detail = await api(`/api/chapters/${chapterId}`);
  const chapter = detail.state;
  document.getElementById("chapter-heading").textContent = `${chapter.chapter_id} · ${chapter.title}`;
  document.getElementById("chapter-meta").innerHTML = `${badge(chapter.status)} current stage: ${chapter.current_stage}`;

  document.getElementById("stage-actions").innerHTML = stages
    .map((stage) => `<button data-stage="${stage}">${stage}</button>`)
    .join("");
  document.querySelectorAll("[data-stage]").forEach((button) => {
    button.onclick = async () => {
      await api(`/api/chapters/${chapterId}/run-stage`, {
        method: "POST",
        body: JSON.stringify({ stage: button.dataset.stage, actor: "ui-editor" }),
      });
      setTimeout(() => loadChapter(chapterId), 300);
    };
  });

  const artifactOptions = detail.artifacts
    .map((artifact) => `<div class="artifact-card"><button data-artifact="${artifact.path}">${artifact.name}</button></div>`)
    .join("");
  document.getElementById("artifact-list").innerHTML = artifactOptions || `<p class="subtle">산출물이 없습니다.</p>`;

  document.querySelectorAll("[data-artifact]").forEach((button) => {
    button.onclick = () => loadArtifact(button.dataset.artifact);
  });

  const draftArtifacts = detail.artifacts.filter((artifact) => artifact.name.startsWith("draft_") || artifact.name === "final_candidate.md");
  const diffOptions = draftArtifacts.map((artifact) => `<option value="${artifact.path}">${artifact.name}</option>`).join("");
  document.getElementById("diff-left").innerHTML = diffOptions;
  document.getElementById("diff-right").innerHTML = diffOptions;

  document.getElementById("review-cards").innerHTML = detail.review_reports.length
    ? detail.review_reports
        .map((report) => `<div class="review-card"><strong>${report.path}</strong><pre>${escapeHtml(report.content)}</pre></div>`)
        .join("")
    : `<p class="subtle">리뷰 산출물이 아직 없습니다.</p>`;

  document.getElementById("chapter-runs").innerHTML = detail.runs.length
    ? detail.runs.map((run) => `<div class="job-card"><strong>${run.job_type}</strong> ${badge(run.status)}<div class="subtle">${run.created_at}</div></div>`).join("")
    : `<p class="subtle">이 장의 job이 없습니다.</p>`;

  document.getElementById("chapter-audit").innerHTML = detail.audit.length
    ? detail.audit.map((item) => `<div class="audit-card"><strong>${item.event_type}</strong><div class="subtle">${item.actor} · ${item.timestamp}</div><pre>${escapeHtml(JSON.stringify(item.details, null, 2))}</pre></div>`).join("")
    : `<p class="subtle">감사 로그가 없습니다.</p>`;

  if (detail.artifacts.length) {
    await loadArtifact(detail.artifacts[0].path);
  } else {
    document.getElementById("artifact-viewer").innerHTML = `<p class="subtle">표시할 문서가 없습니다.</p>`;
  }
}

async function loadArtifact(path) {
  const artifact = await api(`/api/artifacts?path=${encodeURIComponent(path)}`);
  const container = document.getElementById("artifact-viewer");
  if (state.renderMode === "rendered" && artifact.rendered_html) {
    container.innerHTML = artifact.rendered_html;
  } else {
    container.innerHTML = `<pre>${escapeHtml(artifact.content)}</pre>`;
  }
}

async function loadDiff() {
  const left = document.getElementById("diff-left").value;
  const right = document.getElementById("diff-right").value;
  if (!left || !right) return;
  const diff = await api(`/api/artifacts/diff?left=${encodeURIComponent(left)}&right=${encodeURIComponent(right)}`);
  const changed = diff.changed
    .map((entry) => `<div class="badge ${entry.type === "added" ? "success" : "danger"}">${entry.type}</div><pre>${escapeHtml(entry.line)}</pre>`)
    .join("");
  document.getElementById("diff-viewer").innerHTML = changed || `<p class="subtle">차이가 없습니다.</p>`;
}

async function submitApproval(event) {
  event.preventDefault();
  const form = new FormData(event.target);
  const notes = String(form.get("notes") || "")
    .split("\n")
    .map((line) => line.trim())
    .filter(Boolean);
  await api(`/api/chapters/${state.currentChapterId}/approve`, {
    method: "POST",
    body: JSON.stringify({
      approval_key: form.get("approval_key"),
      result: form.get("result"),
      notes,
      actor: form.get("actor") || "editor_in_chief",
    }),
  });
  setTimeout(() => loadChapter(state.currentChapterId), 300);
}

async function submitCreateChapter(event) {
  event.preventDefault();
  const form = new FormData(event.target);
  const dependencies = String(form.get("dependencies") || "")
    .split(",")
    .map((item) => item.trim())
    .filter(Boolean);
  await api("/api/chapters", {
    method: "POST",
    body: JSON.stringify({
      chapter_id: form.get("chapter_id"),
      title: form.get("title"),
      dependencies,
      actor: form.get("actor") || "editor",
    }),
  });
  await loadDashboard();
  showView("dashboard");
}

function attachEvents() {
  document.getElementById("nav-dashboard").onclick = () => { showView("dashboard"); loadDashboard(); };
  document.getElementById("nav-approval").onclick = () => { showView("approvals"); loadApprovalQueue(); };
  document.getElementById("nav-create").onclick = () => showView("create");
  document.getElementById("refresh-dashboard").onclick = loadDashboard;
  document.getElementById("refresh-approvals").onclick = loadApprovalQueue;
  document.getElementById("refresh-chapter").onclick = () => loadChapter();
  document.getElementById("back-dashboard").onclick = () => { showView("dashboard"); loadDashboard(); };
  document.getElementById("toggle-render").onclick = () => {
    state.renderMode = state.renderMode === "rendered" ? "raw" : "rendered";
    const activeButton = document.querySelector("[data-artifact]");
    if (activeButton) loadArtifact(activeButton.dataset.artifact);
  };
  document.getElementById("load-diff").onclick = loadDiff;
  document.getElementById("approval-form").onsubmit = submitApproval;
  document.getElementById("create-chapter-form").onsubmit = submitCreateChapter;
}

attachEvents();
loadDashboard();
