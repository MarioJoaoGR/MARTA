
import pytest
from isort._vendored.tomli._parser import parse_hex_char, HEXDIGIT_CHARS, is_unicode_scalar_value, suffixed_err
from typing import Tuple

def test_parse_hex_char_invalid_input():
    src = "a"
    pos = 0
    hex_len = 3
    
    with pytest.raises(ValueError) as excinfo:
        parse_hex_char(src, pos, hex_len)
    
    assert str(excinfo.value) == 'Invalid hex value (at line 1, column 1)'
