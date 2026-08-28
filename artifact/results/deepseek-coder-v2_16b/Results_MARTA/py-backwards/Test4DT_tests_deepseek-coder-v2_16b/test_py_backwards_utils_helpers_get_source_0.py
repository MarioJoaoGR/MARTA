
import pytest
from inspect import getsource
import re
from typing import Callable, Any

def get_source(fn: Callable[..., Any]) -> str:
    """Returns source code of the function."""
    source_lines = getsource(fn).split('\n')
    padding = len(re.findall(r'^(\s*)', source_lines[0])[0])
    return '\n'.join(line[padding:] for line in source_lines)

def example_function():
    """Example docstring."""
    pass

# Test Scenario 1: test_valid_input
def test_valid_input():
    assert get_source(example_function) == "def example_function():\n    \"\"\"Example docstring.\"\"\"\n    pass\n"

# Test Scenario 2: test_none_input
def test_none_input():
    with pytest.raises(TypeError):
        get_source(None)

# Test Scenario 3: test_invalid_input
def test_invalid_input():
    with pytest.raises(TypeError):
        get_source(12345)
