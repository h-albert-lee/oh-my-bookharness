from __future__ import annotations

from pathlib import Path

from bookharness.agents.chapter_architect import ChapterArchitectAgent
from bookharness.agents.chief_editor import ChiefEditorAgent
from bookharness.agents.continuity_reviewer import ContinuityReviewerAgent
from bookharness.agents.draft_writer import DraftWriterAgent
from bookharness.agents.research_librarian import ResearchLibrarianAgent
from bookharness.agents.revision_synthesizer import RevisionSynthesizerAgent
from bookharness.agents.source_analyst import SourceAnalystAgent
from bookharness.agents.style_reviewer import StyleReviewerAgent
from bookharness.agents.technical_reviewer import TechnicalReviewerAgent
from bookharness.llm import LLMBackend, get_backend
from bookharness.memory.loader import MemoryLoader
from bookharness.memory.summarizer import SummaryBuilder
from bookharness.models.chapter_state import ChapterState
from bookharness.orchestrator.state_manager import StateManager
from bookharness.reviews.evaluator import ReviewIO
from bookharness.reviews.gates import AcceptanceGate
from bookharness.utils.io import write_text
from bookharness.utils.yaml_utils import dump_yaml, load_yaml


class ApprovalRequiredError(RuntimeError):
    """Raised when a human approval stage is reached."""


class WorkflowRunner:
    def __init__(self, root: Path, backend: LLMBackend | None = None) -> None:
        self.root = root
        backend = backend or get_backend()
        self.loader = MemoryLoader(root)
        self.state_manager = StateManager(root)
        self.chief_editor = ChiefEditorAgent(root, backend)
        self.librarian = ResearchLibrarianAgent(root, backend)
        self.analyst = SourceAnalystAgent(root, backend)
        self.architect = ChapterArchitectAgent(root, backend)
        self.writer = DraftWriterAgent(root, backend)
        self.technical = TechnicalReviewerAgent(root, backend)
        self.style = StyleReviewerAgent(root, backend)
        self.continuity = ContinuityReviewerAgent(root, backend)
        self.synthesizer = RevisionSynthesizerAgent(root, backend)
        self.review_io = ReviewIO(root)
        self.gate = AcceptanceGate.from_rubrics(root)
        self.summarizer = SummaryBuilder()

    def initialize_chapter(self, chapter_id: str, title: str, dependencies: list[str] | None = None) -> ChapterState:
        self.loader.validate_required_documents()
        chapter_dir = self.root / f"manuscript/{chapter_id}"
        chapter_dir.mkdir(parents=True, exist_ok=True)
        state = ChapterState(chapter_id=chapter_id, title=title, dependencies=dependencies or [])
        self.state_manager.save(state)
        return state

    def run_stage(self, chapter_id: str, stage: str) -> ChapterState:
        state = self.state_manager.load(chapter_id)
        self.loader.load_project_context()
        prior_summaries = list(self.loader.load_prior_chapter_summaries().values())
        if stage == "brief_generation":
            self.chief_editor.generate_brief(chapter_id, state.title, state.dependencies, prior_summaries)
            state.status = "brief_generated"
        elif stage == "source_collection":
            self.librarian.collect_sources(chapter_id)
            state.status = "source_collection_done"
            state.source_pack_ready = True
        elif stage == "source_analysis":
            self.analyst.analyze(chapter_id)
            state.status = "source_analysis_done"
        elif stage == "outline_design":
            self.architect.build_outline(chapter_id, state.title)
            state.status = "outline_ready"
            state.outline_ready = True
        elif stage == "human_approval_a":
            state.status = "awaiting_human_outline_approval"
            state.current_stage = stage
            self.state_manager.save(state)
            raise ApprovalRequiredError("Approval A required for brief, source bundle, and outline.")
        elif stage == "draft_writing":
            draft_path = self.writer.write(chapter_id, state.title)
            state.status = "draft_generated"
            state.latest_draft = draft_path.name
            state.draft_versions.append(draft_path.name)
        elif stage == "automated_review":
            reports = [
                self.technical.review(chapter_id),
                self.style.review(chapter_id),
                self.continuity.review(chapter_id),
            ]
            for report in reports:
                self.review_io.write_report(chapter_id, report)
            state.review_reports = [
                "review_technical_v1.md",
                "review_style_v1.md",
                "review_continuity_v1.md",
            ]
            gate_result = self.gate.evaluate(reports)
            state.gate_passed = gate_result["passed"]
            state.gate_details = gate_result
            state.status = "auto_review_done"
        elif stage == "revision_plan_synthesis":
            reports = self.review_io.load_reports(chapter_id)
            plan_path = self.synthesizer.synthesize(chapter_id, reports)
            state.status = "revision_ready"
            state.revision_plan = plan_path.name
        elif stage == "draft_revision":
            draft_path = self.writer.write(chapter_id, state.title, revision_mode=True)
            version = draft_path.stem.replace("draft_v", "")
            write_text(
                self.root / f"manuscript/{chapter_id}/change_log_v{version}.md",
                f"# Change Log v{version}\n\n- revision plan을 반영해 draft를 재생성했다.",
            )
            state.latest_draft = draft_path.name
            state.draft_versions.append(draft_path.name)
            state.status = "awaiting_human_draft_approval"
        elif stage == "human_approval_b":
            state.current_stage = stage
            self.state_manager.save(state)
            raise ApprovalRequiredError("Approval B required for revised draft and review summary.")
        else:
            raise ValueError(f"Unsupported stage: {stage}")

        state.current_stage = stage
        state.artifacts.update(self._collect_artifacts(chapter_id))
        self.state_manager.save(state)
        return state

    def approve(self, chapter_id: str, approval_key: str, result: str, notes: list[str] | None = None) -> ChapterState:
        state = self.state_manager.load(chapter_id)
        approvals_path = self.root / "workflow/approvals/approvals.yaml"
        approvals = load_yaml(approvals_path) or {}
        approvals.setdefault(chapter_id, {})[approval_key] = {
            "result": result,
            "notes": notes or [],
        }
        dump_yaml(approvals_path, approvals)

        if notes:
            state.human_feedback.append({
                "approval_key": approval_key,
                "result": result,
                "notes": notes,
            })

        if approval_key == "approval_a":
            if result in {"approved", "approved_with_notes"}:
                state.status = "outline_ready"
                state.current_stage = "human_approval_a"
            elif result == "revision_requested":
                state.status = "outline_ready"
                state.current_stage = "outline_design"
            elif result == "rejected":
                state.status = "brief_generated"
                state.current_stage = "brief_generation"
        elif approval_key == "approval_b":
            if result in {"approved", "approved_with_notes"}:
                final_candidate = self.root / f"manuscript/{chapter_id}/final_candidate.md"
                latest = self.root / f"manuscript/{chapter_id}/{state.latest_draft}"
                write_text(final_candidate, latest.read_text(encoding="utf-8"))
                self.summarizer.write_summary_files(self.root, chapter_id, final_candidate)
                state.approved = True
                state.status = "chapter_approved"
                state.current_stage = "human_approval_b"
            elif result == "revision_requested":
                state.status = "revision_ready"
                state.current_stage = "revision_plan_synthesis"
            elif result == "rejected":
                state.status = "draft_generated"
                state.current_stage = "draft_writing"

        self.state_manager.save(state)
        return state

    def run_mvp(self, chapter_id: str, title: str, dependencies: list[str] | None = None) -> ChapterState:
        """Run the full MVP pipeline for a single chapter.

        Executes stages up to draft_revision, then stops at awaiting_human_draft_approval.
        The human_approval_a gate is included in run_stage but skipped here for MVP convenience.
        Use run_full() for the complete pipeline with approval gates.
        """
        state = self.initialize_chapter(chapter_id, title, dependencies)
        for stage in [
            "brief_generation",
            "source_collection",
            "source_analysis",
            "outline_design",
            "draft_writing",
            "automated_review",
            "revision_plan_synthesis",
            "draft_revision",
        ]:
            state = self.run_stage(chapter_id, stage)
        return state

    def run_full(self, chapter_id: str, title: str, dependencies: list[str] | None = None) -> ChapterState:
        """Run the complete pipeline including approval gates.

        Stops at the first approval gate (human_approval_a).
        After approval, call resume_after_approval() to continue.
        """
        state = self.initialize_chapter(chapter_id, title, dependencies)
        for stage in [
            "brief_generation",
            "source_collection",
            "source_analysis",
            "outline_design",
            "human_approval_a",
        ]:
            state = self.run_stage(chapter_id, stage)
        return state

    def resume_after_approval(self, chapter_id: str) -> ChapterState:
        """Resume pipeline after an approval gate.

        After approval_a: runs draft_writing through draft_revision, then stops at human_approval_b.
        After approval_b: chapter is already complete.
        """
        state = self.state_manager.load(chapter_id)
        if state.status == "chapter_approved":
            return state
        if state.current_stage == "human_approval_a":
            for stage in [
                "draft_writing",
                "automated_review",
                "revision_plan_synthesis",
                "draft_revision",
                "human_approval_b",
            ]:
                state = self.run_stage(chapter_id, stage)
        return state

    def _collect_artifacts(self, chapter_id: str) -> dict[str, str]:
        chapter_dir = self.root / f"manuscript/{chapter_id}"
        artifacts = {}
        for path in sorted(chapter_dir.glob("*.md")):
            artifacts[path.stem] = str(path.relative_to(self.root))
        pack_dir = self.root / f"sources/chapter_packs/{chapter_id}"
        if pack_dir.exists():
            for path in sorted(pack_dir.glob("*")):
                if path.is_file():
                    artifacts[f"source_{path.stem}"] = str(path.relative_to(self.root))
        return artifacts
