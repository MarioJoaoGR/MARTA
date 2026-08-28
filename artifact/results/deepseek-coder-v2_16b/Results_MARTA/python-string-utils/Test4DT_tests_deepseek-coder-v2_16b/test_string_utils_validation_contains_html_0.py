
import pytest
from string_utils.validation import contains_html
from string_utils.errors import InvalidInputError

def is_string(obj):
    return isinstance(obj, str)

# Test for empty string input

# Test for a string without HTML/XML tags
def test_no_html_tags():
    assert not contains_html("plain text without tags")

# Test for a string containing HTML/XML tags
def test_contains_html_tags():
    assert contains_html('my string is <strong>bold</strong>')

# Test for a string with multiple HTML/XML tags
def test_multiple_html_tags():
    assert contains_html('here are some <span>tags</span>, including <a href="#">links</a>')