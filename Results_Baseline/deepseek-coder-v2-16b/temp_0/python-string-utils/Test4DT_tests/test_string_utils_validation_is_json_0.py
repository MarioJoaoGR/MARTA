# Module: string_utils.validation
import pytest
from string_utils.validation import is_json
import json
from typing import Any

# Helper function to check if the input string contains at least one non-whitespace character
def is_full_string(input_string: str) -> bool:
    return bool(input_string and not input_string.isspace())

# Test cases for the is_json function
@pytest.mark.parametrize("test_input, expected", [
    ('{"name": "Peter"}', True),  # Valid JSON string (object)
    ('[1, 2, 3]', True),           # Valid JSON string (array)
    ('{nope}', False),             # Invalid JSON string
    ('', False),                   # Empty string
    (' ', False),                  # String consisting only of whitespace
    (None, False),                 # Passing None
])
def test_is_json(test_input: Any, expected: bool):
    assert is_json(test_input) == expected
