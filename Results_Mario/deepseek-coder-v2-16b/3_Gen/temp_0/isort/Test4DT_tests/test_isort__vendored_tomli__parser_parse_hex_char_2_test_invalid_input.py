
import pytest

from isort._vendored.tomli._parser import (HEXDIGIT_CHARS, parse_hex_char,
                                           suffixed_err)


def test_invalid_input():
    with pytest.raises(ValueError) as excinfo:
        src = "Hello, world!"
        pos = 7
        hex_len = 2
        parse_hex_char(src, pos, hex_len)
    
    assert str(excinfo.value) == 'Invalid hex value (at line 1, column 8)'
