
import pytest
from string_utils.manipulation import __StringFormatter
from string_utils.errors import InvalidInputError
from re import findall

# Assuming URLS_RE and EMAILS_RE are predefined regular expressions for URLs and emails respectively
URLS_RE = findall  # Placeholder for the actual implementation of URLS_RE
EMAILS_RE = findall  # Placeholder for the actual implementation of EMAILS_RE
PRETTIFY_RE = {
    'UPPERCASE_FIRST_LETTER': lambda x: x,
    'DUPLICATES': lambda x: x,
    'RIGHT_SPACE': lambda x: x,
    'LEFT_SPACE': lambda x: x,
    'SPACES_AROUND': lambda x: x,
    'SPACES_INSIDE': lambda x: x,
    'UPPERCASE_AFTER_SIGN': lambda x: x,
    'SAXON_GENITIVE': lambda x: x,
}  # Placeholder for the actual implementation of PRETTIFY_RE

# Test cases for __StringFormatter class
def test_valid_string():
    formatter = __StringFormatter("valid string")
    assert formatter.format() == "Valid string"  # Assuming default transformations result in this output

def test_invalid_input_type():
    with pytest.raises(InvalidInputError):
        __StringFormatter(12345)

def test_string_with_urls_and_emails():
    formatter = __StringFormatter("This is a test string with an email example@example.com and a URL https://www.example.com.")