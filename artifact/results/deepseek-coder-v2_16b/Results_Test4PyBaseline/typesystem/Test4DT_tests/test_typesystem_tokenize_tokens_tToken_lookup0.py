
# Module: typesystem.tokenize.tokens
# test_tokens.py
from typesystem.tokenize.tokens import Token

def test_init_without_content():
    # Test initializing a Token without content
    token = Token(value="example", start_index=0, end_index=7)
    assert token._value == "example"
    assert token._start_index == 0
    assert token._end_index == 7
    assert token._content == ""

def test_init_with_content():
    # Test initializing a Token with content
    token = Token(value="example", start_index=0, end_index=7, content="full text")
    assert token._value == "example"
    assert token._start_index == 0
    assert token._end_index == 7