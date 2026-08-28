# Module: typesystem.base
import pytest
from typesystem.base import Position

# Test creating a Position object with specific values for line number, column number, and character index
def test_position_creation():
    pos = Position(line_no=1, column_no=5, char_index=20)
    assert pos.line_no == 1
    assert pos.column_no == 5
    assert pos.char_index == 20

# Test comparing two Position objects for equality when all attributes are the same
def test_position_equal_same():
    pos1 = Position(line_no=1, column_no=5, char_index=20)
    pos2 = Position(line_no=1, column_no=5, char_index=20)
    assert pos1 == pos2  # True, because all attributes are the same

# Test comparing two Position objects for equality when line number is different
def test_position_equal_different_line():
    pos1 = Position(line_no=1, column_no=5, char_index=20)
    pos3 = Position(line_no=2, column_no=1, char_index=25)
    assert not (pos1 == pos3)  # False, because line_no is different

# Test comparing two Position objects for equality when column number is different
def test_position_equal_different_column():
    pos1 = Position(line_no=1, column_no=5, char_index=20)
    pos4 = Position(line_no=1, column_no=6, char_index=20)
    assert not (pos1 == pos4)  # False, because column_no is different

# Test comparing two Position objects for equality when character index is different
def test_position_equal_different_char():
    pos1 = Position(line_no=1, column_no=5, char_index=20)
    pos5 = Position(line_no=1, column_no=5, char_index=21)
    assert not (pos1 == pos5)  # False, because char_index is different

# Test the string representation of a Position object
def test_position_repr():
    pos = Position(line_no=1, column_no=5, char_index=20)
    assert repr(pos) == "Position(line_no=1, column_no=5, char_index=20)"
