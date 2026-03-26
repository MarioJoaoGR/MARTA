
import re
from typing import Optional, List, Any

# Assuming URL_RE is defined somewhere in the module string_utils.validation
URL_RE = re.compile(r'^https?://[^\s/$.?#].[^\s]*$', re.IGNORECASE)

def is_url(input_string: Any, allowed_schemes: Optional[List[str]] = None) -> bool:
    """
    Check if a string is a valid URL.

    This function verifies whether the provided `input_string` is a valid URL. It optionally checks against a list of allowed schemes (e.g., 'http', 'https', 'ftp'). If no schemes are specified, it allows any scheme. The function returns `True` if the string matches the criteria for a valid URL and optional scheme check, and `False` otherwise.

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
      >>> is_url('ftp://example.com', allowed_schemes=['ftp'])  # returns True
      ```

    :param input_string: The string to check for validity as a URL.
    :type input_string: str
    :param allowed_schemes: A list of valid schemes (e.g., 'http', 'https', 'ftp'). Default is None, allowing any scheme.
    :type allowed_schemes: Optional[List[str]]
    :return: True if the string is a valid URL with an optional check against allowed schemes, False otherwise.
    """
    if not isinstance(input_string, str):
        return False

    valid = URL_RE.match(input_string) is not None

    if allowed_schemes:
        return valid and any([input_string.startswith(s) for s in allowed_schemes])

    return valid

# Pytest function to test a valid HTTP URL
def test_valid_http_url():
    input_string = 'http://www.mysite.com'
    assert is_url(input_string) == True, "Expected True for a valid HTTP URL"
