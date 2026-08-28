
import pytest
from typesystem.tokenize.tokens import Token

# Scenario 1: Test initialization of a token with value, start index, and end index
def test_token_initialization():
    token = Token(value="print", start_index=0, end_index=5)
    assert token._value == "print"
    assert token._start_index == 0
    assert token._end_index == 5
    assert token._content == ""

# Scenario 2: Test initialization of a token with value, start index, end index, and content
def test_token_initialization_with_content():
    token = Token(value="example", start_index=10, end_index=15, content="context")
    assert token._value == "example"
    assert token._start_index == 10
    assert token._end_index == 15
    assert token._content == "context"

# Scenario 3: Test initialization of a token with different types of values
def test_token_initialization_with_different_values():
    token = Token(value=42, start_index=20, end_index=25)
    assert token._value == 42
    assert token._start_index == 20
    assert token._end_index == 25
    assert token._content == ""

# Scenario 4: Test initialization of a token without additional content
def test_token_initialization_without_content():
    token = Token(value="value", start_index=30, end_index=35)
    assert token._value == "value"
    assert token._start_index == 30
    assert token._end_index == 35
    assert token._content == ""
