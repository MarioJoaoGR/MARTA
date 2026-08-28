
# Module: string_utils.validation
import re
from typing import Any

def is_ip_v4(input_string: str) -> bool:
    pattern = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    return bool(re.match(pattern, input_string))

def is_ip_v6(input_string: str) -> bool:
    pattern = r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$'
    return bool(re.match(pattern, input_string))

def is_ip(input_string: Any) -> bool:
    """
    Checks if a string is a valid ip (either v4 or v6).

    *Examples:*

    >>> is_ip('255.200.100.75') # returns true
    >>> is_ip('2001:db8:85a3:0000:0000:8a2e:370:7334') # returns true
    >>> is_ip('1.2.3') # returns false

    :param input_string: String to check.
    :type input_string: str
    :return: True if an ip, false otherwise.
    """
    if not isinstance(input_string, str):
        raise TypeError("is_ip() requires a string argument")
    return is_ip_v6(input_string) or is_ip_v4(input_string)

# Test cases for the function `is_ip`
def test_valid_ipv4():
    assert is_ip('255.200.100.75') == True, "Expected True for a valid IPv4 address"

def test_valid_ipv6():
    assert is_ip('2001:db8:85a3:0000:0000:8a2e:370:7334') == True, "Expected True for a valid IPv6 address"

def test_invalid_ip():
    assert is_ip('1.2.3') == False, "Expected False for an invalid IP address"

def test_non_string_input():
    # This should raise a TypeError since the function expects a string input
    try:
        is_ip(12345)
    except TypeError as e:
        assert str(e) == "is_ip() requires a string argument", f"Expected TypeError, got {str(e)}"
