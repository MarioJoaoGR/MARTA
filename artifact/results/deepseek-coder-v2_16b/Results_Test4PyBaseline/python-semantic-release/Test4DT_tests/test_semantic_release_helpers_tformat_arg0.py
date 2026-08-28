# Module: semantic_release.helpers
# Import the function from its module
from semantic_release.helpers import format_arg

import pytest

# Test cases for format_arg function
def test_format_string():
    assert format_arg("hello") == "'hello'"
    assert format_arg(" hello ") == "'hello'"
    # Additional test to ensure string is stripped of whitespace if present

def test_format_integer():
    assert format_arg(42) == '42'

def test_format_list():
    assert format_arg([1, 2, 3]) == '[1, 2, 3]'

def test_format_mixed_types():
    mixed_list = [format_arg("hello"), format_arg(42), format_arg([1, 2, 3])]
    assert mixed_list == ["'hello'", '42', '[1, 2, 3]']

def test_format_none():
    assert format_arg(None) == 'None'

def test_format_float():
    assert format_arg(3.14) == '3.14'

# Additional edge cases can be added to cover more scenarios
