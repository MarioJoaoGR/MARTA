
import pytest
from ansible.module_utils.common.network import to_subnet

# Test valid case 1: Test standard input with valid IP address and netmask in dotted notation
def test_valid_case_1():
    addr = '192.168.1.1'
    mask = '255.255.255.0'
    result = to_subnet(addr, mask)
    assert result == '192.168.1.0/24'

# Test valid case 2: Test standard input with valid IP address and mask length
def test_valid_case_2():
    addr = '192.168.1.1'
    mask = 24
    result = to_subnet(addr, mask)
    assert result == '192.168.1.0/24'

# Test error case: Test raising ValueError with invalid netmask
def test_error_case():
    addr = '192.168.1.1'
    mask = 'invalid_netmask'
    with pytest.raises(ValueError):
        to_subnet(addr, mask)
