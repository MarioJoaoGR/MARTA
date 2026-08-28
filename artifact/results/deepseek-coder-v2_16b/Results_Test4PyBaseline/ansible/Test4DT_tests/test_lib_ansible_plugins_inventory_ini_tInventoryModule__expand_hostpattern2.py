
import pytest
from ansible.errors import AnsibleParserError
from ansible.plugins.inventory.ini import InventoryModule

# Test cases for the _expand_hostpattern method in InventoryModule class
def test_expand_hostpattern_valid():
    inventory_module = InventoryModule()
    hosts, port = inventory_module._expand_hostpattern("example.com")
    assert isinstance(hosts, list)
    assert len(hosts) == 1
    assert hosts[0] == "example.com"