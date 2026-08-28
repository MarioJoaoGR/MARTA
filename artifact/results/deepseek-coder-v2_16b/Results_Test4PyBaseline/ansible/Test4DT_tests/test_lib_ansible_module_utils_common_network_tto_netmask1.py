
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

# Additional test cases for uncovered lines (41-42, 44-46, 48)
def test_to_netmask_uncovered():
    # Test case for invalid mask length that raises ValueError
    with pytest.raises(ValueError):
        to_netmask("33")  # Mask length out of range
    
    # Test case for negative mask length that raises ValueError
    with pytest.raises(ValueError):
        to_netmask("-1")  # Negative mask length
    
    # Test case for non-integer string that raises ValueError
    with pytest.raises(ValueError):
        to_netmask("abc")  # Non-integer string
    
    # Test case for valid mask length conversion
    assert to_netmask("24") == '255.255.255.0'
    assert to_netmask("32") == '255.255.255.255'
    assert to_netmask("16") == '255.255.0.0'
    
    # Test case for invalid mask length conversion (should raise ValueError)
    with pytest.raises(ValueError):
        to_netmask("33")  # Mask length out of range
    
    # Additional test cases for bits calculation and inet_ntoa usage
    val = "24"
    assert is_masklen(val) == True
    bits = 0
    for i in range(32 - int(val), 32):
        bits |= (1 << i)
    expected_netmask = '255.255.255.0'
    assert inet_ntoa(pack('>I', bits)) == expected_netmask
    
    val = "32"
    assert is_masklen(val) == True
    bits = 0
    for i in range(32 - int(val), 32):
        bits |= (1 << i)
    expected_netmask = '255.255.255.255'
    assert inet_ntoa(pack('>I', bits)) == expected_netmask
    
    val = "16"
    assert is_masklen(val) == True
    bits = 0
    for i in range(32 - int(val), 32):
        bits |= (1 << i)
    expected_netmask = '255.255.0.0'
    assert inet_ntoa(pack('>I', bits)) == expected_netmask

# Run the tests
if __name__ == "__main__":
    pytest.main()
