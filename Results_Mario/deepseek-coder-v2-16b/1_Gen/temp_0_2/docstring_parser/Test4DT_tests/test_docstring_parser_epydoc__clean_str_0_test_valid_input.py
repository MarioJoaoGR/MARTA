
import pytest
from typing import Optional

def _clean_str(string: str) -> Optional[str]:
    string = string.strip()
    if len(string) > 0:
        return string
    return None

@pytest.mark.parametrize("input_string, expected", [
    ('  Hello, World!  ', 'Hello, World!'),
    ('Hello, World!', 'Hello, World!'),
    ('   Hello, World!   ', 'Hello, World!'),
    ('', None),
    ('     ', None)
])
def test_valid_input(input_string, expected):
    assert _clean_str(input_string) == expected
