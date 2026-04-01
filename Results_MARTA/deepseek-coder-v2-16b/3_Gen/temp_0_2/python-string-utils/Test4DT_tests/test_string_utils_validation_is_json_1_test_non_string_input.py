
import pytest
from string_utils.validation import is_full_string, JSON_WRAPPER_RE
import json
from typing import Any

def is_json(input_string: Any) -> bool:
    """
    Check if a string is a valid JSON.

    This function verifies whether the provided `input_string` is a valid JSON object or array by attempting to parse it using `json.loads`. It first ensures that the input string is not empty and contains at least one non-whitespace character (using the `is_full_string` function). Then, it checks if the parsed result is either a dictionary (`dict`) or a list.

    *Examples:*

    - When you pass a valid JSON string to the function, it will return `True`:
      ```python
      >>> is_json('{"name": "Peter"}')  # returns True
      >>> is_json('[1, 2, 3]')  # returns True
      ```

    - When you pass an invalid JSON string or a non-string input to the function, it will return `False`:
      ```python
      >>> is_json('{nope}')  # returns False
      >>> is_json(None)  # returns False
      >>> is_json('')  # returns False
      >>> is_json(' ')  # returns False
      ```

    :param input_string: The string to check. It must be a valid JSON object or array for the function to return `True`.
    :type input_string: str
    :return: True if the input string is a valid JSON, False otherwise.
    """
    if is_full_string(input_string) and JSON_WRAPPER_RE.match(input_string) is not None:
        try:
            return isinstance(json.loads(input_string), (dict, list))
        except (TypeError, ValueError, OverflowError):
            pass

    return False

def test_non_string_input():
    # Test with non-string input
    assert not is_json('')  # Empty string should return False
    assert not is_json(None)  # None should return False
    assert not is_json(12345)  # Integer should return False
    assert not is_json({})  # Dictionary should return False
    assert not is_json([])  # List should return False
    assert not is_json(' ')  # Whitespace string should return False
    assert not is_json('{nope}')  # Invalid JSON string should return False

    # Test with valid JSON strings
    assert is_json('{"name": "Peter"}')  # Valid JSON object should return True
    assert is_json('[1, 2, 3]')  # Valid JSON array should return True
