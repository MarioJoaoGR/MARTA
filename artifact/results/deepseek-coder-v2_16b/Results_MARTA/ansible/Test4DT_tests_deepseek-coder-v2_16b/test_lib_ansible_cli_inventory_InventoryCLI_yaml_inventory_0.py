
import pytest
from ansible.cli.inventory import InventoryCLI



def test_valid_yaml_inventory():
    args = {'host': 'example-host', 'group': 'example-group'}
    inventory_cli = InventoryCLI(args)
    with pytest.raises(AttributeError):
        top = inventory_cli.inventory.groups['all']  # Assuming 'top' is the root group named 'all'