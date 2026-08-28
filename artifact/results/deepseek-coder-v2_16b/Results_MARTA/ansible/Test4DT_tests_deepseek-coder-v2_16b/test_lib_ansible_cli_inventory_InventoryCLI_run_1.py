
import pytest
from ansible.cli.inventory import InventoryCLI

def test_edge_cases():
    args = None
    with pytest.raises(ValueError):
        InventoryCLI(args)
