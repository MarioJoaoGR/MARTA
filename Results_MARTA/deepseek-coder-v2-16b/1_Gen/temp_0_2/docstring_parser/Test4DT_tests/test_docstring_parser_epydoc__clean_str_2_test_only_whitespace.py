
import pytest
from typing import Optional

def _clean_str(string: str) -> Optional[str]:
    string = string.strip()
    if len(string) > 0:
        return string
    return None

@pytest.mark.parametrize("input_string, expected", [
    ("   ", None),
    ("\t \n", None),
    ("     ", None),
    ("", None),
    ("Hello, World!", "Hello, World!")
])
def test_only_whitespace(input_string, expected):
    assert _clean_str(input_string) == expected
