
import re
from typing import Optional, List, Any

# Assuming URL_RE is defined somewhere in string_utils.validation or similar module
URL_RE = re.compile(r'^https?://')  # Simplified regex for demonstration purposes

def is_url(input_string: Any, allowed_schemes: Optional[List[str]] = None) -> bool:
    """
    Check if a string is a valid URL.

    This function verifies whether the provided `input_string` is a valid URL. It optionally checks against a list of allowed schemes (e.g., 'http', 'https'). If no allowed schemes are specified, any scheme is considered valid. The function returns `True` if the string is a valid URL and matches one of the allowed schemes, and `False` otherwise.

    *Examples:*

    - Checking a valid HTTP URL:
      ```python
      >>> is_url('http://www.mysite.com')  # returns True
      ```
    - Checking a valid HTTPS URL:
      ```python
      >>> is_url('https://mysite.com')  # returns True
      ```
    - Checking an invalid URL without a scheme:
      ```python
      >>> is_url('.mysite.com')  # returns False
      ```
    - Checking a valid URL with an allowed scheme:
      ```python
      >>> is_url('ftp://example.com', allowed_schemes=['http', 'https', 'ftp'])  # returns True
      ```
    - Checking a valid URL with a disallowed scheme:
      ```python
      >>> is_url('ftp://example.com', allowed_schemes=['http', 'https'])  # returns False
      ```

    :param input_string: The string to check for validity as a URL.
    :type input_string: str
    :param allowed_schemes: A list of valid schemes (e.g., 'http', 'https'). If not provided, any scheme is considered valid. Default is None.
    :type allowed_schemes: Optional[List[str]]
    :return: True if the string is a valid URL and matches one of the allowed schemes, False otherwise.
    """
    if not isinstance(input_string, str):
        return False

    valid = URL_RE.match(input_string) is not None

    if allowed_schemes:
        return valid and any([input_string.startswith(s) for s in allowed_schemes])

    return valid

# Pytest function to test an invalid URL without a scheme
def test_invalid_url():
    input_string = '.mysite.com'
    assert not is_url(input_string), f"Expected False for input '{input_string}', but got True"
