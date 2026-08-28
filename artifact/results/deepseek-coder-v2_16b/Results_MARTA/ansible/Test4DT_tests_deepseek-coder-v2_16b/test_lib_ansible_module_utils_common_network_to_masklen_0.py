
import pytest
from ansible.module_utils.common.network import to_masklen

def is_netmask(val):
    """ Helper function to check if a value is a valid netmask """
    try:
        int(val)
        return True
    except ValueError:
        return False

def test_valid_case_1():
    val = "255.255.255.0"
    assert to_masklen(val) == 24, f"Expected masklen for value {val} to be 24, but got {to_masklen(val)}"


def test_invalid_case():
    val = "255.255.255"
    with pytest.raises(ValueError) as excinfo:
        to_masklen(val)
    assert str(excinfo.value) == 'invalid value for netmask: 255.255.255'