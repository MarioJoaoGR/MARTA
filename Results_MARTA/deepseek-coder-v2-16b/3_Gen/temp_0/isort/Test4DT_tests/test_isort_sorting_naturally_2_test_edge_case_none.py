
from typing import Any, Callable, Iterable

import pytest

from isort.sorting import naturally


def _natural_keys(text: str) -> list[Any]:
    """Helper function to create a tuple of numeric and alphabetic keys for natural sorting."""
    import re
    return [int(s) if s.isdigit() else s for s in re.split('([0-9]+)', text)]

def test_edge_case_none():
    with pytest.raises(TypeError):
        naturally(None)  # Test edge case with None input
