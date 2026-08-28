
import pytest
from ansible.module_utils.common.network import to_masklen

# Test cases for valid inputs
def test_valid_dot_decimal():
    assert to_masklen("255.255.255.0") == 24
    # Corrected the invalid input assertion to match the function's expected behavior
    with pytest.raises(ValueError):
        to_masklen("255.255.255")
