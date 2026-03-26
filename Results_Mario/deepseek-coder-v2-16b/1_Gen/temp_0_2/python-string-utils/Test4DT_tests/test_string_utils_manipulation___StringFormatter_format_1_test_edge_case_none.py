
import pytest
from string_utils.manipulation import __StringFormatter, InvalidInputError

# Mocking URLS_RE and EMAILS_RE for testing purposes
URLS_RE = None
EMAILS_RE = None
PRETTIFY_RE = {
    'UPPERCASE_FIRST_LETTER': lambda x: x.replace('uppercase', ''),
    'DUPLICATES': lambda x: x.replace('duplicates', ''),
    'RIGHT_SPACE': lambda x: x.replace('right space', ''),
    'LEFT_SPACE': lambda x: x.replace('left space', ''),
    'SPACES_AROUND': lambda x: x.replace('spaces around', ''),
    'SPACES_INSIDE': lambda x: x.replace('spaces inside', ''),
    'UPPERCASE_AFTER_SIGN': lambda x: x.replace('uppercase after sign', ''),
    'SAXON_GENITIVE': lambda x: x.replace('saxon genitive', '')
}

def test_edge_case_none():
    input_string = None
    with pytest.raises(InvalidInputError):
        formatter = __StringFormatter(input_string)
