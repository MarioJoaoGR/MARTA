
import pytest
from string import ascii_lowercase
from unittest.mock import patch

def is_full_string(input_string):
    return bool(input_string and input_string.strip())

def is_pangram(input_string: str) -> bool:
    if not is_full_string(input_string):
        return False

    return set(input_string.replace(" ", "").lower()).issuperset(set(ascii_lowercase))

@pytest.mark.parametrize("input_string, expected", [
    ('The quick brown fox jumps over the lazy dog', True),
    ('hello world', False),
    ('Sphinx of black quartz, judge my vow', True),
    ('', False),
    (' ', False)
])
def test_valid_pangram(input_string, expected):
    assert is_pangram(input_string) == expected
