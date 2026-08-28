
import pytest
from typesystem.base import Message, Position

# Scenario 1: Test standard input with valid schema definitions

# Scenario 2: Test input with missing key and index

# Scenario 3: Test input with conflicting fields
def test_invalid_input_with_conflicting_fields():
    with pytest.raises(TypeError):
        Message(text='Error message', code='custom', key='username', index=['users', 1], start_position=Position(line=1, column=1), end_position=Position(line=1, column=20))