
import pytest
from typesystem.tokenize.tokens import Token

# Test Case 1: Basic Usage
def test_basic_usage():
    token = Token(value="example", start_index=0, end_index=7)
    assert token._value == "example"
    assert token._start_index == 0
    assert token._end_index == 7
    assert token._content == ""

# Test Case 2: Usage with Content
def test_usage_with_content():
    token_with_content = Token(value="example", start_index=0, end_index=7, content="full text")
    assert token_with_content._content == "full text"

# Test Case 3: Accessing Attributes
def test_accessing_attributes():
    token = Token(value="example", start_index=0, end_index=7)