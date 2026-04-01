
import pytest
from unittest.mock import patch, MagicMock
from string_utils.manipulation import __StringFormatter, InvalidInputError
import re

# Define the regex patterns for testing (assuming these are defined elsewhere)
URLS_RE = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
EMAILS_RE = re.compile(r'(?:[a-z0-9!#$%&’*+/=?^_{|}~-]+(?:\.[a-z0-9!#$%&’*+/=?^_{|}~-]+)*)@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z]{2,})')
PRETTIFY_RE = {
    'UPPERCASE_FIRST_LETTER': re.compile(r'(^|[^a-zA-Z])([a-z])', re.IGNORECASE),
    'DUPLICATES': re.compile(r'([aeiou])\1'),
    'RIGHT_SPACE': re.compile(r' ([.,:;!?])'),
    'LEFT_SPACE': re.compile(r'([.,:;!?]) '),
    'SPACES_AROUND': re.compile(r'( )'),
    'SPACES_INSIDE': re.compile(r'([a-zA-Z])([a-zA-Z])'),
    'UPPERCASE_AFTER_SIGN': re.compile(r'(?<=[,.])([a-z])', re.IGNORECASE),
    'SAXON_GENITIVE': re.compile(r'([a-zA-Z]+)’s')
}

@pytest.fixture
def string_formatter():
    return __StringFormatter("initial input")

@patch('string_utils.manipulation.__StringFormatter._StringFormatter__placeholder_key', MagicMock(return_value='PLACEHOLDER'))
def test_invalid_input(string_formatter):
    with pytest.raises(InvalidInputError):
        string_formatter = __StringFormatter(12345)  # Invalid input type
