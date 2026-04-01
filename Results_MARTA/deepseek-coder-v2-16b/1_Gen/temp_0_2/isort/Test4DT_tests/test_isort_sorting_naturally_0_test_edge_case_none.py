
import pytest
from isort.sorting import naturally
from typing import Iterable, Callable, Any

def _natural_keys(text: str) -> list[Any]:
    """Helper function to extract numeric keys from a string for natural sorting."""
    import re
    return [int(s) if s.isdigit() else s for s in re.split('([0-9]+)', text)]

def test_edge_case_none():
    with pytest.raises(TypeError):
        naturally(None)
