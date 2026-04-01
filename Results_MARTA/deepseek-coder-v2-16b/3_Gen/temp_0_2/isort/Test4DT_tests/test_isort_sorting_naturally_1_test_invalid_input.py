
import pytest
from isort.sorting import naturally
from typing import Iterable, Callable, Any

def _natural_keys(text: str) -> list[Any]:
    """Helper function to extract natural sorting keys from a string."""
    import re
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    return [convert(part) for part in re.split('([0-9]+)', text)]

def test_invalid_input():
    with pytest.raises(TypeError):
        naturally(to_sort=[1, 2, 3])  # Expecting TypeError because input should be strings
