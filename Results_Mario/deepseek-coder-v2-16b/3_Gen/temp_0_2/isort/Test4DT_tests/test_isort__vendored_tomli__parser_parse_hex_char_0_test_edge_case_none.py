
import pytest
from typing import Tuple

# Assuming HEXDIGIT_CHARS and is_unicode_scalar_value are defined elsewhere in your codebase
HEXDIGIT_CHARS = set('0123456789abcdefABCDEF')

def parse_hex_char(src: str, pos: int, hex_len: int) -> Tuple[int, str]:
    if src is None:
        raise ValueError("Source string cannot be None")
    hex_str = src[pos : pos + hex_len]
    if len(hex_str) != hex_len or not HEXDIGIT_CHARS.issuperset(hex_str):
        raise ValueError("Invalid hex value")
    pos += hex_len
    hex_int = int(hex_str, 16)
    if not is_unicode_scalar_value(hex_int):
        raise ValueError("Escaped character is not a Unicode scalar value")
    return pos, chr(hex_int)

# Mock function for testing purposes
def is_unicode_scalar_value(code_point: int) -> bool:
    return 0 <= code_point <= 0x10FFFF and (code_point < 0xD800 or code_point > 0xDFFF)

# Pytest function to test the edge case where src is None
def test_edge_case_none():
    with pytest.raises(ValueError):
        parse_hex_char(None, 0, 2)
