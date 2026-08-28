
# Module: ansible.module_utils.common.network
import pytest
from struct import pack
from socket import inet_ntoa
from ansible.module_utils.common.network import to_netmask, is_masklen

# Helper function for testing mask length validation
def test_is_masklen():
    assert is_masklen("0") == True
    assert is_masklen("32") == True
    assert is_masklen("-1") == False
    assert is_masklen("33") == False
    assert is_masklen("abc") == False

# Test cases for to_netmask function
def test_to_netmask():
    # Valid mask lengths should return the correct netmask
    assert to_netmask("24") == '255.255.255.0'
    assert to_netmask("32") == '255.255.255.255'
    assert to_netmask("16") == '255.255.0.0'
    
    # Invalid mask lengths should raise a ValueError
    with pytest.raises(ValueError):
        to_netmask("33")  # Mask length out of range
    with pytest.raises(ValueError):
        to_netmask("-1")  # Negative mask length
    with pytest.raises(ValueError):
        to_netmask("abc")  # Non-integer string

# Additional test cases for uncovered lines in to_netmask function
def test_to_netmask_uncovered():
    # Test invalid masklen input that should raise ValueError
    with pytest.raises(ValueError):
        to_netmask("33")  # Mask length out of range
    with pytest.raises(ValueError):
        to_netmask("-1")  # Negative mask length
    with pytest.raises(ValueError):
        to_netmask("abc")  # Non-integer string
    
    # Test valid masklen input that should not raise ValueError
    assert to_netmask("24") == '255.255.255.0'
    assert to_netmask("32") == '255.255.255.255'
    assert to_netmask("16") == '255.255.0.0'
    
    # Test the implementation of bits construction and IP address formatting
    val = 24
    bits = 0
    for i in range(32 - int(val), 32):
        bits |= (1 << i)
    expected_netmask = inet_ntoa(pack('>I', bits))
    assert to_netmask(str(val)) == expected_netmask
    
    val = 32
    bits = 0
    for i in range(32 - int(val), 32):
        bits |= (1 << i)
    expected_netmask = inet_ntoa(pack('>I', bits))
    assert to_netmask(str(val)) == expected_netmask
    
    val = 16
    bits = 0
    for i in range(32 - int(val), 32):
        bits |= (1 << i)
    expected_netmask = inet_ntoa(pack('>I', bits))
    assert to_netmask(str(val)) == expected_netmask

# Run the tests
if __name__ == "__main__":
    pytest.main()
