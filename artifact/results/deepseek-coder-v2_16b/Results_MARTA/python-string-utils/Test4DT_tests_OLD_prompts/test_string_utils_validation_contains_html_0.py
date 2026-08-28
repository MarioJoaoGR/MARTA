
import pytest
from string_utils.validation import contains_html

# Test for a string containing HTML tags
def test_contains_html_with_tags():
    assert contains_html('my string is <strong>bold</strong>') == True

# Test for a string without any HTML tags
def test_contains_html_without_tags():
    assert contains_html('my string is not bold') == False

# Test for a string containing multiple tags
def test_contains_html_multiple_tags():
    assert contains_html('here are some <span>tags</span>, including <a href="#">links</a>') == True

# Test for an empty string

# Test for a string containing only comments (should return False)