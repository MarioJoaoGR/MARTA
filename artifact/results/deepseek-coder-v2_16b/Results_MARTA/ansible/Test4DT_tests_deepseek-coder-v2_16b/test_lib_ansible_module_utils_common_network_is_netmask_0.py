
import pytest
from ansible.module_utils.common.network import is_netmask

def test_is_netmask_valid():
    assert is_netmask("255.255.255.0") == True


def test_is_netmask_invalid_string():
    assert is_netmask("255.255.255") == False

def test_is_netmask_invalid_string_out_of_range():
    assert is_netmask("256.255.255.0") == False

def test_is_netmask_invalid_integer():
    assert is_netmask(1) == False