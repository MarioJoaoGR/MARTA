
import re
import pytest
from string_utils.validation import is_ip_v4, is_ip_v6

def is_ip(input_string: str) -> bool:
    """
    Checks if a string is a valid IP address (either IPv4 or IPv6).

    This function determines whether the provided `input_string` represents a valid IPv4 or IPv6 address by checking both formats. It returns `True` if the string is a valid IP address of either version, and `False` otherwise.

    *Examples:*

    - Valid IPv4 address:
      ```python
      >>> is_ip('255.200.100.75')  # returns True
      ```
    - Valid IPv6 address:
      ```python
      >>> is_ip('2001:db8:85a3:0000:0000:8a2e:370:7334')  # returns True
      ```
    - Invalid IP address:
      ```python
      >>> is_ip('1.2.3')  # returns False
      ```

    :param input_string: The string to check for validity as an IP address.
    :type input_string: str
    :return: True if the string is a valid IP address, false otherwise.
    """
    return is_ip_v6(input_string) or is_ip_v4(input_string)

def test_valid_ipv6():
    assert is_ip('2001:db8:85a3:0000:0000:8a2e:370:7334') == True
