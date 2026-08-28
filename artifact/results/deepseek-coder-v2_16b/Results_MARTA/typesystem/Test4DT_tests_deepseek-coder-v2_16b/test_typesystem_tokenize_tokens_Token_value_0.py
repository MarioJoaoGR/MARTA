
import pytest
from typesystem.tokenize.tokens import Token

# Test Scenario 1: Test standard input with string value
def test_valid_case_1():
    token = Token(value="example", start_index=0, end_index=5)
    assert token._value == "example"
    assert token._start_index == 0
    assert token._end_index == 5
    assert token._content == ""

# Test Scenario 2: Test standard input with integer value and content
def test_valid_case_2():
    token = Token(value=123, start_index=10, end_index=15, content="context")
    assert token._value == 123
    assert token._start_index == 10
    assert token._end_index == 15
    assert token._content == "context"

# Test Scenario 3: Test raising TypeError when value is not provided as an argument
def test_error_case():
    with pytest.raises(TypeError):
        token = Token()
