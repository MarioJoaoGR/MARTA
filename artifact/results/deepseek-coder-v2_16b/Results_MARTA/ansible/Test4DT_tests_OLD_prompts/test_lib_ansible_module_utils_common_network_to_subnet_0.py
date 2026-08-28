
import pytest
from unittest.mock import patch
from ansible.module_utils.common.network import to_subnet

def test_valid_case_1():
    with patch('ansible.module_utils.common.network.to_netmask', return_value='255.255.255.0'):
        result = to_subnet("192.168.1.1", "255.255.255.0")
        assert result == '192.168.1.0/24'

def test_valid_case_2():
    with patch('ansible.module_utils.common.network.to_netmask', return_value='255.255.255.0'):
        result = to_subnet("192.168.1.1", 24)
        assert result == '192.168.1.0/24'

def test_invalid_input():
    with pytest.raises(ValueError):
        to_subnet("192.168.1.1", "33")  # Invalid mask length
