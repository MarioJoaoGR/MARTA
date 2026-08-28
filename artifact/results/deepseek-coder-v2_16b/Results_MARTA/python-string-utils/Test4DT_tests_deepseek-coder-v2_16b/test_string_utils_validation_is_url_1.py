
import re
from typing import Any, Optional, List
import pytest

# Define a regular expression for URL validation
URL_RE = re.compile(
    r'^(?:http|https)://'  # Scheme: http or https
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+'  # Domain
    r'[A-Z]{2,6}\b|'  # Top-level domain
    r'localhost|'  # Localhost
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # IP address
    r'(?:/[^\s]*)?$', re.IGNORECASE)

def is_full_string(input_string: str) -> bool:
    return isinstance(input_string, str) and len(input_string.strip()) > 0

def is_url(input_string: Any, allowed_schemes: Optional[List[str]] = None) -> bool:
    """
    Check if a string is a valid URL.

    This function verifies whether the provided `input_string` is a valid URL by checking its format against a regular expression and optionally ensuring it starts with one of the allowed schemes. The default behavior allows any scheme, but you can specify a list of allowed schemes to restrict validation accordingly.

    *Examples:*

    - Validating a standard HTTP URL:
      ```python
      >>> is_url('http://www.mysite.com')  # returns True
      ```
    - Validating a secure HTTPS URL:
      ```python
      >>> is_url('https://mysite.com')  # returns True
      ```
    - Checking a string that does not represent a valid URL:
      ```python
      >>> is_url('.mysite.com')  # returns False
      ```

    :param input_string: The string to check, which should be a potential URL.
    :type input_string: str
    :param allowed_schemes: A list of strings representing the schemes that are considered valid for the URL (e.g., 'http', 'https'). If not provided or set to `None`, any scheme is accepted.
    :type allowed_schemes: Optional[List[str]]
    :return: True if the input string is a valid URL according to the specified criteria, False otherwise.
    """
    if not isinstance(input_string, str):
        return False

    match = URL_RE.match(input_string) is not None

    if allowed_schemes:
        starts_with_allowed_scheme = any([input_string.startswith(s) for s in allowed_schemes])
        return match and starts_with_allowed_scheme

    return match

# Test cases for the `is_url` function
def test_valid_http_url():
    assert is_url('http://www.mysite.com') == True

def test_valid_https_url():
    assert is_url('https://mysite.com') == True

def test_invalid_url():
    assert is_url('.mysite.com') == False

def test_non_string_input():
    assert is_url(12345) == False

def test_valid_with_allowed_schemes():
    allowed_schemes = ['http', 'https']
    assert is_url('http://www.mysite.com', allowed_schemes) == True
    assert is_url('https://mysite.com', allowed_schemes) == True
    assert is_url('ftp://mysite.com', allowed_schemes) == False
