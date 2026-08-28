# Module: string_utils.validation
import pytest
from string_utils.validation import is_ip_v4

# Test cases for valid IPv4 addresses
def test_valid_ipv4():
    assert is_ip_v4('255.200.100.75') == True

# Test cases for invalid inputs that are not IP addresses
def test_invalid_not_ip():
    assert is_ip_v4('nope') == False

# Test cases for invalid IPv4 addresses due to out-of-range segments
def test_invalid_out_of_range():
    assert is_ip_v4('255.200.100.999') == False

# Additional test case for empty string
def test_empty_string():
    assert is_ip_v4('') == False

# Additional test case for string with only spaces
def test_string_with_spaces():
    assert is_ip_v4('     ') == False

# Additional test case for valid but non-IP strings
def test_valid_but_non_ip_string():
    assert is_ip_v4('this is not an ip') == False

if __name__ == "__main__":
    pytest.main()
