# Module: typesystem.base
import pytest
from typesystem.base import Position

# Test case 1: Creating a Position at line 1, column 5, and character index 20
def test_position_creation():
    pos = Position(1, 5, 20)
    assert pos.line_no == 1
    assert pos.column_no == 5
    assert pos.char_index == 20

# Test case 2: Creating a Position at line 3, column 8, and character index 30
def test_position_creation_different():
    pos = Position(3, 8, 30)
    assert pos.line_no == 3
    assert pos.column_no == 8
    assert pos.char_index == 30

# Test case 3: Creating a Position at line 10, column 1, and character index 100
def test_position_creation_large():
    pos = Position(10, 1, 100)
    assert pos.line_no == 10
    assert pos.column_no == 1
    assert pos.char_index == 100

# Test case 4: Checking the string representation of a Position object
def test_position_repr():
    pos = Position(1, 5, 20)
    expected_repr = "Position(line_no=1, column_no=5, char_index=20)"
    assert repr(pos) == expected_repr
