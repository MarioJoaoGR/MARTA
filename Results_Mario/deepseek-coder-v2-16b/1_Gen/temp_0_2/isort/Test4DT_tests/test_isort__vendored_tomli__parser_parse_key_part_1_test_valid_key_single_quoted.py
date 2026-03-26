
import pytest
from isort._vendored.tomli._parser import parse_key_part, Pos

def test_valid_key_single_quoted():
    src = "name = 'value'"
    pos = Pos(0)
    
    expected_pos = Pos(4)
    expected_key = "name"
    
    actual_pos, actual_key = parse_key_part(src, pos)
    
    assert actual_pos == expected_pos
    assert actual_key == expected_key
