# Module: string_utils.validation
import pytest
from string_utils.validation import is_json
import json
from typing import Any

# Helper function to check if a string contains at least one non-whitespace character
def is_full_string(s: str) -> bool:
    return s and s.strip()

# Test cases for the is_json function
@pytest.mark.parametrize("input_string, expected", [
    ('{"name": "Peter"}', True),  # Valid JSON object
    ('[1, 2, 3]', True),           # Valid JSON array
    ('{nope}', False),             # Invalid JSON string
    (None, False),                 # Non-string input
    ('', False),                   # Empty string
    (' ', False),                  # Whitespace string
])
def test_is_json(input_string: Any, expected: bool):
    assert is_json(input_string) == expected
