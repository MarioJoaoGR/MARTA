
import pytest
from unittest.mock import patch, MagicMock
from ansible.plugins.inventory.yaml import InventoryModule


@patch('ansible.plugins.inventory.yaml.InventoryModule._expand_hostpattern')
def test_valid_host_pattern(mock_expand_hostpattern):
    mock_expand_hostpattern.return_value = (['example.com'], None)
    inventory_module = InventoryModule()
    hostnames, port = inventory_module._parse_host('example.com')
    assert hostnames == ['example.com']
    assert port is None

@patch('ansible.plugins.inventory.yaml.InventoryModule._expand_hostpattern')
def test_valid_host_pattern_with_port(mock_expand_hostpattern):
    mock_expand_hostpattern.return_value = (['example.com'], 8080)
    inventory_module = InventoryModule()
    hostnames, port = inventory_module._parse_host('example.com:8080')
    assert hostnames == ['example.com']
    assert port == 8080

@patch('ansible.plugins.inventory.yaml.InventoryModule._expand_hostpattern')
def test_invalid_host_pattern(mock_expand_hostpattern):
    mock_expand_hostpattern.side_effect = TypeError("Invalid host pattern")
    inventory_module = InventoryModule()
    with pytest.raises(TypeError):
        inventory_module._parse_host('invalid*pattern')