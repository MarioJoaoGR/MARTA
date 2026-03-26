
import pytest
from typing import Tuple

# Assuming HEXDIGIT_CHARS is a set of valid hexadecimal characters
HEXDIGIT_CHARS = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'A', 'B', 'C', 'D', 'E', 'F'}

def parse_hex_char(src: str, pos: int, hex_len: int) -> Tuple[int, str]:
    hex_str = src[pos : pos + hex_len]
    if len(hex_str) != hex_len or not HEXDIGIT_CHARS.issuperset(hex_str):
        raise ValueError("Invalid hex value")
    pos += hex_len
    hex_int = int(hex_str, 16)
    if not is_unicode_scalar_value(hex_int):
        raise ValueError("Escaped character is not a Unicode scalar value")
    return pos, chr(hex_int)

def test_valid_input():
    src = '48656c6c6f20776f726c6421'
    pos = 0
    hex_len = 2
    
    expected_pos = 2
    expected_char = 'H'
    
    with pytest.raises(ValueError):
        parse_hex_char(src, pos, hex_len)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort__vendored_tomli__parser_parse_hex_char_0_test_valid_input
isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_hex_char_0_test_valid_input.py:14:11: E0602: Undefined variable 'is_unicode_scalar_value' (undefined-variable)


"""