
import pytest
from string_utils.validation import is_json, is_full_string, JSON_WRAPPER_RE

@pytest.mark.parametrize("invalid_json", [
    '{nope}',
    '',
    ' ',
    None,
])
def test_invalid_json_string(invalid_json):
    assert not is_json(invalid_json)
