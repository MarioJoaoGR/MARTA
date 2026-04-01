
import re
from typing import Any

# Assuming IP_V6_RE is a predefined regular expression for IPv6 validation
IP_V6_RE = re.compile(r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$')

def is_full_string(input_string: str) -> bool:
    return bool(input_string and input_string.strip())

def is_ip_v6(input_string: Any) -> bool:
    """
    Checks if a string is a valid ip v6.

    *Examples:*

    >>> is_ip_v6('2001:db8:85a3:0000:0000:8a2e:370:7334') # returns true
    >>> is_ip_v6('2001:db8:85a3:0000:0000:8a2e:370:?') # returns false (invalid "?")

    :param input_string: String to check.
    :type input_string: str
    :return: True if a v6 ip, false otherwise.
    """
    return is_full_string(input_string) and IP_V6_RE.match(input_string) is not None

def test_empty_string():
    input_string = ''
    assert is_ip_v6(input_string) == False, f"Expected False for empty string but got True"
