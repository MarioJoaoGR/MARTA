
import pytest
from typing import Any

class Position:
    def __init__(self, line_no: int, column_no: int, char_index: int):
        self.line_no = line_no
        self.column_no = column_no
        self.char_index = char_index

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Position):
            return False
        return (
            self.line_no == other.line_no
            and self.column_no == other.column_no
            and self.char_index == other.char_index
        )

# Test cases
def test_valid_inputs():
    pos1 = Position(line_no=1, column_no=5, char_index=20)
    pos2 = Position(line_no=1, column_no=5, char_index=20)
    pos3 = Position(line_no=2, column_no=1, char_index=30)
    assert pos1 == pos2
    assert not (pos1 == pos3)

def test_none_case():
    pos1 = Position(line_no=1, column_no=5, char_index=20)
    pos_none = None
    assert not (pos1 == pos_none)

def test_invalid_inputs():
    pos1 = Position(line_no=1, column_no=5, char_index=20)
    pos_str = 'not a Position'
    assert not (pos1 == pos_str)
