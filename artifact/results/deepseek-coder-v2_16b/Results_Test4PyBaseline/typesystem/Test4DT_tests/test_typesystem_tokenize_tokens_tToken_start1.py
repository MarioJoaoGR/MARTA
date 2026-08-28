
# Module: typesystem.tokenize.tokens
# test_tokens.py
from typesystem.tokenize.tokens import Token, Position
import pytest

@pytest.fixture
def token():
    return Token(value="example", start_index=0, end_index=7)

@pytest.fixture
def token_with_content():
    return Token(value="example", start_index=0, end_index=7, content="full text")

def test_token_creation(token):
    assert token._value == "example"
    assert token._start_index == 0
    assert token._end_index == 7
    assert token._content == ""

def test_token_with_content_creation(token_with_content):
    assert token_with_content._value == "example"
    assert token_with_content._start_index == 0
    assert token_with_content._end_index == 7
    assert token_with_content._content == "full text"

def test_get_position(token):
    position = token._get_position(token._start_index)
    assert isinstance(position, Position)
    assert position.line_no == 1
    assert position.column_no == 1
    assert position.char_index == 0

def test_get_position_with_content(token_with_content):
    position = token_with_content._get_position(token_with_content._start_index)
    assert isinstance(position, Position)
    assert position.line_no == 1
    assert position.column_no == 1
    assert position.char_index == 0

def test_get_position_multiple_lines():
    token = Token(value="example", start_index=7, end_index=14, content="line1\nline2")
    position = token._get_position(token._start_index)
    assert isinstance(position, Position)
    assert position.line_no == 2  # Corrected line number assertion
    assert position.column_no == 2  # Corrected column number assertion
    assert position.char_index == 7
