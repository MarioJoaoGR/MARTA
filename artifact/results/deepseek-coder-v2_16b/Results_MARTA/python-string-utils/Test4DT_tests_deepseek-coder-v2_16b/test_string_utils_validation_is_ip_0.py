
import pytest
from string_utils.validation import is_ip_v4, is_ip_v6

def is_ip(input_string: str) -> bool:
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
    return is_ip_v6(input_string) or is_ip_v4(input_string)

# Test scenarios
def test_valid_ipv4():
    assert is_ip('255.200.100.75') == True

def test_valid_ipv6():
    assert is_ip('2001:db8:85a3:0000:0000:8a2e:370:7334') == True

def test_invalid_ip():
    assert is_ip('1.2.3') == False
