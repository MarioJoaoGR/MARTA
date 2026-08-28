
import pytest
from ansible.errors import AnsibleParserError
from ansible.plugins.inventory.ini import InventoryModule

@pytest.fixture(scope="module")
def inventory_module():
    return InventoryModule()

def test_expand_hostpattern_invalid_colon(inventory_module):
    hostpattern = "hostname:"
    with pytest.raises(AnsibleParserError) as excinfo:
        inventory_module._expand_hostpattern(hostpattern)
    assert str(excinfo.value) == "Invalid host pattern 'hostname:' supplied, ending in ':' is not allowed, this character is reserved to provide a port."
