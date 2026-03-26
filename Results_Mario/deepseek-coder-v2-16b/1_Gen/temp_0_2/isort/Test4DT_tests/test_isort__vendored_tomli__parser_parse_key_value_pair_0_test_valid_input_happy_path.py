
from isort._vendored.tomli._parser import parse_key_value_pair, Pos
import pytest

def test_valid_input_happy_path():
    src = 'name = 3.14'
    pos = Pos(0)
    parsed_pos, parsed_key, value = parse_key_value_pair(src, pos, float)
    
    # Assert that the parsing correctly identifies and assigns the float value to `value`
    assert isinstance(value, float)
    assert value == 3.14
