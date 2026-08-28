
import pytest
from typesystem.base import Message

# Scenario 1: Test standard input with valid schema definitions

# Scenario 2: Test edge cases with None values

# Scenario 3: Test handling of conflicting parameters
def test_conflicting_parameters():
    with pytest.raises(AssertionError):
        Message(text='Conflicting', code='custom', key='username', index=[], start_position=None, end_position=None)

    with pytest.raises(AssertionError):
        Message(text='Conflicting', code='custom', key='username', index=[], position=None)