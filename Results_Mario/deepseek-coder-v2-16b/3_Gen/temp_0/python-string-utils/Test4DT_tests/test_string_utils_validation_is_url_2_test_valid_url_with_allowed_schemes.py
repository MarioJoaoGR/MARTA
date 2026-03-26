
import re
from typing import Any, Optional, List

# Assuming URL_RE is a pre-defined regex for matching URLs
URL_RE = re.compile(r'^(http|https|ftp)://[^\s/$.?#].[^\s]*$', re.IGNORECASE)

def is_full_string(input_string: str) -> bool:
    return isinstance(input_string, str) and len(input_string.strip()) > 0

def is_url(input_string: Any, allowed_schemes: Optional[List[str]] = None) -> bool:
    """
    Check if a string is a valid URL.

    This function verifies whether the provided `input_string` is a valid URL. It optionally checks against a list of allowed schemes (e.g., 'http', 'https', 'ftp'). If no allowed schemes are specified, any scheme is considered valid. The function returns `True` if the string is a valid URL and matches the allowed schemes, and `False` otherwise.

    *Examples:*

    - Valid URLs with default settings:
      ```python
      >>> is_url('http://www.mysite.com')  # returns True
      >>> is_url('https://mysite.com')     # returns True
      ```
    - Invalid URL without schemes specified:
      ```python
      >>> is_url('.mysite.com')            # returns False
      ```
    - Valid URLs with allowed schemes:
      ```python
      >>> is_url('ftp://example.com', ['http', 'https', 'ftp'])  # returns True
      ```

    :param input_string: String to check for URL validity.
    :type input_string: str
    :param allowed_schemes: List of valid schemes ('http', 'https', 'ftp'...). Default is None, allowing any scheme.
    :type allowed_schemes: Optional[List[str]]
    :return: True if the string is a valid URL and matches the allowed schemes, False otherwise.
    """
    if not is_full_string(input_string):
        return False

    valid = URL_RE.match(input_string) is not None

    if allowed_schemes:
        return valid and any([input_string.startswith(s) for s in allowed_schemes])

    return valid

# Test function to test the above functionality
def test_valid_url_with_allowed_schemes():
    assert is_url('ftp://example.com', ['http', 'https', 'ftp']) == True
    assert is_url('http://example.com', ['http', 'https', 'ftp']) == True
    assert is_url('https://example.com', ['http', 'https', 'ftp']) == True
    assert is_url('ftp://example.com', ['http', 'https']) == False
    assert is_url('http://example.com', ['https', 'ftp']) == False
