
import re
from typing import Any

# Assuming SHALLOW_IP_V4_RE is defined somewhere in string_utils.validation module
SHALLOW_IP_V4_RE = re.compile(r'^(\d{1,3}\.){3}\d{1,3}$')

def is_full_string(input_string: Any) -> bool:
    return bool(input_string and input_string.strip())

def is_ip_v4(input_string: Any) -> bool:
    """
    Checks if a string is a valid ip v4.

    *Examples:*

    >>> is_ip_v4('255.200.100.75') # returns true
    >>> is_ip_v4('nope') # returns false (not an ip)
    >>> is_ip_v4('255.200.100.999') # returns false (999 is out of range)

    :param input_string: String to check.
    :type input_string: str
    :return: True if an ip v4, false otherwise.
    """
    if not is_full_string(input_string) or SHALLOW_IP_V4_RE.match(input_string) is None:
        return False

    # checks that each entry in the ip is in the valid range (0 to 255)
    for token in input_string.split('.'):
        if not (0 <= int(token) <= 255):
            return False

    return True

import pytest
from string_utils.validation import SHALLOW_IP_V4_RE, is_full_string, is_ip_v4

@pytest.mark.parametrize("input_string, expected", [
    ('255.200.100.75', True),
    ('nope', False),
    ('255.200.100.999', False),
])
def test_out_of_range(input_string, expected):
    assert is_ip_v4(input_string) == expected
