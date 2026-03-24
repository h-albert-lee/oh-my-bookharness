"""Global test configuration.

Injects MockLLMBackend so all tests run without a real API key.
"""

from __future__ import annotations

import pytest

from bookharness.llm import reset_backend, set_backend
from tests.mock_backend import MockLLMBackend


@pytest.fixture(autouse=True)
def mock_llm(request):
    """Inject mock LLM backend for every test."""
    backend = MockLLMBackend()
    set_backend(backend)
    yield backend
    reset_backend()
