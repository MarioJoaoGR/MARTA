
import pytest
from ansible.cli.inventory import InventoryCLI

def test_init_with_valid_args():
    args = {'host': 'example_host', 'group': 'example_group'}
    inventory_cli = InventoryCLI(args)
    assert isinstance(inventory_cli, InventoryCLI), "Expected an instance of InventoryCLI"
