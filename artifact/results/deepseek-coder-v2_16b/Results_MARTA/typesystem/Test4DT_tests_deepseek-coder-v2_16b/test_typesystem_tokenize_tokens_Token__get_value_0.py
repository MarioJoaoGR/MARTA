
import pytest
from typesystem.tokenize.tokens import Token

# Scenario 1: Test initialization with valid input
def test_valid_initialization():
    token = Token(value="example", start_index=0, end_index=5)
    assert token._value == "example"
    assert token._start_index == 0
    assert token._end_index == 5
    assert token._content == ""

# Scenario 2: Test initialization with content
def test_initialization_with_content():
    token = Token(value=123, start_index=10, end_index=15, content="context")
    assert token._value == 123
    assert token._start_index == 10
    assert token._end_index == 15
    assert token._content == "context"

# Scenario 3: Test invalid input (should raise TypeError)
def test_invalid_input():
    with pytest.raises(TypeError):
        Token()
