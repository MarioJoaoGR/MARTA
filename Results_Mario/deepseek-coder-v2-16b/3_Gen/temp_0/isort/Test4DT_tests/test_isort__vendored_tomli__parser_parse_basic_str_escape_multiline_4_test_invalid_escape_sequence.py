
import pytest
from isort._vendored.tomli._parser import parse_basic_str_escape_multiline
from isort._vendored.tomli._parser import Pos

def test_invalid_escape_sequence():
    src = 'Hello\\zWorld'  # Invalid escape sequence \z
    pos = Pos(0)
    
    with pytest.raises(ValueError):
        parse_basic_str_escape_multiline(src, pos)
