
# Module: ansible.module_utils.common.network
import re
from ansible.module_utils.common.network import is_mac

def test_is_mac_valid_hyphen():
    assert is_mac("12-34-56-78-9A-BC") == True

def test_is_mac_valid_colon():
    assert is_mac("12:34:56:78:9A:BC") == True

def test_is_mac_invalid_format():
    assert is_mac("1234.5678.9ABC") == False

def test_is_mac_invalid_character():
    assert is_mac("12-34-56-78-9A-CG") == False

# Additional test cases for uncovered lines 160-161

def test_is_mac_valid_mixed_case():
    # Test with a valid MAC address in mixed case (should be normalized to lowercase)
    assert is_mac("12:34:56:78:9A:BC") == True

def test_is_mac_invalid_length():
    # Test with an invalid length of MAC address (should return False)
    assert is_mac("12-34-56-78-9A") == False

def test_is_mac_valid_all_lowercase():
    # Test with a valid MAC address in all lowercase letters
    assert is_mac("ab:cd:ef:12:34:56") == True

def test_is_mac_invalid_middle_character():
    # Test with an invalid character in the middle of the MAC address (should return False)
    assert is_mac("12-34-56-78-9A-C!") == False
