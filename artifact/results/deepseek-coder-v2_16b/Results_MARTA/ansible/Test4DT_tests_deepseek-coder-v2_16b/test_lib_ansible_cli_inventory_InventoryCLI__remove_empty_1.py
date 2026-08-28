
import pytest
from ansible.cli.inventory import InventoryCLI

def test_edge_cases():
    args = {}
    with pytest.raises(ValueError):
        inventory_cli = InventoryCLI(args)
