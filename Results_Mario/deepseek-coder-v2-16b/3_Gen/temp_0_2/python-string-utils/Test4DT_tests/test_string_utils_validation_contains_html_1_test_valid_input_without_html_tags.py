
import re
from string_utils.validation import contains_html, InvalidInputError
import pytest

# Mocking the necessary module or function if needed
HTML_RE = re.compile(r'<.*?>')

def test_valid_input_without_html_tags():
    # Test a string without HTML tags
    input_string = "my string is not bold"
    assert not contains_html(input_string)

    # Optionally, you can add more tests to cover different scenarios
    # For example:
    # test with an empty string
    # test with a string containing HTML tags
