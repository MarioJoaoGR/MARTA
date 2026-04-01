
import re
import pytest
from string_utils.validation import is_ip_v6

def test_valid_ipv6():
    input_string = '2001:db8:85a3:0000:0000:8a2e:370:7334'
    assert is_ip_v6(input_string) == True, f"Expected {input_string} to be a valid IPv6 address"
