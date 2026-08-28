
import pytest
from string_utils.validation import is_ip_v4

def is_full_string(input_string: str) -> bool:
    return isinstance(input_string, str) and len(input_string.strip()) > 0

# Test for valid IPv4 address
def test_valid_ipv4():
    assert is_ip_v4('255.200.100.75') == True

# Test for invalid inputs that are not IP addresses
def test_invalid_inputs():
    assert is_ip_v4('nope') == False
    assert is_ip_v4('255.200.100.999') == False

# Test edge cases with empty string, whitespace-only string, and None type
def test_edge_cases():
    assert is_ip_v4('') == False
    assert is_ip_v4(' ') == False
    assert is_ip_v4(None) == False
