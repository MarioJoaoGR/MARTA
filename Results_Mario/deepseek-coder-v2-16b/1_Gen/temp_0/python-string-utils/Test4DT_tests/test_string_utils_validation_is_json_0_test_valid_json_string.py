
import pytest
import json
from string_utils.validation import is_json, is_full_string, JSON_WRAPPER_RE

@pytest.mark.parametrize("test_input, expected", [
    ('{"name": "Peter"}', True),
    ('[1, 2, 3]', True),
    ('{nope}', False),
    ('', False),
    (' ', False),
    (None, False)
])
def test_valid_json_string(test_input, expected):
    assert is_json(test_input) == expected
