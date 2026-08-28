
import pytest
from typesystem.base import Message

# Scenario 1: Test standard input with valid schema definitions

# Scenario 2: Test creation of a message with a specific code
def test_message_with_specific_code():
    msg = Message(text="Invalid format.", code="invalid")
    assert msg.text == "Invalid format."
    assert msg.code == "invalid"

# Scenario 3: Test creation of a message with an index

# Scenario 4: Test creation of a message with start and end positions