
import pytest
from typesystem.tokenize.tokens import Token

def test_valid_initialization():
    token = Token(value="example", start_index=0, end_index=5)
    assert hasattr(token, '_value') and token._value == "example"
    assert hasattr(token, '_start_index') and token._start_index == 0
    assert hasattr(token, '_end_index') and token._end_index == 5
    assert hasattr(token, '_content') and token._content == ""

def test_initialization_with_content():
    token = Token(value="example", start_index=0, end_index=5, content="context")
    assert hasattr(token, '_value') and token._value == "example"
    assert hasattr(token, '_start_index') and token._start_index == 0
    assert hasattr(token, '_end_index') and token._end_index == 5
    assert hasattr(token, '_content') and token._content == "context"

def test_invalid_input():
    with pytest.raises(TypeError):
        Token()
