
import pytest
from string_utils.validation import is_pangram

def is_full_string(input_string: str) -> bool:
    return isinstance(input_string, str) and len(input_string.strip()) > 0

@pytest.mark.parametrize("input_string, expected", [
    ('The quick brown fox jumps over the lazy dog', True),
    ('hello world', False),
    (' ', False)
])
def test_is_pangram(input_string, expected):
    assert is_pangram(input_string) == expected
