
import pytest
import typing as T

def _clean_str(string: str) -> T.Optional[str]:
    string = string.strip()
    if len(string) > 0:
        return string

# Test scenarios

@pytest.mark.parametrize("input_string, expected", [
    ("  Hello, World!  ", "Hello, World!"),
    ("Hello, World!", "Hello, World!")
])
def test_valid_input(input_string, expected):
    result = _clean_str(input_string)
    assert result == expected

def test_empty_string():
    result = _clean_str("")
    assert result is None

def test_whitespace_only():
    result = _clean_str("   ")
    assert result is None
