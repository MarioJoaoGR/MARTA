# Module: string_utils.manipulation
import re
from string_utils.manipulation import strip_html
import pytest

# Define the regular expressions for testing
HTML_TAG_ONLY_RE = re.compile(r'<[^>]+>')
HTML_RE = re.compile(r'<\w+>.*?<\/\w*>')

def is_string(input_str):
    return isinstance(input_str, str)

class InvalidInputError(Exception):
    pass

# Test cases for strip_html function
@pytest.mark.parametrize("input_string, keep_tag_content, expected", [
    ('test: <a href="foo/bar">click here</a>', False, 'test: '),  # Removing HTML tags without preserving content
    ('test: <a href="foo/bar">click here</a>', True, 'test: click here'),  # Preserving the content of HTML tags
    ('test: <a href="foo/bar">click here</a>', None, 'test: '),  # Default parameter should behave like False
    ('test: <a href="foo/bar">click here</a>', True, 'test: click here'),  # Explicitly setting keep_tag_content=True
    ('plain text', False, 'plain text'),  # Calling with a string that contains no HTML tags
    ('', '', '')  # Calling with an empty string
])
def test_strip_html(input_string, keep_tag_content, expected):
    if keep_tag_content is None:
        assert strip_html(input_string) == expected
    else:
        assert strip_html(input_string, keep_tag_content=keep_tag_content) == expected
