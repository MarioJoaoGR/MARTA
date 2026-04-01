
import pytest
from typing import Tuple

# Assuming HEXDIGIT_CHARS and is_unicode_scalar_value are defined elsewhere in your codebase
HEXDIGIT_CHARS = set('0123456789abcdefABCDEF')
def is_unicode_scalar_value(hex_int: int) -> bool:
    return 0 <= hex_int <= 0x10FFFF and (hex_int < 0xD800 or hex_int > 0xDFFF)

def parse_hex_char(src: str, pos: int, hex_len: int) -> Tuple[int, str]:
    hex_str = src[pos : pos + hex_len]
    if len(hex_str) != hex_len or not HEXDIGIT_CHARS.issuperset(hex_str):
        raise ValueError("Invalid hex value")
    pos += hex_len
    hex_int = int(hex_str, 16)
    if not is_unicode_scalar_value(hex_int):
        raise ValueError("Escaped character is not a Unicode scalar value")
    return pos, chr(hex_int)

@pytest.mark.parametrize("src,pos,hex_len", [(None, 0, 2)])
def test_edge_case_none(src, pos, hex_len):
    with pytest.raises(TypeError):
        parse_hex_char(src, pos, hex_len)
