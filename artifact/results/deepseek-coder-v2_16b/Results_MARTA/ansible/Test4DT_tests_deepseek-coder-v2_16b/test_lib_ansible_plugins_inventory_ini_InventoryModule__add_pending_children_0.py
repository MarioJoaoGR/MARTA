
import pytest
from ansible.plugins.inventory import ini

class InventoryModule(ini.InventoryModule):
    def __init__(self):
        super(InventoryModule, self).__init__()
        self.patterns = {}
        self._filename = None

    def _add_pending_children(self, group, pending):
        for parent in pending[group]['parents']:
            self.inventory.add_child(parent, group)
            if parent in pending and pending[parent]['state'] == 'children':
                self._add_pending_children(parent, pending)
        del pending[group]

def test_edge_case():
    inventory_module = InventoryModule()
    with pytest.raises(AttributeError):
        inventory_module.parse_options(['--list'], host=None, user=None)
