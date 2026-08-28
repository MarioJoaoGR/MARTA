
# Module: ansible.module_utils.common.network
import pytest
from ansible.module_utils.common.network import to_subnet

# Test cases for invalid mask inputs
def test_to_subnet_invalid_mask():
    with pytest.raises(ValueError):
        to_subnet("192.168.1.0", "33")  # Invalid mask length (should raise ValueError)
    with pytest.raises(ValueError):
        to_subnet("192.168.1.0", "255.255.255.256")  # Invalid netmask format (should raise ValueError)

# Test cases for edge cases and typical usage scenarios
def test_to_subnet_edge_cases():
    assert to_subnet("0.0.0.0", "0") == '0.0.0.0/0'  # Edge case with all zeros
    assert to_subnet("255.255.255.255", "32") == '255.255.255.255/32'  # Edge case with maximum netmask

# Test cases for the to_subnet function
def test_to_subnet_cidr():
    assert to_subnet("192.168.1.0", "24") == '192.168.1.0/24'
    assert to_subnet("192.168.1.0", "255.255.255.0", dotted_notation=True) == '192.168.1.0 255.255.255.0'
    assert to_subnet("192.168.1.0", "32") == '192.168.1.0/32'

# Test cases for the function logic not covered by existing test cases
def test_to_subnet_functionality():
    # Test with invalid mask length
    with pytest.raises(ValueError):
        to_subnet("192.168.1.0", "33")  # Invalid mask length (should raise ValueError)
    
    # Test with invalid netmask format
    with pytest.raises(ValueError):
        to_subnet("192.168.1.0", "255.255.255.256")  # Invalid netmask format (should raise ValueError)
    
    # Test edge case with all zeros in the IP address and mask length of 0
    assert to_subnet("0.0.0.0", "0") == '0.0.0.0/0'
    
    # Test edge case with maximum netmask for a valid IP address
    assert to_subnet("255.255.255.255", "32") == '255.255.255.255/32'
    
    # Test conversion without dotted notation
    assert to_subnet("192.168.1.0", "24") == '192.168.1.0/24'
    
    # Test conversion with dotted notation
    assert to_subnet("192.168.1.0", "255.255.255.0", dotted_notation=True) == '192.168.1.0 255.255.255.0'
    
    # Test conversion with mask length of 32
    assert to_subnet("192.168.1.0", "32") == '192.168.1.0/32'
