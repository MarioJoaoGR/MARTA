
import pytest
from ansible.module_utils.common.network import to_masklen

# Test cases for invalid inputs
def test_invalid_netmask():
    with pytest.raises(ValueError) as excinfo:
        to_masklen("256.256.256.256")  # Invalid netmask, should raise ValueError
    assert str(excinfo.value) == 'invalid value for netmask: 256.256.256.256'

def test_invalid_type():
    with pytest.raises(ValueError) as excinfo:
        to_masklen(12345)  # Invalid type, should raise ValueError
    assert str(excinfo.value) == 'invalid value for netmask: 12345'

def test_empty_string():
    with pytest.raises(ValueError) as excinfo:
        to_masklen("")  # Empty string, should raise ValueError