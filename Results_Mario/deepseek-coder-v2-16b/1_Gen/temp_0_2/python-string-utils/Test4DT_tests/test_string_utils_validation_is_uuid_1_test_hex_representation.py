
import re
from uuid import UUID
import pytest

# Assuming UUID_RE and UUID_HEX_OK_RE are defined in a module named string_utils.validation
# from string_utils.validation import UUID_RE, UUID_HEX_OK_RE

UUID_RE = re.compile(r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$', re.IGNORECASE)
UUID_HEX_OK_RE = re.compile(r'^[0-9a-f]{32}$', re.IGNORECASE)

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
    # string casting is used to allow UUID itself as input data type
    s = str(input_string)

    if allow_hex:
        return UUID_HEX_OK_RE.match(s) is not None

    return UUID_RE.match(s) is not None

@pytest.mark.parametrize("uuid_str, allow_hex, expected", [
    ('6f8aa2f9-686c-4ac3-8766-5712354a04cf', False, True),
    ('6f8aa2f9686c4ac387665712354a04cf', False, False),
    ('6f8aa2f9686c4ac387665712354a04cf', True, True),
    (str(UUID('6f8aa2f9-686c-4ac3-8766-5712354a04cf')), False, True),
    ('not a uuid string', False, False),
])
def test_uuid_representation(uuid_str, allow_hex, expected):
    assert is_uuid(uuid_str, allow_hex) == expected
