
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