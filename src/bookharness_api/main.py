from __future__ import annotations

import argparse

import uvicorn

from bookharness_api.app import create_app


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="bookharness-api")
    parser.add_argument("--root", default=".")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8000)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    app = create_app(args.root)
    uvicorn.run(app, host=args.host, port=args.port)


if __name__ == "__main__":
    main()
