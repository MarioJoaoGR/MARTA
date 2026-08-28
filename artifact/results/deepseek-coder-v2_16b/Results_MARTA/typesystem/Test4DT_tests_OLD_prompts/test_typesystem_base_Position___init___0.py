
import pytest
from typesystem.base import Position

def test_valid_init():
    pos = Position(line_no=1, column_no=5, char_index=20)
    assert isinstance(pos, Position), "Expected an instance of Position"
    assert pos.line_no == 1, "Expected line_no to be 1"
    assert pos.column_no == 5, "Expected column_no to be 5"
    assert pos.char_index == 20, "Expected char_index to be 20"

def test_invalid_init():
    with pytest.raises(TypeError):
        Position()

def test_equality():
    pos1 = Position(line_no=1, column_no=5, char_index=20)
    pos2 = Position(line_no=1, column_no=5, char_index=20)
    assert pos1 == pos2, "Expected positions to be equal"

def test_inequality():
    pos1 = Position(line_no=1, column_no=5, char_index=20)
    pos2 = Position(line_no=2, column_no=1, char_index=30)
    assert not (pos1 == pos2), "Expected positions to be unequal"
