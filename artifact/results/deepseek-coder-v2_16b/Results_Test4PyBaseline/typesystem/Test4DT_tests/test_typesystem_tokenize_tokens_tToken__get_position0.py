# Module: typesystem.tokenize.tokens
import pytest
from typesystem.tokenize.tokens import Token, Position

# Test creating a Token with default content
def test_token_creation_with_default_content():
    token = Token(value="example", start_index=0, end_index=7)
    assert token._value == "example"
    assert token._start_index == 0
    assert token._end_index == 7
    assert token._content == ""

# Test creating a Token with specified content
def test_token_creation_with_specified_content():
    token_with_content = Token(value="example", start_index=0, end_index=7, content="full text")
    assert token_with_content._content == "full text"

# Test accessing attributes of a created Token
def test_token_attributes():
    token = Token(value="example", start_index=0, end_index=7)
    assert token._value == "example"
    assert token._start_index == 0
    assert token._end_index == 7
    assert token._content == ""

# Test using the _get_position method
def test_get_position():
    token = Token(value="example", start_index=0, end_index=7, content="full text")
    pos = token._get_position(5)
    assert pos.line_no == 1
    assert pos.column_no == 6
    assert pos.char_index == 5
