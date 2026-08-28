
import pytest
from typesystem.tokenize.tokens import Token

# Test initialization of Token class
def test_token_initialization():
    token = Token(value="example", start_index=0, end_index=7)
    assert token._value == "example"
    assert token._start_index == 0
    assert token._end_index == 7
    assert token._content == ""

# Test initialization of Token with content
def test_token_initialization_with_content():
    token_with_content = Token(value="example", start_index=0, end_index=7, content="full text")
    assert token_with_content._content == "full text"

# Test the __repr__ method of Token class
def test_token_repr():
    token = Token(value="example", start_index=0, end_index=7)
    expected_repr = f"Token({token._value})"