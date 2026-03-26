
import re
from uuid import UUID
import pytest

# Assuming these are defined in a separate file or module
UUID_RE = re.compile(r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$', re.IGNORECASE)
UUID_HEX_RE = re.compile(r'^[0-9a-f]{32}$', re.IGNORECASE)

def is_uuid(input_string: str, allow_hex: bool = False) -> bool:
    """
    Check if a string is a valid UUID.

    *Example:*

    >>> is_uuid('6f8aa2f9-686c-4ac3-8766-5712354a04cf') # returns true
    >>> is_uuid('6f8aa2f9686c4ac387665712354a04cf') # returns false
    >>> is_uuid('6f8aa2f9686c4ac387665712354a04cf', allow_hex=True) # returns true

    :param input_string: String to check.
    :type input_string: str
    :param allow_hex: True to allow UUID hex representation as valid, false otherwise (default)
    :type allow_hex: bool
    :return: True if UUID, false otherwise
    """
    s = str(input_string)

    if allow_hex:
        return UUID_HEX_RE.match(s) is not None

    return UUID_RE.match(s) is not None

@pytest.mark.parametrize("uuid_str", [
    "invalid-uuid",  # Invalid format with hyphens
    "6f8aa2f9-686c-4ac3-8766-5712354a04cf-extra",  # Extra characters after valid UUID
    "",  # Empty string
    None,  # None value
    " ",  # Whitespace only
    12345,  # Integer
])
def test_invalid_uuid(uuid_str):
    assert not is_uuid(uuid_str)
