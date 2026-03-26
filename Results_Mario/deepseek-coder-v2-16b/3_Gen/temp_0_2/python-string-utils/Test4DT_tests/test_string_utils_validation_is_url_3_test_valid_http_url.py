
import re
from typing import Optional, List, Any

# Assuming URL_RE is defined somewhere in string_utils.validation module
URL_RE = re.compile(r'^https?://[^\s/$.?#].[^\s]*$', re.IGNORECASE)

def is_full_string(input_string: str) -> bool:
    return isinstance(input_string, str) and len(input_string) > 0

def is_url(input_string: Any, allowed_schemes: Optional[List[str]] = None) -> bool:
    """
    Check if a string is a valid url.

    *Examples:*

    >>> is_url('http://www.mysite.com') # returns true
    >>> is_url('https://mysite.com') # returns true
    >>> is_url('.mysite.com') # returns false

    :param input_string: String to check.
    :type input_string: str
    :param allowed_schemes: List of valid schemes ('http', 'https', 'ftp'...). Default to None (any scheme is valid).
    :type allowed_schemes: Optional[List[str]]
    :return: True if url, false otherwise
    """
    if not is_full_string(input_string):
        return False

    valid = URL_RE.match(input_string) is not None

    if allowed_schemes:
        return valid and any([input_string.startswith(s) for s in allowed_schemes])

    return valid

import pytest
from string_utils.validation import is_url

@pytest.mark.parametrize("input_string, expected", [
    ('http://www.mysite.com', True),
    ('https://mysite.com', True),
    ('.mysite.com', False),
    ('ftp://example.com', True),  # Assuming ftp is allowed scheme
])
def test_valid_http_url(input_string, expected):
    assert is_url(input_string) == expected
