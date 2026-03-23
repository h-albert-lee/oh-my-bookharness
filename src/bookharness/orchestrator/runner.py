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
from bookharness.memory.loader import MemoryLoader
from bookharness.memory.summarizer import SummaryBuilder
from bookharness.models.chapter_state import ChapterState
from bookharness.orchestrator.state_manager import StateManager
from bookharness.reviews.evaluator import ReviewEvaluator
from bookharness.utils.io import write_text
from bookharness.utils.yaml_utils import dump_yaml, load_yaml


class ApprovalRequiredError(RuntimeError):
    """Raised when a human approval stage is reached."""


class WorkflowRunner:
    def __init__(self, root: Path) -> None:
        self.root = root
        self.loader = MemoryLoader(root)
        self.state_manager = StateManager(root)
        self.chief_editor = ChiefEditorAgent(root)
        self.librarian = ResearchLibrarianAgent(root)
        self.analyst = SourceAnalystAgent(root)
        self.architect = ChapterArchitectAgent(root)
        self.writer = DraftWriterAgent(root)
        self.technical = TechnicalReviewerAgent(root)
        self.style = StyleReviewerAgent(root)
        self.continuity = ContinuityReviewerAgent(root)
        self.synthesizer = RevisionSynthesizerAgent(root)
        self.evaluator = ReviewEvaluator(root)
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
                self.evaluator.write_report(chapter_id, report)
            state.status = "auto_review_done"
            state.review_reports = [
                "review_technical_v1.md",
                "review_style_v1.md",
                "review_continuity_v1.md",
            ]
        elif stage == "revision_plan_synthesis":
            reports = [
                self.technical.review(chapter_id),
                self.style.review(chapter_id),
                self.continuity.review(chapter_id),
            ]
            plan_path = self.synthesizer.synthesize(chapter_id, reports)
            state.status = "revision_ready"
            state.revision_plan = plan_path.name
        elif stage == "draft_revision":
            draft_path = self.writer.write(chapter_id, state.title, revision_mode=True)
            write_text(self.root / f"manuscript/{chapter_id}/change_log_v2.md", "# Change Log v2\n\n- revision plan을 반영해 draft를 재생성했다.")
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
        if approval_key == "approval_b" and result in {"approved", "approved_with_notes"}:
            final_candidate = self.root / f"manuscript/{chapter_id}/final_candidate.md"
            latest = self.root / f"manuscript/{chapter_id}/{state.latest_draft}"
            write_text(final_candidate, latest.read_text(encoding="utf-8"))
            self.summarizer.write_summary_files(self.root, chapter_id, final_candidate)
            state.approved = True
            state.status = "chapter_approved"
            state.current_stage = "human_approval_b"
        self.state_manager.save(state)
        return state

    def run_mvp(self, chapter_id: str, title: str, dependencies: list[str] | None = None) -> ChapterState:
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

    def _collect_artifacts(self, chapter_id: str) -> dict[str, str]:
        chapter_dir = self.root / f"manuscript/{chapter_id}"
        artifacts = {}
        for path in sorted(chapter_dir.glob("*.md")):
            artifacts[path.stem] = str(path.relative_to(self.root))
        return artifacts
