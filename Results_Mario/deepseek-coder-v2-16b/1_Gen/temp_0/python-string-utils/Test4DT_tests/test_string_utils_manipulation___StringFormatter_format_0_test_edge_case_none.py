
import pytest
from string_utils.manipulation import __StringFormatter
from re import compile

# Mocking necessary regex patterns
URLS_RE = compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
EMAILS_RE = compile(r'(?:[a-z0-9!#$%&’*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&’*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9]{2,}|(?:\[?(\d{1,3}\.){3}\d{1,3}\]?))')
PRETTIFY_RE = {
    'UPPERCASE_FIRST_LETTER': compile(r'(^|[^a-zA-Z])([a-z])'),
    'DUPLICATES': compile(r'(\b\w+\b)(\s+\1\b)'),
    'RIGHT_SPACE': compile(r'([a-zA-Z0-9])\s+'),
    'LEFT_SPACE': compile(r'\s+([a-zA-Z0-9])'),
    'SPACES_AROUND': compile(r'(\S)\s+(\S)'),
    'SPACES_INSIDE': compile(r'([a-zA-Z0-9])([a-zA-Z0-9])'),
    'UPPERCASE_AFTER_SIGN': compile(r'(?<=[,;:])([a-z])'),
    'SAXON_GENITIVE': compile(r'(\w+)\'s')
}

@pytest.fixture
def string_formatter():
    return __StringFormatter("Initial String")

def test_format_edge_case_none(string_formatter):
    assert string_formatter.format() == "Initial String"
