
import pytest
from isort._vendored.tomli._parser import parse_hex_char, Pos

def test_parse_hex_char():
    src = "Hello, world!"
    pos = Pos(7)
    hex_len = 2
    
    with pytest.raises(ValueError):
        parse_hex_char(src, pos, hex_len)
