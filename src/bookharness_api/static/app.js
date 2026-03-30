/* ── State ── */
const S = {
  chapterId: null,
  renderMode: "rendered",
  editing: false,
  chapterFilter: "",
  statusFilter: "all",
  artifactFilter: "",
  selectedArtifact: null,
  chapters: [],
  currentArtifacts: [],
  autoRefresh: true,
  timer: null,
};

const STAGES = [
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

const STAGE_LABELS = {
  brief_generation: "Brief",
  source_collection: "Sources",
  source_analysis: "Analysis",
  outline_design: "Outline",
  human_approval_a: "Approval A",
  draft_writing: "Draft",
  automated_review: "Review",
  revision_plan_synthesis: "Rev. Plan",
  draft_revision: "Revision",
  human_approval_b: "Approval B",
};

/* ── API ── */
async function api(path, opts = {}) {
  const res = await fetch(path, { headers: { "Content-Type": "application/json" }, ...opts });
  if (!res.ok) throw new Error(await res.text());
  return res.json();
}

/* ── Helpers ── */
function $(id) { return document.getElementById(id); }
function esc(t) { return String(t).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;"); }
function fmtDate(v) { if (!v) return "-"; const d = new Date(v); return isNaN(d) ? v : d.toLocaleString("ko-KR"); }

function notify(msg, err = false) {
  const t = $("toast");
  t.textContent = msg;
  t.className = err ? "toast error" : "toast";
  clearTimeout(t._tid);
  t._tid = setTimeout(() => t.classList.add("hidden"), 3000);
}

function badge(status) {
  const s = String(status || "unknown");
  const cls = s.includes("approved") || s.includes("completed") || s.includes("succeeded") ? "badge-success"
    : s.includes("failed") || s.includes("rejected") ? "badge-danger"
    : s.includes("running") || s.includes("queued") ? "badge-accent"
    : "badge-warning";
  return `<span class="badge ${cls}">${s.replace(/_/g, " ")}</span>`;
}

function showView(name) {
  document.querySelectorAll(".view").forEach(v => v.classList.remove("active"));
  document.querySelectorAll(".nav-btn").forEach(b => b.classList.remove("active"));
  $(`view-${name}`).classList.add("active");
  const nav = $(`nav-${name}`);
  if (nav) nav.classList.add("active");
}

function showLoading(on) { $("loading-overlay").classList.toggle("hidden", !on); }

/* ── Dashboard ── */
async function loadDashboard() {
  try {
    const p = await api("/api/project");
    S.chapters = p.chapters;
    $("project-title").textContent = p.title || "BookHarness";
    $("global-status").textContent = `${p.metrics.chapter_count} chapters · ${p.metrics.pending_approval_count} pending approvals`;

    // Approval badge
    const ab = $("approval-badge");
    if (p.metrics.pending_approval_count > 0) {
      ab.textContent = p.metrics.pending_approval_count;
      ab.classList.remove("hidden");
    } else {
      ab.classList.add("hidden");
    }

    $("metrics").innerHTML = [
      ["Chapters", p.metrics.chapter_count, "Total"],
      ["Approved", p.metrics.approved_count, "Final"],
      ["Pending", p.metrics.pending_approval_count, "Needs review"],
      ["Jobs", p.metrics.recent_run_count, "Recent"],
    ].map(([l,v,h]) => `<div class="metric"><div class="metric-label">${l}</div><div class="metric-value">${v}</div><div class="metric-hint">${h}</div></div>`).join("");

    populateStatusFilter(p.chapters);
    renderChapterTable();

    $("pending-approvals").innerHTML = p.pending_approvals.length
      ? p.pending_approvals.map(a => `<div class="approval-item"><div class="info"><strong>${a.chapter_id}</strong> <span class="subtle">${a.title}</span><div>${badge(a.status)} <span class="subtle">${a.approval_key}</span></div></div><button class="btn btn-sm" data-open="${a.chapter_id}">Review</button></div>`).join("")
      : `<div class="empty">No pending approvals</div>`;

    $("recent-runs").innerHTML = p.recent_runs.length
      ? p.recent_runs.map(r => `<div class="job-item"><div class="tl-head"><strong>${r.chapter_id || "-"}</strong> ${badge(r.status)}</div><div class="tl-sub">${r.job_type} · ${r.actor} · ${fmtDate(r.created_at)}</div></div>`).join("")
      : `<div class="empty">No recent jobs</div>`;

    bindOpenButtons();
  } catch (e) { notify(`Dashboard error: ${e.message}`, true); }
}

function populateStatusFilter(chapters) {
  const sel = $("chapter-status-filter");
  const statuses = [...new Set(chapters.map(c => c.status))].sort();
  sel.innerHTML = `<option value="all">All statuses</option>` + statuses.map(s => `<option value="${s}">${s.replace(/_/g," ")}</option>`).join("");
  sel.value = S.statusFilter;
}

function renderChapterTable() {
  const kw = S.chapterFilter.toLowerCase();
  const filtered = S.chapters.filter(c => {
    const hit = !kw || c.chapter_id.toLowerCase().includes(kw) || c.title.toLowerCase().includes(kw);
    const st = S.statusFilter === "all" || c.status === S.statusFilter;
    return hit && st;
  });

  const stageIdx = (c) => Math.max(STAGES.indexOf(c.current_stage), 0);

  $("chapter-table").innerHTML = filtered.length
    ? filtered.map(c => {
      const idx = stageIdx(c);
      const pct = Math.round(((idx + 1) / STAGES.length) * 100);
      return `<tr>
        <td><strong>${c.chapter_id}</strong><br><span class="subtle">${c.title}</span></td>
        <td>${badge(c.status)}</td>
        <td><div style="display:flex;align-items:center;gap:8px"><span class="subtle" style="font-size:11px;white-space:nowrap">${STAGE_LABELS[c.current_stage] || c.current_stage}</span><div class="progress-bar" style="flex:1"><div class="progress-fill" style="width:${pct}%"></div></div><span class="subtle" style="font-size:11px">${pct}%</span></div></td>
        <td><span class="subtle">${c.latest_draft || "-"}</span></td>
        <td><button class="btn btn-sm" data-open="${c.chapter_id}">Open</button></td>
      </tr>`;
    }).join("")
    : `<tr><td colspan="5" class="empty">No chapters match</td></tr>`;

  bindOpenButtons();
}

function bindOpenButtons() {
  document.querySelectorAll("[data-open]").forEach(b => {
    b.onclick = () => openChapter(b.dataset.open);
  });
}

/* ── Approval Queue ── */
async function loadApprovals() {
  try {
    const items = await api("/api/approvals/pending");
    $("approval-queue").innerHTML = items.length
      ? items.map((a, i) => `<div class="card" style="margin-bottom:12px"><div class="card-body"><div style="display:flex;justify-content:space-between;align-items:center"><div><strong>#${i+1} ${a.chapter_id}</strong> ${badge(a.status)}<div class="subtle">${a.title} · ${a.approval_key}</div></div><button class="btn btn-sm btn-primary" data-open="${a.chapter_id}">Review</button></div></div></div>`).join("")
      : `<div class="card"><div class="empty">No pending approvals</div></div>`;
    bindOpenButtons();
  } catch (e) { notify(`Approval error: ${e.message}`, true); }
}

/* ── Chapter Detail ── */
async function openChapter(id) {
  S.chapterId = id;
  S.selectedArtifact = null;
  S.editing = false;
  showView("chapter");
  await loadChapter();
}

async function loadChapter() {
  const id = S.chapterId;
  if (!id) return;
  try {
    const d = await api(`/api/chapters/${id}`);
    const c = d.state;
    S.currentArtifacts = d.artifacts;
    $("chapter-heading").textContent = `${c.chapter_id} · ${c.title}`;
    $("chapter-meta").innerHTML = `${badge(c.status)} · Stage: ${STAGE_LABELS[c.current_stage] || c.current_stage}`;

    renderPipeline(c);
    renderActions(c);
    renderArtifacts(d.artifacts);
    renderDiffOptions(d.artifacts);
    renderRuns(d.runs);
    renderAudit(d.audit);
    renderReviews(d.review_reports);

    if (d.artifacts.length && !S.selectedArtifact) {
      S.selectedArtifact = d.artifacts[0].path;
    }
    if (S.selectedArtifact) {
      await loadArtifact(S.selectedArtifact);
      renderArtifacts(d.artifacts);
    } else {
      $("artifact-viewer").innerHTML = `<div class="empty">No artifacts yet. Run a stage to generate content.</div>`;
      $("active-artifact").textContent = "No artifact selected";
    }
  } catch (e) { notify(`Chapter error: ${e.message}`, true); }
}

function renderPipeline(chapter) {
  const cur = Math.max(STAGES.indexOf(chapter.current_stage), 0);
  $("stage-progress").innerHTML = `<div class="pipeline">${STAGES.map((s, i) => {
    const cls = i < cur ? "done" : i === cur ? "current" : "todo";
    return `<div class="pipeline-step ${cls}"><span class="step-label">${STAGE_LABELS[s]}</span>${i < cur ? '<span class="badge badge-success step-badge">done</span>' : i === cur ? '<span class="badge badge-accent step-badge">current</span>' : ''}</div>`;
  }).join("")}</div>`;
}

function renderActions(chapter) {
  $("stage-actions").innerHTML = STAGES.map(s =>
    `<button class="btn btn-sm" data-run-stage="${s}" title="${s}">${STAGE_LABELS[s]}</button>`
  ).join("");

  document.querySelectorAll("[data-run-stage]").forEach(b => {
    b.onclick = async () => {
      try {
        showLoading(true);
        await api(`/api/chapters/${S.chapterId}/run-stage`, {
          method: "POST",
          body: JSON.stringify({ stage: b.dataset.runStage, actor: "ui-editor" }),
        });
        notify(`Queued: ${b.dataset.runStage}`);
        setTimeout(() => { showLoading(false); loadChapter(); }, 500);
      } catch (e) { showLoading(false); notify(`Failed: ${e.message}`, true); }
    };
  });

  // Run MVP button
  $("run-mvp-btn").onclick = async () => {
    try {
      showLoading(true);
      const detail = await api(`/api/chapters/${S.chapterId}`);
      await api(`/api/chapters/${S.chapterId}/run-mvp`, {
        method: "POST",
        body: JSON.stringify({ title: detail.state.title, dependencies: detail.state.dependencies || [], actor: "ui-editor" }),
      });
      notify("Full pipeline queued");
      setTimeout(() => { showLoading(false); loadChapter(); }, 500);
    } catch (e) { showLoading(false); notify(`MVP failed: ${e.message}`, true); }
  };
}

function renderArtifacts(artifacts) {
  const kw = S.artifactFilter.toLowerCase();
  const filtered = artifacts.filter(a => !kw || a.name.toLowerCase().includes(kw) || a.path.toLowerCase().includes(kw));
  $("artifact-list").innerHTML = filtered.length
    ? filtered.map(a => `<button class="artifact-chip ${S.selectedArtifact === a.path ? "active" : ""}" data-artifact="${a.path}">${a.name}</button>`).join("")
    : `<span class="subtle" style="padding:4px">No artifacts</span>`;

  document.querySelectorAll("[data-artifact]").forEach(b => {
    b.onclick = () => {
      S.selectedArtifact = b.dataset.artifact;
      S.editing = false;
      loadArtifact(b.dataset.artifact);
      renderArtifacts(artifacts);
    };
  });
}

async function loadArtifact(path) {
  try {
    const a = await api(`/api/artifacts?path=${encodeURIComponent(path)}`);
    $("active-artifact").textContent = a.path;
    const viewer = $("artifact-viewer");

    if (S.editing) {
      viewer.innerHTML = `<div style="display:flex;flex-direction:column;height:100%">
        <textarea id="editor-textarea" style="flex:1;min-height:400px;font-family:var(--mono);font-size:13px;line-height:1.6;background:var(--bg);color:var(--text);border:1px solid var(--border);border-radius:var(--radius);padding:12px;resize:vertical">${esc(a.content)}</textarea>
        <div style="display:flex;gap:8px;margin-top:8px;justify-content:flex-end">
          <button class="btn btn-ghost btn-sm" id="editor-cancel">Cancel</button>
          <button class="btn btn-primary btn-sm" id="editor-save">Save</button>
        </div>
      </div>`;
      $("editor-cancel").onclick = () => { S.editing = false; loadArtifact(path); };
      $("editor-save").onclick = async () => {
        const content = $("editor-textarea").value;
        try {
          showLoading(true);
          await api("/api/artifacts", {
            method: "PUT",
            body: JSON.stringify({ path: a.path, content, actor: "ui-editor" }),
          });
          S.editing = false;
          showLoading(false);
          notify("Saved successfully");
          await loadArtifact(path);
        } catch (e) { showLoading(false); notify(`Save failed: ${e.message}`, true); }
      };
    } else if (S.renderMode === "rendered" && a.rendered_html) {
      viewer.innerHTML = a.rendered_html;
    } else {
      viewer.innerHTML = `<pre>${esc(a.content)}</pre>`;
    }
  } catch (e) { notify(`Artifact error: ${e.message}`, true); }
}

function renderDiffOptions(artifacts) {
  const drafts = artifacts.filter(a => a.name.startsWith("draft_") || a.name === "final_candidate.md" || a.name.endsWith(".md"));
  const opts = drafts.map(a => `<option value="${a.path}">${a.name}</option>`).join("");
  $("diff-left").innerHTML = opts;
  $("diff-right").innerHTML = opts;
}

function renderRuns(runs) {
  $("chapter-runs").innerHTML = runs.length
    ? runs.map(r => `<div class="tl-item"><div class="tl-head"><span>${r.job_type}</span>${badge(r.status)}</div><div class="tl-sub">${r.actor} · ${fmtDate(r.created_at)}${r.finished_at ? ` → ${fmtDate(r.finished_at)}` : ""}</div>${r.error ? `<pre style="color:var(--danger);margin-top:4px">${esc(r.error)}</pre>` : ""}</div>`).join("")
    : `<div class="empty">No jobs yet</div>`;
}

function renderAudit(audit) {
  $("chapter-audit").innerHTML = audit.length
    ? audit.map(a => `<div class="tl-item"><div class="tl-head"><span>${a.event_type}</span></div><div class="tl-sub">${a.actor} · ${fmtDate(a.timestamp)}</div><details><summary class="subtle">Details</summary><pre>${esc(JSON.stringify(a.details, null, 2))}</pre></details></div>`).join("")
    : `<div class="empty">No audit entries</div>`;
}

function renderReviews(reports) {
  $("review-cards").innerHTML = reports.length
    ? reports.map(r => `<div class="review-item"><strong>${r.path}</strong><pre>${esc(r.content)}</pre></div>`).join("")
    : `<div class="empty">No review reports yet</div>`;
}

/* ── Diff ── */
async function loadDiff() {
  const l = $("diff-left").value, r = $("diff-right").value;
  if (!l || !r) return;
  try {
    const d = await api(`/api/artifacts/diff?left=${encodeURIComponent(l)}&right=${encodeURIComponent(r)}`);
    $("diff-viewer").innerHTML = d.changed.length
      ? d.changed.map(c => `<div class="${c.type === "added" ? "diff-add" : "diff-del"}">${c.type === "added" ? "+" : "-"} ${esc(c.line)}</div>`).join("")
      : `<div class="empty">No differences</div>`;
  } catch (e) { notify(`Diff error: ${e.message}`, true); }
}

/* ── Forms ── */
async function submitApproval(e) {
  e.preventDefault();
  const fd = new FormData(e.target);
  const notes = String(fd.get("notes") || "").split("\n").map(l => l.trim()).filter(Boolean);
  try {
    showLoading(true);
    await api(`/api/chapters/${S.chapterId}/approve`, {
      method: "POST",
      body: JSON.stringify({ approval_key: fd.get("approval_key"), result: fd.get("result"), notes, actor: fd.get("actor") || "editor" }),
    });
    showLoading(false);
    notify("Approval submitted");
    setTimeout(loadChapter, 300);
  } catch (e) { showLoading(false); notify(`Approval failed: ${e.message}`, true); }
}

async function submitCreate(e) {
  e.preventDefault();
  const fd = new FormData(e.target);
  const deps = String(fd.get("dependencies") || "").split(",").map(s => s.trim()).filter(Boolean);
  try {
    showLoading(true);
    await api("/api/chapters", {
      method: "POST",
      body: JSON.stringify({ chapter_id: fd.get("chapter_id"), title: fd.get("title"), dependencies: deps, actor: fd.get("actor") || "editor" }),
    });
    showLoading(false);
    notify("Chapter created");
    await loadDashboard();
    showView("dashboard");
  } catch (e) { showLoading(false); notify(`Create failed: ${e.message}`, true); }
}

/* ── Live Activity ── */
async function pollActivity() {
  try {
    const a = await api("/api/agent-logs/activity");
    const panel = $("live-activity");
    const detail = $("live-detail");
    panel.classList.remove("hidden");

    if (a.active) {
      panel.classList.remove("idle");
      const agent = a.last_agent || "unknown";
      const elapsed = a.last_elapsed ? `${a.last_elapsed}s` : "";
      const count = a.recent_count || 0;
      detail.textContent = `${agent} ${elapsed} · ${count} calls in 5min`;
    } else {
      panel.classList.add("idle");
      $("live-activity").querySelector(".live-label").textContent = "Idle";
      if (a.last_agent) {
        detail.textContent = `Last: ${a.last_agent} · ${fmtDate(a.last_timestamp)}`;
      } else {
        detail.textContent = "No activity yet";
      }
    }
  } catch (e) { /* silent */ }
}

/* ── Auto Refresh ── */
function setupAutoRefresh() {
  if (S.timer) clearInterval(S.timer);
  if (!S.autoRefresh) return;
  S.timer = setInterval(() => {
    const active = document.querySelector(".view.active")?.id;
    if (active === "view-dashboard") loadDashboard();
    if (active === "view-approvals") loadApprovals();
    if (active === "view-chapter" && S.chapterId && !S.editing) loadChapter();
    if (active === "view-logs") loadAgentLogs();
    pollActivity();
  }, 5000);
}

/* ── Agent Logs ── */
async function loadAgentLogs() {
  try {
    // Load agent list for filter
    const agents = await api("/api/agent-logs/agents");
    const sel = $("log-agent-filter");
    const current = sel.value;
    sel.innerHTML = `<option value="">All agents</option>` + agents.map(a => `<option value="${a}">${a}</option>`).join("");
    sel.value = current;

    const filter = sel.value;
    const url = filter ? `/api/agent-logs?agent=${encodeURIComponent(filter)}&limit=100` : "/api/agent-logs?limit=100";
    const logs = await api(url);

    $("agent-log-list").innerHTML = logs.length
      ? logs.map(l => {
        const hasError = !!l.error;
        return `<div class="card" style="margin-bottom:8px">
          <div class="card-body">
            <div class="tl-head">
              <div style="display:flex;align-items:center;gap:8px">
                <span class="badge badge-accent">${l.agent}</span>
                ${hasError ? '<span class="badge badge-danger">error</span>' : `<span class="badge badge-neutral">${l.elapsed_sec}s</span>`}
              </div>
              <span class="subtle">${fmtDate(l.timestamp)}</span>
            </div>
            ${hasError ? `<pre style="color:var(--danger);margin-top:8px;font-size:12px">${esc(l.error)}</pre>` : ""}
            <details style="margin-top:8px">
              <summary class="subtle">System prompt (preview)</summary>
              <pre style="font-size:12px;margin-top:4px;padding:8px;background:var(--bg);border-radius:var(--radius)">${esc(l.system_prompt_preview || "")}</pre>
            </details>
            <details style="margin-top:4px">
              <summary class="subtle">User prompt (preview)</summary>
              <pre style="font-size:12px;margin-top:4px;padding:8px;background:var(--bg);border-radius:var(--radius)">${esc(l.user_prompt_preview || "")}</pre>
            </details>
            <details style="margin-top:4px">
              <summary class="subtle">Response (preview)</summary>
              <pre style="font-size:12px;margin-top:4px;padding:8px;background:var(--bg);border-radius:var(--radius)">${esc(l.response_preview || "")}</pre>
            </details>
          </div>
        </div>`;
      }).join("")
      : `<div class="card"><div class="empty">No agent logs yet. Run a pipeline stage to generate logs.</div></div>`;
  } catch (e) { notify(`Agent logs error: ${e.message}`, true); }
}

/* ── Events ── */
function init() {
  $("nav-dashboard").onclick = () => { showView("dashboard"); loadDashboard(); };
  $("nav-approval").onclick = () => { showView("approvals"); loadApprovals(); };
  $("nav-create").onclick = () => showView("create");
  $("nav-logs").onclick = () => { showView("logs"); loadAgentLogs(); };
  $("global-refresh").onclick = async () => { await loadDashboard(); notify("Refreshed"); };
  $("refresh-approvals").onclick = loadApprovals;
  $("refresh-chapter").onclick = loadChapter;
  $("back-dashboard").onclick = () => { showView("dashboard"); loadDashboard(); };

  $("toggle-render").onclick = () => {
    if (S.editing) return;
    S.renderMode = S.renderMode === "rendered" ? "raw" : "rendered";
    $("toggle-render").textContent = S.renderMode === "rendered" ? "Show Raw" : "Show Rendered";
    if (S.selectedArtifact) loadArtifact(S.selectedArtifact);
  };

  // Edit button - add to viewer header
  const viewerHeader = $("toggle-render").parentElement;
  const editBtn = document.createElement("button");
  editBtn.className = "btn btn-ghost btn-sm";
  editBtn.id = "edit-artifact-btn";
  editBtn.textContent = "Edit";
  viewerHeader.prepend(editBtn);
  editBtn.onclick = () => {
    if (!S.selectedArtifact) return;
    S.editing = true;
    loadArtifact(S.selectedArtifact);
  };

  $("refresh-logs").onclick = loadAgentLogs;
  $("log-agent-filter").onchange = loadAgentLogs;
  $("load-diff").onclick = loadDiff;
  $("approval-form").onsubmit = submitApproval;
  $("create-chapter-form").onsubmit = submitCreate;

  $("chapter-search").oninput = (e) => { S.chapterFilter = e.target.value; renderChapterTable(); };
  $("chapter-status-filter").onchange = (e) => { S.statusFilter = e.target.value; renderChapterTable(); };
  $("artifact-search").oninput = (e) => { S.artifactFilter = e.target.value; if (S.currentArtifacts) renderArtifacts(S.currentArtifacts); };

  $("auto-refresh-toggle").onchange = (e) => {
    S.autoRefresh = e.target.checked;
    setupAutoRefresh();
    notify(S.autoRefresh ? "Auto-refresh on" : "Auto-refresh off");
  };

  setupAutoRefresh();
  pollActivity();
  loadDashboard();
}

init();
