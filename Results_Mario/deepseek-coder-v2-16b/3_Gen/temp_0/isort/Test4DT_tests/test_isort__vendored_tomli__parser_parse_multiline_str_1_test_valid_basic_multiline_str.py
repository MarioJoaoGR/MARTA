
import pytest
from typing import Tuple
from isort._vendored.tomli._parser import parse_multiline_str, Pos

def test_valid_basic_multiline_str():
    src = '"""Hello\nWorld"""'
    pos = Pos(0)
    literal = False
    
    result = parse_multiline_str(src, pos, literal=literal)
    
    assert result[1] == "Hello\nWorld"
    assert isinstance(result[0], Pos)
