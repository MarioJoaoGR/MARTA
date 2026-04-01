
import pytest
from string_utils.validation import JSON_WRAPPER_RE  # Assuming this import exists in the provided module
import json

def is_full_string(input_string):
    """Dummy implementation for testing purposes."""
    return bool(input_string and input_string.strip())

@pytest.mark.parametrize("test_input, expected", [
    ('{"name": "Peter"}', True),
    ('[1, 2, 3]', True),
    ('{nope}', False),
    (None, False),
    ('', False),
    (' ', False)
])
def test_invalid_json_string(test_input, expected):
    assert is_json(test_input) == expected

def is_json(input_string: str) -> bool:
    """Check if a string is a valid JSON."""
    if is_full_string(input_string) and JSON_WRAPPER_RE.match(input_string) is not None:
        try:
            parsed = json.loads(input_string)
            return isinstance(parsed, (dict, list))
        except (TypeError, ValueError, OverflowError):
            pass
    return False
