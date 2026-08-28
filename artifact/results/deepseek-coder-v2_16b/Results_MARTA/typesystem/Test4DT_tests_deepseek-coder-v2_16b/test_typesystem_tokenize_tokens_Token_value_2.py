
import pytest
from typesystem.tokenize.tokens import Token

# Scenario 1: Test standard input with valid schema definitions
def test_valid_input():
    token = Token(value="example", start_index=0, end_index=5)
    assert token._value == "example"
    assert token._start_index == 0
    assert token._end_index == 5
    assert token._content == ""

# Scenario 2: Test invalid input to raise TypeError
def test_invalid_input():
    with pytest.raises(TypeError):
        Token()
