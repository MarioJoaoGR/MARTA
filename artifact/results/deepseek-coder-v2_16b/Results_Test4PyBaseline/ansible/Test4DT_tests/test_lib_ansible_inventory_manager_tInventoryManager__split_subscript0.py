
import pytest
from ansible.inventory.manager import InventoryManager

# Assuming the loader is already defined and properly configured for testing
loader = ...  # Your loader setup here

@pytest.fixture
def inventory_manager():
    return InventoryManager(loader)

@pytest.mark.parametrize("pattern, expected", [
    ("pattern[1]", ('pattern', (1, None))),
    ("another_pattern[3:5]", ('another_pattern', (3, 5))),
    ("yet_another[10-20]", ('yet_another', None)),
    ("invalid[syntax]", ('invalid', None)),
    ("~pattern", ('~pattern', None))
])
def test_split_subscript(inventory_manager, pattern, expected):
    result = inventory_manager._split_subscript(pattern)
    assert result == expected
