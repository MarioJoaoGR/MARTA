
import pytest
from string_utils.validation import is_ip_v6

# Test for valid IPv6 address
def test_valid_ipv6():
    input_string = '2001:db8:85a3:0000:0000:8a2e:370:7334'
    assert is_ip_v6(input_string) == True

# Test for invalid IPv6 address due to an invalid character
def test_invalid_ipv6():
    input_string = '2001:db8:85a3:0000:0000:8a2e:370:?'
    assert is_ip_v6(input_string) == False

# Test for empty string after stripping whitespace
def test_empty_ipv6():
    input_string = ' '
    assert is_ip_v6(input_string) == False
