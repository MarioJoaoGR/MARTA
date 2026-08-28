
import pytest
from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork

# Test 1: Valid input with specific address
def test_valid_input_with_specific_address():
    network = GenericBsdIfconfigNetwork()
    defaults = {'interface': 'eth0', 'address': '192.168.1.1'}
    interfaces = {
        'eth0': {
            'ipv4': [
                {'address': '192.168.1.1'},
                {'address': '192.168.1.2'}
            ],
            'ipv6': [],
            'mac': '00:1A:2B:3C:4D:5E'
        }
    }
    merged_settings = network.merge_default_interface(defaults, interfaces, 'ipv4')
    assert merged_settings['address'] == '192.168.1.1'
    assert merged_settings['mac'] == '00:1A:2B:3C:4D:5E'

# Test 2: Valid input without address
def test_valid_input_without_address():
    network = GenericBsdIfconfigNetwork()
    defaults = {'interface': 'eth0'}
    interfaces = {
        'eth0': {
            'ipv4': [
                {'address': '192.168.1.1'},
                {'address': '192.168.1.2'}
            ],
            'ipv6': [],
            'mac': '00:1A:2B:3C:4D:5E'
        }
    }
    merged_settings = network.merge_default_interface(defaults, interfaces, 'ipv4')
    assert merged_settings['address'] == '192.168.1.1'
    assert merged_settings['mac'] == '00:1A:2B:3C:4D:5E'

# Test 3: Invalid input missing interface
def test_invalid_input_missing_interface():
    network = GenericBsdIfconfigNetwork()
    defaults = {'address': '192.168.1.1'}
    interfaces = {
        'eth0': {
            'ipv4': [
                {'address': '192.168.1.1'},
                {'address': '192.168.1.2'}
            ],
            'ipv6': [],
            'mac': '00:1A:2B:3C:4D:5E'
        }
    }
    merged_settings = network.merge_default_interface(defaults, interfaces, 'ipv4')
    assert merged_settings is None
