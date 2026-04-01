
import pytest
from isort._vendored.tomli._parser import parse_hex_char
from isort._vendored.tomli._parser import Pos

def is_unicode_scalar_value(n):
    return 0 <= n <= 0x10FFFF and (n <= 0xD7FF or n >= 0xE000)

@pytest.mark.parametrize("src, pos, hex_len, expected_pos, expected_char", [
    ("48", Pos(0), 2, Pos(2), 'H'),
    # Add more test cases as needed to cover different scenarios
])
def test_valid_input(src, pos, hex_len, expected_pos, expected_char):
    result_pos, result_char = parse_hex_char(src, pos, hex_len)
    assert result_pos == expected_pos
    assert result_char == expected_char
