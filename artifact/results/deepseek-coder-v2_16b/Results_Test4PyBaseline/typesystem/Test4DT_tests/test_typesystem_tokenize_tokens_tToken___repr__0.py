
# Module: typesystem.tokenize.tokens
# test_tokens.py
from typesystem.tokenize.tokens import Token

def test_basic_initialization():
    token = Token(value="example", start_index=0, end_index=7)
    assert token._value == "example"
    assert token._start_index == 0
    assert token._end_index == 7
    assert token._content == ""

def test_initialization_with_content():
    token_with_content = Token(value="example", start_index=0, end_index=7, content="full text")
    assert token_with_content._value == "example"
    assert token_with_content._start_index == 0
    assert token_with_content._end_index == 7
    assert token_with_content._content == "full text"

def test_accessing_attributes():
    token = Token(value="example", start_index=0, end_index=7)
    assert token._value == "example"
    assert token._start_index == 0
    assert token._end_index == 7
    assert token._content == ""

def test_string_representation():
    token = Token(value="example", start_index=0, end_index=7)