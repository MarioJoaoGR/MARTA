
import pytest
from typesystem.base import Position

# Scenario 1: Test standard input with valid schema definitions
def test_valid_inputs():
    pos = Position(line_no=1, column_no=5, char_index=20)
    assert pos.line_no == 1
    assert pos.column_no == 5
    assert pos.char_index == 20

# Scenario 2: Test invalid input where line_no is not an integer

# Scenario 3: Test invalid input where column_no is not an integer

# Scenario 4: Test invalid input where char_index is not an integer