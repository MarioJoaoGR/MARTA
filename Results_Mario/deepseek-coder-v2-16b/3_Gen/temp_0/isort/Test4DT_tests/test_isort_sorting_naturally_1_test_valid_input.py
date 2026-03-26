
from typing import Any, Callable, Iterable

import pytest

from isort.sorting import naturally


def _natural_keys(text: str) -> list[Any]:
    """Helper function to create a tuple for natural sorting."""
    import re
    return [int(s) if s.isdigit() else s for s in re.split('([0-9]+)', text)]

def test_valid_input():
    # Test case with valid list of strings
    input_list = ['item12', 'item2', 'item1']
    expected_output = ['item1', 'item2', 'item12']
    
    result = naturally(input_list)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"
