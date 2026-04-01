
from typing import Any

import pytest

from isort.literal import _set


# Mocking ISortPrettyPrinter for testing purposes
class MockISortPrettyPrinter:
    def pformat(self, value: tuple[Any]) -> str:
        return f"[{', '.join(map(str, value))}]"

def test_set():
    custom_printer = MockISortPrettyPrinter()
    result = _set({3, 1, 2}, custom_printer)
    assert result == "{1, 2, 3}"
