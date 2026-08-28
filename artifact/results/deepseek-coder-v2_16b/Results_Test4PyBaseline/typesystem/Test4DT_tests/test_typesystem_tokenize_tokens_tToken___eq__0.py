
import pytest
from typesystem.tokenize.tokens import Token

# Test creating a token with default content
def test_create_token_with_default_content():
    token = Token(value="example_value", start_index=0, end_index=10)
    assert token._value == "example_value"
    assert token._start_index == 0
    assert token._end_index == 10
    assert token._content == ""

# Test creating a token with specified content
def test_create_token_with_specified_content():
    token_with_content = Token(value="example", start_index=0, end_index=7, content="full text")
    assert token_with_content._content == "full text"

# Test accessing the value of a token (should raise NotImplementedError)
def test_access_token_value():
    token = Token(value="example", start_index=0, end_index=7)
    with pytest.raises(NotImplementedError):
        token._get_value()

# Test getting the string representation of a token (should return the value substring)
def test_get_string_representation():
    token = Token(value="example", start_index=0, end_index=7)