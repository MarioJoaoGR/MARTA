
import pytest
from typesystem.tokenize.tokens import Token

# Test creating a Token with default content
def test_create_token_with_default_content():
    token = Token(value="example", start_index=0, end_index=7)
    assert token._value == "example"
    assert token._start_index == 0
    assert token._end_index == 7
    assert token._content == ""

# Test creating a Token with specified content
def test_create_token_with_specified_content():
    token_with_content = Token(value="example", start_index=0, end_index=7, content="full text")