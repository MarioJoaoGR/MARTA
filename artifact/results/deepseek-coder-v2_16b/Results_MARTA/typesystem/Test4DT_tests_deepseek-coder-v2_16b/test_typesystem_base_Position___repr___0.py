
import pytest
from typesystem.base import Position

# Scenario 1: Test standard input with valid schema definitions
def test_valid_inputs():
    pos = Position(1, 5, 20)
    assert pos.line_no == 1
    assert pos.column_no == 5
    assert pos.char_index == 20

# Scenario 2: Test invalid input to ensure TypeError is raised
def test_invalid_input():
    with pytest.raises(TypeError):
        Position()

# Scenario 3: Test the string representation of a valid position instance
def test_position_repr():
    pos = Position(1, 5, 20)
    assert repr(pos) == "Position(line_no=1, column_no=5, char_index=20)"
