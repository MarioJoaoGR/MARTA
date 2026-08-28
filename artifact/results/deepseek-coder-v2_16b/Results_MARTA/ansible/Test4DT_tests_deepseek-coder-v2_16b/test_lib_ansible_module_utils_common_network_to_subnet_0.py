
import pytest
from ansible.module_utils.common.network import to_subnet

def is_masklen(mask):
    try:
        mask = int(mask)
        return 0 <= mask <= 32
    except ValueError:
        return False

def to_netmask(masklen):
    bits = ['0'] * 4
    for i in range(int(masklen)):
        bits[i // 8] = str(int(bits[i // 8]) | (1 << (7 - i % 8)))
    return '.'.join(bits)

def to_masklen(netmask):
    try:
        parts = [int(part) for part in netmask.split('.')]
        masklen = sum([bin(octet).count('1') for octet in parts])
        return masklen
    except ValueError:
        raise ValueError("Invalid netmask")

# Test cases
def test_valid_case_1():
    addr = '192.168.1.1'
    mask = '255.255.255.0'
    result = to_subnet(addr, mask)
    assert result == '192.168.1.0/24'

def test_valid_case_2():
    addr = '192.168.1.1'
    mask = 24
    result = to_subnet(addr, mask)
    assert result == '192.168.1.0/24'

def test_error_case():
    addr = '192.168.1.1'
    mask = 'invalid_netmask'
    with pytest.raises(ValueError):
        to_subnet(addr, mask)
