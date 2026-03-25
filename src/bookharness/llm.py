"""LLM backend abstraction for bookharness agents.

Every agent MUST call the LLM backend. There is no template fallback.
Tests inject a MockLLMBackend via set_backend().

Configuration:
- BOOKHARNESS_LLM_PROVIDER: "anthropic" (default) or "openai"
- ANTHROPIC_API_KEY / OPENAI_API_KEY: API key for the chosen provider
- BOOKHARNESS_MODEL: Model ID (provider-specific default if unset)
- BOOKHARNESS_MAX_TOKENS: Max output tokens (default: 8192)
"""

from __future__ import annotations

import os
from typing import Protocol


class LLMBackend(Protocol):
    """Protocol for LLM backends."""

    def generate(self, system: str, user: str, *, max_tokens: int | None = None) -> str: ...


class AnthropicBackend:
    """Production backend using the Anthropic Claude API."""

    def __init__(
        self,
        model: str | None = None,
        max_tokens: int | None = None,
        api_key: str | None = None,
    ) -> None:
        try:
            import anthropic
        except ImportError as exc:
            raise ImportError(
                "anthropic package is required. "
                "Install with: pip install 'bookharness[llm]'"
            ) from exc
        self.model = model or os.environ.get("BOOKHARNESS_MODEL", "claude-sonnet-4-6")
        self.default_max_tokens = max_tokens or int(os.environ.get("BOOKHARNESS_MAX_TOKENS", "8192"))
        timeout = float(os.environ.get("BOOKHARNESS_TIMEOUT", "300"))
        self.client = anthropic.Anthropic(
            api_key=api_key,
            timeout=timeout,
        )

    def generate(self, system: str, user: str, *, max_tokens: int | None = None) -> str:
        response = self.client.messages.create(
            model=self.model,
            max_tokens=max_tokens or self.default_max_tokens,
            system=system,
            messages=[{"role": "user", "content": user}],
        )
        return response.content[0].text

    def search_web(self, query: str, *, max_tokens: int | None = None) -> str:
        """Call LLM with web search tool enabled. Returns text with grounded citations."""
        response = self.client.messages.create(
            model=self.model,
            max_tokens=max_tokens or self.default_max_tokens,
            tools=[{"type": "web_search_20250305", "name": "web_search"}],
            messages=[{"role": "user", "content": query}],
        )
        # Extract all text blocks from the response
        parts = []
        for block in response.content:
            if hasattr(block, "text"):
                parts.append(block.text)
        return "\n\n".join(parts) if parts else ""


class OpenAIBackend:
    """Production backend using the OpenAI Chat Completions API."""

    DEFAULT_MODEL = "gpt-4o"

    def __init__(
        self,
        model: str | None = None,
        max_tokens: int | None = None,
        api_key: str | None = None,
    ) -> None:
        try:
            import openai
        except ImportError as exc:
            raise ImportError(
                "openai package is required. "
                "Install with: pip install 'bookharness[openai]'"
            ) from exc
        self.model = model or os.environ.get("BOOKHARNESS_MODEL", self.DEFAULT_MODEL)
        self.default_max_tokens = max_tokens or int(os.environ.get("BOOKHARNESS_MAX_TOKENS", "8192"))
        self.client = openai.OpenAI(api_key=api_key)

    def generate(self, system: str, user: str, *, max_tokens: int | None = None) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            max_tokens=max_tokens or self.default_max_tokens,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
        )
        return response.choices[0].message.content


_backend: LLMBackend | None = None


class _BuiltinMockBackend:
    """Minimal built-in mock for CLI testing (activated by BOOKHARNESS_MOCK=1)."""

    def generate(self, system: str, user: str, *, max_tokens: int | None = None) -> str:
        # Return minimal but parseable content for each agent role
        if "리뷰" in system or "Reviewer" in system:
            return '```json\n{"must_fix": [], "should_fix": [], "nice_to_have": [], "score": {"technical_accuracy": 4, "source_grounding": 4, "clarity": 4, "tone_fit": 4, "reader_friendliness": 4, "redundancy": 5, "continuity": 4, "dependency_coverage": 5}}\n```'
        if "집필자" in system or "Draft Writer" in system:
            title = "제목 미정"
            for line in user.splitlines():
                if "제목:" in line:
                    title = line.split("제목:", 1)[1].strip()
                    break
            return f"# {title}\n\n이 장에서는 핵심 주제를 다룬다.\n\n## 도입\n\n독자에게 이 장의 내용을 안내한다.[^source_1]\n\n## 핵심 개념\n\n주요 개념을 설명한다.\n\n## 정리\n\n다음 장에서는 이 내용을 확장한다.\n"
        if "장 설계자" in system or "Chapter Architect" in system:
            return "# Outline\n\n## Section 1. 도입\n\n- 목적: 주제 소개\n\n## Section 2. 핵심 개념\n\n- 목적: 개념 정의\n"
        if "편집장" in system or "Chief Editor" in system:
            return "# Chapter Brief\n\n## 이 장의 목표\n\n- 핵심 개념을 설명한다.\n\n## 반드시 들어갈 개념\n\n- workflow state\n"
        if "수정 통합" in system or "Revision Synth" in system:
            return "# Revision Plan\n\n## Must Fix\n\n- 없음\n\n## Should Fix\n\n- 용어 확인\n"
        return "# Generated\n\nContent.\n"


def get_backend() -> LLMBackend:
    """Return the configured LLM backend (singleton).

    Priority:
    1. Explicitly set backend (via set_backend())
    2. Built-in mock (if BOOKHARNESS_MOCK=1)
    3. BOOKHARNESS_LLM_PROVIDER explicit choice ("anthropic" or "openai")
    4. Auto-detect: OPENAI_API_KEY → OpenAI, ANTHROPIC_API_KEY → Anthropic
    5. Raise RuntimeError
    """
    global _backend
    if _backend is not None:
        return _backend
    if os.environ.get("BOOKHARNESS_MOCK") == "1":
        _backend = _BuiltinMockBackend()
        return _backend

    provider = os.environ.get("BOOKHARNESS_LLM_PROVIDER", "").lower()

    if provider == "openai":
        if not os.environ.get("OPENAI_API_KEY"):
            raise RuntimeError("BOOKHARNESS_LLM_PROVIDER=openai but OPENAI_API_KEY is not set.")
        _backend = OpenAIBackend()
        return _backend

    if provider == "anthropic":
        if not os.environ.get("ANTHROPIC_API_KEY"):
            raise RuntimeError("BOOKHARNESS_LLM_PROVIDER=anthropic but ANTHROPIC_API_KEY is not set.")
        _backend = AnthropicBackend()
        return _backend

    if provider and provider not in ("anthropic", "openai"):
        raise RuntimeError(f"Unknown BOOKHARNESS_LLM_PROVIDER: {provider!r}. Use 'anthropic' or 'openai'.")

    if os.environ.get("OPENAI_API_KEY"):
        _backend = OpenAIBackend()
        return _backend

    if os.environ.get("ANTHROPIC_API_KEY"):
        _backend = AnthropicBackend()
        return _backend

    raise RuntimeError(
        "No LLM backend configured. "
        "Set ANTHROPIC_API_KEY or OPENAI_API_KEY for production, "
        "BOOKHARNESS_MOCK=1 for testing, "
        "or call set_backend() in code."
    )


def set_backend(backend: LLMBackend) -> None:
    """Override the global LLM backend (for testing or custom backends)."""
    global _backend
    _backend = backend


def reset_backend() -> None:
    """Reset the global backend so it will be re-detected on next use."""
    global _backend
    _backend = None
