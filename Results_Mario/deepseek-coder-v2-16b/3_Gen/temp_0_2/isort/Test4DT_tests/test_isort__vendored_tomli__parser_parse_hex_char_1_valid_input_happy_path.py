
from isort._vendored.tomli._parser import parse_hex_char
from isort._vendored.tomli._parser import Pos
import pytest

def test_parse_hex_char_valid_input():
    src = "1a3f"
    pos = 0
    hex_len = 2
    
    new_pos, char = parse_hex_char(src, pos, hex_len)
    
    assert new_pos == 2
    assert char == '\x1a'
