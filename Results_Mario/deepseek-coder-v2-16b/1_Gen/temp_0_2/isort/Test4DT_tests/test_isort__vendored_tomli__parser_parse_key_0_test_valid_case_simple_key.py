
import pytest
from isort._vendored.tomli._parser import parse_key, Pos, Key

def test_valid_case_simple_key():
    src = 'name'
    pos = Pos(0)
    expected_pos = len(src)
    expected_key = ('name',)
    
    actual_pos, actual_key = parse_key(src, pos)
    
    assert actual_pos == expected_pos
    assert actual_key == expected_key
