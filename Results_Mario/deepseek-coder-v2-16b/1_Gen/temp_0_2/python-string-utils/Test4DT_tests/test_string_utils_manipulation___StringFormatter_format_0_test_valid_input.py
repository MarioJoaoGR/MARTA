
import pytest
from string_utils.manipulation import __StringFormatter, InvalidInputError

# Mocking the necessary modules and functions if required for the test
URLS_RE = None
EMAILS_RE = None
PRETTIFY_RE = {
    'UPPERCASE_FIRST_LETTER': lambda x: x,
    'DUPLICATES': lambda x: x,
    'RIGHT_SPACE': lambda x: x,
    'LEFT_SPACE': lambda x: x,
    'SPACES_AROUND': lambda x: x,
    'SPACES_INSIDE': lambda x: x,
    'UPPERCASE_AFTER_SIGN': lambda x: x,
    'SAXON_GENITIVE': lambda x: x,
}

def test_valid_input():
    input_string = "Hello, World!"
    formatter = __StringFormatter(input_string)
    
    assert formatter.input_string == input_string
