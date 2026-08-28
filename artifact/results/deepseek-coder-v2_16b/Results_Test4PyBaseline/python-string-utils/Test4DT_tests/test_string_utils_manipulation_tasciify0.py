# Module: string_utils.manipulation
import pytest
from string_utils import manipulation as sm
import unicodedata

# Helper function to check if the input is a string
def is_string(input_value):
    return isinstance(input_value, str)

# Test cases for asciify function
def test_asciify_with_non_ascii_chars():
    result = sm.asciify('èéùúòóäåëýñÅÀÁÇÌÍÑÓË')
    assert result == 'eeuuooaaeynAAACIINOE'

def test_asciify_with_ascii_chars():
    result = sm.asciify('hello world')
    assert result == 'hello world'

def test_asciify_invalid_input():
    with pytest.raises(sm.InvalidInputError):
        sm.asciify(12345)

# Additional edge cases can be added to ensure robustness of the function
