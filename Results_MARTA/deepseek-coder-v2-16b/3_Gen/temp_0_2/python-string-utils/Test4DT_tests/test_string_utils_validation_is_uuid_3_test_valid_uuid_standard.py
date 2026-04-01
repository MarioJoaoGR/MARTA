
import re
from uuid import UUID

# Define regular expressions for UUID validation
UUID_RE = re.compile(r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$')
UUID_HEX_RE = re.compile(r'^[0-9a-f]{32}$')

def is_uuid(input_string: str, allow_hex: bool = False) -> bool:
    """
    Check if a string is a valid UUID.

    This function validates whether the provided input string conforms to the universally unique identifier (UUID) format. By default, it checks for standard UUID formats; however, if `allow_hex` is set to True, it will also accept hex representations of UUIDs.

    *Examples:*

    >>> is_uuid('6f8aa2f9-686c-4ac3-8766-5712354a04cf') # returns true
    >>> is_uuid('6f8aa2f9686c4ac387665712354a04cf') # returns false
    >>> is_uuid('6f8aa2f9686c4ac387665712354a04cf', allow_hex=True) # returns true

    :param input_string: The string to be checked for UUID validity. It must be a string (str).
    :type input_string: str
    :param allow_hex: A boolean flag that, when set to True, allows the function to validate hex representations of UUIDs. If False (default), only standard UUID formats are considered valid.
    :type allow_hex: bool
    :return: Returns True if the input string is a valid UUID according to the specified criteria, otherwise returns False.
    """
    s = str(input_string)

    if allow_hex:
        return UUID_HEX_RE.match(s) is not None

    return UUID_RE.match(s) is not None

# Test function for standard UUID format
def test_valid_uuid_standard():
    input_string = '6f8aa2f9-686c-4ac3-8766-5712354a04cf'
    assert is_uuid(input_string) == True
