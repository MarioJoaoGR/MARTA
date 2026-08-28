
import pytest
from ansible.module_utils.common.network import is_netmask

# Define a set of valid masks for testing
VALID_MASKS = {255, 254, 252, 248, 240, 224, 192, 128, 0}


def test_invalid_netmask_integer():
    val = 1
    assert is_netmask(val) == False

def test_valid_netmask_string():
    val = "255.255.255.0"
    assert is_netmask(val) == True

def test_invalid_netmask_string():
    val = "255.255.255"
    assert is_netmask(val) == False