
import re
from uuid import UUID

# Assuming these are defined in string_utils.validation module
UUID_RE = re.compile(r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$', re.IGNORECASE)
UUID_HEX_RE = re.compile(r'^[0-9a-f]{32}$', re.IGNORECASE)

def is_uuid(input_string: str, allow_hex: bool = False) -> bool:
    """
    Check if a string is a valid UUID.

    This function validates whether the provided input string conforms to the universally unique identifier (UUID) format. It supports both standard UUID formats and allows for hexadecimal representation when specified.

    *Examples:*

    >>> is_uuid('6f8aa2f9-686c-4ac3-8766-5712354a04cf') # returns True
    >>> is_uuid('6f8aa2f9686c4ac387665712354a04cf') # returns False
    >>> is_uuid('6f8aa2f9686c4ac387665712354a04cf', allow_hex=True) # returns True

    :param input_string: The string to be checked for UUID validity. It must be a string (str).
    :param allow_hex: A boolean flag that, when set to True, allows the function to validate strings that represent a hexadecimal UUID. Default is False.
    :return: Returns True if the input string is a valid UUID according to the specified conditions, otherwise returns False.
    """
    s = str(input_string)

    if allow_hex:
        return UUID_HEX_RE.match(s) is not None

    return UUID_RE.match(s) is not None

import pytest

@pytest.mark.parametrize("uuid_str, allow_hex, expected", [
    ('6f8aa2f9-686c-4ac3-8766-5712354a04cf', False, True),
    ('6f8aa2f9686c4ac387665712354a04cf', False, False),
    ('6f8aa2f9686c4ac387665712354a04cf', True, True),
])
def test_valid_uuid(uuid_str, allow_hex, expected):
    assert is_uuid(uuid_str, allow_hex) == expected
