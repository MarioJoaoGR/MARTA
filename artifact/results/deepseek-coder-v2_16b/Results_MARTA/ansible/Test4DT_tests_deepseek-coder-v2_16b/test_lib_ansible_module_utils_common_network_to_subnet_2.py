
import pytest
from your_module import to_subnet

# Helper functions for testing
def is_masklen(mask):
    try:
        mask = int(mask)
        return 0 <= mask <= 32
    except ValueError:
        return False

def to_netmask(mask_length):
    bits = ['0'] * 32
    for i in range(mask_length):
        bits[i] = '1'
    return '.'.join([str(int(''.join(bits[i*8:(i+1)*8]), 2)) for i in range(4)])

def to_masklen(netmask):
    try:
        parts = [int(part) for part in netmask.split('.')]
        binary_parts = ['{:08b}'.format(part) for part in parts]
        mask_length = sum([bin(part).count('1') for part in parts])
        return mask_length
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

def test_valid_case_3():
    addr = '192.168.1.1'
    mask = '255.255.255.0'
    dotted_notation = True
    result = to_subnet(addr, mask, dotted_notation)
    assert result == '192.168.1.0 255.255.255.0'

def test_edge_case_1():
    addr = None
    mask = 24
    with pytest.raises(ValueError):
        to_subnet(addr, mask)

def test_edge_case_2():
    addr = ''
    mask = ''
    with pytest.raises(ValueError):
        to_subnet(addr, mask)

def test_error_case_1():
    addr = '192.168.1.1'
    mask = 'invalid netmask'
    with pytest.raises(ValueError):
        to_subnet(addr, mask)

def test_error_case_2():
    addr = '192.168.1.1'
    mask = 33
    with pytest.raises(ValueError):
        to_subnet(addr, mask)
