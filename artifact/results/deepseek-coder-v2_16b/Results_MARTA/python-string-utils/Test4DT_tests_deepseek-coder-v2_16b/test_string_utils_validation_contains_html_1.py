
import pytest
from string_utils.validation import contains_html, InvalidInputError

def is_string(obj):
    return isinstance(obj, str)

# Test for valid input string
def test_valid_input():
    assert contains_html('my string is <strong>bold</strong>') == True
    assert contains_html('here are some <span>tags</span>, including <a href="#">links</a>') == True

# Test for invalid input type (None)
def test_invalid_input_none():
    with pytest.raises(InvalidInputError):
        contains_html(None)

# Test for valid input string without HTML/XML tags
def test_valid_no_tags():
    assert contains_html('my string is not bold') == False
    assert contains_html('plain text without tags') == False
