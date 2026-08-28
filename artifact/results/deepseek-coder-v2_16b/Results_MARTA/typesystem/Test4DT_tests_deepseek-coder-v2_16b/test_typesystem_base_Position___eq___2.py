
import pytest
from typesystem.base import Position

# Scenario 1: Test standard input with valid schema definitions
def test_valid_inputs():
    pos = Position(line_no=1, column_no=5, char_index=20)
    assert pos == Position(line_no=1, column_no=5, char_index=20)

# Scenario 2: Test comparison with an invalid type to raise TypeError