
import pytest
from ansible.cli.inventory import InventoryCLI
from ansible.errors import AnsibleError



def test_invalid_input():
    args = {}
    with pytest.raises(ValueError):
        InventoryCLI(args)