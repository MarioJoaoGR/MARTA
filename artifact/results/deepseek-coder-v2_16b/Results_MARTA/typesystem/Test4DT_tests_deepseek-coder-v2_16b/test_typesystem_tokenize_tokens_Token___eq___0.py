
import pytest
from typesystem.tokenize.tokens import Token

# Test cases for valid scenarios
def test_valid_case_1():
    token = Token(value='example', start_index=0, end_index=5)
    assert token._value == 'example'
    assert token._start_index == 0
    assert token._end_index == 5
    assert token._content == ""

def test_valid_case_2():
    token = Token(value=123, start_index=10, end_index=15, content='context')
    assert token._value == 123
    assert token._start_index == 10
    assert token._end_index == 15
    assert token._content == 'context'

# Test case for invalid scenario
def test_invalid_case_1():
    token = Token(value='example', start_index=0, end_index=5)
    with pytest.raises(AssertionError):
        assert token._start_index == 1
