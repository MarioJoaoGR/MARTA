
from string_utils.manipulation import __StringFormatter, InvalidInputError
import re

# Assuming URLS_RE and EMAILS_RE are predefined regular expressions for URLs and emails respectively
URLS_RE = re.compile(r'https?://[^\s]+')
EMAILS_RE = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')

# Assuming PRETTIFY_RE is a dictionary of regex patterns for various string manipulations
PRETTIFY_RE = {
    'UPPERCASE_FIRST_LETTER': re.compile(r'^[a-z]'),
    'DUPLICATES': re.compile(r'(.)\1+'),
    'RIGHT_SPACE': re.compile(r' [^ ]+$'),
    'LEFT_SPACE': re.compile(r'^[^ ]* '),
    'SPACES_AROUND': re.compile(r'(\S) (\S)'),
    'SPACES_INSIDE': re.compile(r'(.) (.)'),
    'UPPERCASE_AFTER_SIGN': re.compile(r' ([.,;:!?])'),
    'SAXON_GENITIVE': re.compile(r'\b(\w+)\'',)
}

def test_valid_input():
    formatter = __StringFormatter("This is a test string with an email example@example.com.")
    formatted_string = formatter.format()
    
    # Add assertions to validate the output if necessary
    assert isinstance(formatted_string, str), "The formatted string should be a string"
    assert len(formatted_string) > 0, "The formatted string should not be empty"
