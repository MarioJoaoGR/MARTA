
import pytest
from string_utils.manipulation import strip_html
from string_utils.errors import InvalidInputError

# Test removing HTML tags without preserving content
def test_strip_html_no_preserve():
    assert strip_html('test: <a href="foo/bar">click here</a>') == 'test: '

# Test preserving the content of HTML tags
def test_strip_html_preserve():
    assert strip_html('test: <a href="foo/bar">click here</a>', keep_tag_content=True) == 'test: click here'

# Test with invalid input that should raise InvalidInputError