
import pytest
from typesystem.tokenize.tokens import Token

def test_valid_initialization():
    token = Token(value="example", start_index=0, end_index=5)
    assert isinstance(token, Token), "Token instance should be of type Token"
    assert token._value == "example", "Value should match the provided value"
    assert token._start_index == 0, "Start index should match the provided start index"
    assert token._end_index == 5, "End index should match the provided end index"
    assert token._content == "", "Content should be an empty string by default"

def test_initialization_with_content():
    token = Token(value=123, start_index=10, end_index=15, content="context")
    assert isinstance(token, Token), "Token instance should be of type Token"
    assert token._value == 123, "Value should match the provided value"
    assert token._start_index == 10, "Start index should match the provided start index"
    assert token._end_index == 15, "End index should match the provided end index"
    assert token._content == "context", "Content should match the provided content"

def test_invalid_initialization():
    with pytest.raises(TypeError):
        Token()
