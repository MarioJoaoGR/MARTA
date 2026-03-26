
import pytest
from isort._vendored.tomli._parser import parse_hex_char, Pos

def test_parse_hex_char():
    # Test case for valid hex character parsing
    src = "48"
    pos = 0
    hex_len = 2
    expected = (Pos(2), 'H')
    
    result = parse_hex_char(src, pos, hex_len)
    assert result == expected

    # Test case for valid hex character parsing with different input
    src = "A1B2"
    pos = 0
    hex_len = 4
    expected = (Pos(4), 'ꆲ')
    
    result = parse_hex_char(src, pos, hex_len)
    assert result == expected
