# Module: string_utils.validation
import pytest
from string_utils.validation import is_ip_v4

# Test cases for valid IPv4 addresses
def test_valid_ipv4():
    assert is_ip_v4('255.200.100.75') == True

# Test cases for invalid IPv4 addresses (not an IP)
def test_invalid_not_an_ip():
    assert is_ip_v4('nope') == False

# Test cases for invalid IPv4 addresses (number out of range)
def test_invalid_number_out_of_range():
    assert is_ip_v4('255.200.100.999') == False

# Test cases for invalid IPv4 addresses (first number out of range)
def test_invalid_first_number_out_of_range():
    assert is_ip_v4('256.200.100.75') == False

# Test cases for invalid IPv4 addresses (not enough numbers)
def test_invalid_not_enough_numbers():
    assert is_ip_v4('255.200.100') == False

if __name__ == "__main__":
    pytest.main()
