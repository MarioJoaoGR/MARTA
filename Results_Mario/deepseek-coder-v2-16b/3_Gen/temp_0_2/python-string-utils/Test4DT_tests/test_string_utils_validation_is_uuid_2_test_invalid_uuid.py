
import re
from uuid import UUID
import pytest

# Assuming these are defined in string_utils.validation module
UUID_RE = re.compile(r'^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$')
UUID_HEX_OK_RE = re.compile(r'^[0-9a-fA-F]{32}$')

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
        return UUID_HEX_OK_RE.match(s) is not None

    return UUID_RE.match(s) is not None

def test_invalid_uuid():
    input_string = 'not-a-valid-uuid'
    assert not is_uuid(input_string), "Expected False for invalid UUID format"
