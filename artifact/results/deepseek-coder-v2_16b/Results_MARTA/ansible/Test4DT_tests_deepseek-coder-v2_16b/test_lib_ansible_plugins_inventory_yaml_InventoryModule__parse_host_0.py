
import pytest
from ansible.plugins.inventory.yaml import InventoryModule

@pytest.fixture
def inventory_module():
    return InventoryModule()

# Test for valid host pattern
def test_valid_hostpattern(inventory_module):
    hostnames, port = inventory_module._parse_host('example.com')
    assert isinstance(hostnames, list)
    assert hostnames == ['example.com']
    assert port is None

# Test for wildcard host pattern expansion
def test_wildcard_hostpattern(inventory_module):
    hostnames, port = inventory_module._parse_host('*.example.com')
    assert isinstance(hostnames, list)
    # Assuming the method _expand_hostpattern expands wildcards correctly
    assert len(hostnames) > 0
    assert port is None

# Test for invalid host pattern with error handling
def test_invalid_hostpattern(inventory_module):
    try:
        inventory_module._parse_host('example.com:invalidport')
    except ValueError as e:
        pass
