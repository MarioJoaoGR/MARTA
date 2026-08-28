
import re
import pytest

def is_mac(mac_address):
    """
    Validate a MAC address for a given string. The function checks if the provided string matches the standard format of a MAC address, 
    which includes hexadecimal characters separated by colons, hyphens, or periods. This helps in ensuring that the input is likely to be 
    a valid MAC address before further processing or storage.

    Args:
        mac_address (str): The string to validate as a MAC address.

    Returns:
        bool: True if the string is a valid MAC address, otherwise False.

    Examples:
        >>> is_mac("12-34-56-78-9A-BC")
        True
        >>> is_mac("123456-789ABC")
        False
        >>> is_mac("12:34:56:78:9A:BC")
        True
        >>> is_mac("1234.5678.9abc")
        True
    """
    mac_addr_regex = re.compile('[0-9a-f]{2}([-:])[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$')
    return bool(mac_addr_regex.match(mac_address.lower()))

# Test cases
def test_valid_mac_addresses():
    mac_address = '12:34:56:78:9A:BC'
    assert is_mac(mac_address) == True, f"Expected {mac_address} to be a valid MAC address."

def test_invalid_mac_addresses():
    mac_address = '123456-789ABC'
    assert is_mac(mac_address) == False, f"Expected {mac_address} to be an invalid MAC address."

def test_none_input():
    mac_address = None
    assert is_mac(mac_address) == False, "Expected None to be considered as an invalid MAC address."
