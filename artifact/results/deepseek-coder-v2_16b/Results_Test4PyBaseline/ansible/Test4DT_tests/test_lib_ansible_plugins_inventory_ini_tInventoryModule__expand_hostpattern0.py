
import pytest
from ansible.errors import AnsibleParserError  # Corrected import and variable name
from ansible.plugins.inventory.ini import InventoryModule

# Test cases for the _expand_hostpattern method in InventoryModule class
def test_expand_hostpattern_valid():
    inventory_module = InventoryModule()
    hosts, port = inventory_module._expand_hostpattern("example.com")
    assert isinstance(hosts, list)
    assert len(hosts) == 1
    assert hosts[0] == "example.com"
    assert port is None

def test_expand_hostpattern_with_port():
    inventory_module = InventoryModule()
    with pytest.raises(AnsibleParserError):  # Corrected the expected exception
        inventory_module._expand_hostpattern("example.com:80")

def test_expand_hostpattern_invalid_yaml():
    inventory_module = InventoryModule()
    with pytest.raises(AnsibleParserError):  # Corrected the expected exception
        inventory_module._expand_hostpattern("---")

def test_expand_hostpattern_empty_string():
    inventory_module = InventoryModule()
    hosts, port = inventory_module._expand_hostpattern("")
    assert isinstance(hosts, list)
    assert len(hosts) == 0
    assert port is None
