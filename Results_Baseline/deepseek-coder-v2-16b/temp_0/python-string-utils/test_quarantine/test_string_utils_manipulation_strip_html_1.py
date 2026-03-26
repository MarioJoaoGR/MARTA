
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
    ('plain text', False, 'plain text'),  # Calling with a string that contains no HTML tags
    ('', '', '')  # Calling with an empty string
])
def test_strip_html(input_string, keep_tag_content, expected):
    if keep_tag_content is None:
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation_strip_html_1
python-string-utils/Test4DT_tests/test_string_utils_manipulation_strip_html_1.py:24:33: E0001: Parsing failed: 'expected an indented block after 'if' statement on line 24 (Test4DT_tests.test_string_utils_manipulation_strip_html_1, line 24)' (syntax-error)

"""