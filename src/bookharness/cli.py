from __future__ import annotations

import argparse
from pathlib import Path

import uvicorn

from bookharness.memory.updater import ensure_memory_files
from bookharness.orchestrator.runner import ApprovalRequiredError, WorkflowRunner
from bookharness.utils.io import write_text
from bookharness.utils.logging import get_logger
from bookharness.utils.yaml_utils import dump_yaml

LOGGER = get_logger(__name__)


def scaffold_project(root: Path) -> None:
    directories = [
        "book",
        "sources/raw/papers",
        "sources/raw/blogs",
        "sources/raw/talks",
        "sources/raw/docs",
        "sources/raw/interviews",
        "sources/normalized",
        "sources/metadata",
        "sources/chapter_packs",
        "manuscript/shared",
        "memory/chapter_summaries",
        "eval/rubrics",
        "eval/reports",
        "workflow/runs",
        "workflow/chapter_states",
        "workflow/approvals",
        "prompts/system",
        "prompts/tasks",
        "prompts/review",
        "prompts/rewrite",
        "scripts",
    ]
    for directory in directories:
        (root / directory).mkdir(parents=True, exist_ok=True)

    defaults = {
        "book/blueprint.md": "# Blueprint\n\n- 책 제목(가제)\n- 대상 독자\n- 핵심 차별점\n- 장 구성 개요\n",
        "book/tone_guide.md": "# Tone Guide\n\n- 한빛미디어 기술서 톤 지향\n- 선언문 스타일 금지\n- 과도한 수사 금지\n",
        "book/argument_map.md": "# Argument Map\n\n- AI 애플리케이션은 모델이 아니라 시스템으로 봐야 한다.\n",
        "book/decisions_log.md": "# Decisions Log\n\n- 과장된 표현을 사용하지 않는다.\n",
        "book/audience_profile.md": "# Audience Profile\n\n- 실무형 AI 시스템 설계 독자\n",
        "book/writing_rules.md": "# Writing Rules\n\n- Markdown-first\n- 승인 전 canonical 승격 금지\n",
    }
    for relative_path, content in defaults.items():
        path = root / relative_path
        if not path.exists():
            write_text(path, content)

    concept_dictionary_path = root / "book/concept_dictionary.yaml"
    if not concept_dictionary_path.exists():
        dump_yaml(
            concept_dictionary_path,
            {
                "harness": {
                    "preferred_korean": "평가 하네스",
                    "definition": "반복 가능하게 실행과 평가를 수행하는 외부 구조",
                    "notes": ["첫 등장 시 쉬운 설명을 덧붙인다"],
                }
            },
        )
    chapter_dependencies_path = root / "book/chapter_dependencies.yaml"
    if not chapter_dependencies_path.exists():
        dump_yaml(chapter_dependencies_path, {})

    ensure_memory_files(root)
    yaml_defaults = {
        root / "sources/metadata/registry.yaml": [],
        root / "workflow/approvals/approvals.yaml": {},
        root / "eval/rubrics/chapter_quality.yaml": {
            "clarity": {"description": "독자가 문단과 섹션 흐름을 쉽게 따라갈 수 있는가", "scale": "1-5"},
            "technical_accuracy": {"description": "기술 설명이 부정확하거나 과장되지 않았는가", "scale": "1-5"},
            "source_grounding": {"description": "핵심 주장들이 source pack에 의해 뒷받침되는가", "scale": "1-5"},
            "tone_fit": {"description": "책 전체 기술서 톤과 부합하는가", "scale": "1-5"},
            "continuity": {"description": "앞뒤 장 연결성이 자연스러운가", "scale": "1-5"},
            "reader_friendliness": {"description": "과도하게 추상적이거나 위압적이지 않은가", "scale": "1-5"},
            "redundancy": {"description": "불필요한 반복이 적절히 제어되는가", "scale": "1-5"},
        },
        root / "eval/rubrics/source_quality.yaml": {"authority": {"scale": "1-5"}, "relevance": {"scale": "1-5"}},
        root / "eval/rubrics/style_consistency.yaml": {"tone_fit": {"scale": "1-5"}, "terminology": {"scale": "1-5"}},
        root / "eval/rubrics/continuity.yaml": {"continuity": {"scale": "1-5"}, "redundancy": {"scale": "1-5"}},
    }
    for path, payload in yaml_defaults.items():
        if not path.exists():
            dump_yaml(path, payload)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="bookharness")
    subparsers = parser.add_subparsers(dest="command", required=True)

    init_project = subparsers.add_parser("init-project")
    init_project.add_argument("--root", default=".")

    init_chapter = subparsers.add_parser("init-chapter")
    init_chapter.add_argument("chapter_id")
    init_chapter.add_argument("title")
    init_chapter.add_argument("--root", default=".")
    init_chapter.add_argument("--depends-on", nargs="*", default=[])

    run_stage = subparsers.add_parser("run-stage")
    run_stage.add_argument("chapter_id")
    run_stage.add_argument("stage")
    run_stage.add_argument("--root", default=".")

    approve = subparsers.add_parser("approve")
    approve.add_argument("chapter_id")
    approve.add_argument("approval_key", choices=["approval_a", "approval_b"])
    approve.add_argument("result", choices=["approved", "approved_with_notes", "revision_requested", "rejected"])
    approve.add_argument("--root", default=".")
    approve.add_argument("--note", action="append", default=[])

    run_mvp = subparsers.add_parser("run-mvp")
    run_mvp.add_argument("chapter_id")
    run_mvp.add_argument("title")
    run_mvp.add_argument("--root", default=".")
    run_mvp.add_argument("--depends-on", nargs="*", default=[])

    serve = subparsers.add_parser("serve")
    serve.add_argument("--root", default=".")
    serve.add_argument("--host", default="127.0.0.1")
    serve.add_argument("--port", type=int, default=8000)
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    root = Path(args.root).resolve()

    if args.command == "init-project":
        scaffold_project(root)
        LOGGER.info("Initialized project scaffold at %s", root)
        return

    runner = WorkflowRunner(root)
    if args.command == "init-chapter":
        runner.initialize_chapter(args.chapter_id, args.title, args.depends_on)
        LOGGER.info("Initialized chapter %s", args.chapter_id)
        return
    if args.command == "run-stage":
        try:
            state = runner.run_stage(args.chapter_id, args.stage)
            LOGGER.info("Completed stage %s for %s with status %s", args.stage, args.chapter_id, state.status)
        except ApprovalRequiredError as exc:
            LOGGER.info(str(exc))
        return
    if args.command == "approve":
        state = runner.approve(args.chapter_id, args.approval_key, args.result, args.note)
        LOGGER.info("Recorded approval %s=%s for %s", args.approval_key, args.result, state.chapter_id)
        return
    if args.command == "run-mvp":
        state = runner.run_mvp(args.chapter_id, args.title, args.depends_on)
        LOGGER.info("Completed MVP run for %s; latest draft=%s", args.chapter_id, state.latest_draft)
        return
    if args.command == "serve":
        from bookharness_api.app import create_app

        uvicorn.run(create_app(root), host=args.host, port=args.port)
        return


if __name__ == "__main__":
    main()
