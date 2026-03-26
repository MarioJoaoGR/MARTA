
import pytest
from isort._vendored.tomli._parser import parse_key, Pos, Key

def test_valid_case_with_quotes():
    src = 'user."full name"'
    pos = 0
    
    expected_pos = len(src)
    expected_key = ('user', 'full name')
    
    actual_pos, actual_key = parse_key(src, Pos(pos))
    
    assert actual_pos == expected_pos
    assert actual_key == expected_key
