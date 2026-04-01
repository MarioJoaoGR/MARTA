
import re
import pytest
from string_utils.validation import is_full_string, EMAIL_RE, ESCAPED_AT_SIGN

def is_email(input_string: str) -> bool:
    """
    Check if a string is a valid email address.

    This function validates an email by following the rules outlined in RFC 3696, which specifies that an email must be a non-empty string with a maximum length of 320 characters and cannot start with a dot. The email should consist of two parts separated by an '@' symbol: a "head" part (before the '@') and a "tail" part (after the '@'). The head part must not exceed 64 characters, contain escaped spaces or start/end with quotes, and must not have multiple consecutive dots.

    *Examples:*

    - Valid email:
      ```python
      >>> is_email('my.email@the-provider.com')  # returns True
      ```

    - Invalid email (starts with a dot):
      ```python
      >>> is_email('.invalid@example.com')  # returns False
      ```

    - Invalid email (contains multiple "@" symbols):
      ```python
      >>> is_email('multiple@@example.com')  # returns False
      ```

    :param input_string: The string to check for validity as an email address.
    :type input_string: str
    :return: True if the input string is a valid email, False otherwise.
    """
    if not is_full_string(input_string) or len(input_string) > 320 or input_string.startswith('.'):
        return False

    try:
        head, tail = input_string.split('@')

        if len(head) > 64 or len(tail) > 255 or head.endswith('.') or ('..' in head):
            return False

        head = head.replace('\\ ', '')
        if head.startswith('"') and head.endswith('"'):
            head = head.replace(' ', '')[1:-1]

        return EMAIL_RE.match(head + '@' + tail) is not None

    except ValueError:
        if ESCAPED_AT_SIGN.search(input_string) is not None:
            return is_email(ESCAPED_AT_SIGN.sub('a', input_string))

        return False

# Test cases for valid email addresses
@pytest.mark.parametrize("test_input, expected", [
    ('my.email@the-provider.com', True),
    ('user@example.com', True),
    ('valid-email@domain.co', True),
    ('user.name@subdomain.domain.com', True),
])
def test_valid_email(test_input, expected):
    assert is_email(test_input) == expected
