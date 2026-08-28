
import pytest
from thonny.roughparse import _is_char_in_string

def test__is_char_in_string_valid_index():
    """Test that _is_char_in_string returns 1 when the index is within string length."""
    text = "example"
    assert _is_char_in_string(0) == 1, f"_is_char_in_string(0) should return 1 but returned {_is_char_in_string(0)}"
    assert _is_char_in_string(6) == 1, f"_is_char_in_string(6) should return 1 but returned {_is_char_in_string(6)}"

