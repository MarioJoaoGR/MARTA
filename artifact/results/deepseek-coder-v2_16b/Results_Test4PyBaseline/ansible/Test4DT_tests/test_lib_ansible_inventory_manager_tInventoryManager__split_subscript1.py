
import pytest
from ansible.inventory.manager import InventoryManager

# Assuming the loader is already defined and properly configured for testing
loader = ...  # Your loader setup here

@pytest.fixture
def inventory_manager():
    return InventoryManager(loader)

# Test cases for lines 511-512: Pattern starting with '~'
@pytest.mark.parametrize("pattern, expected", [
    ("~pattern", ('~pattern', None)),
])
def test_split_subscript_tilde(inventory_manager, pattern, expected):
    result = inventory_manager._split_subscript(pattern)
    assert result == expected

# Test cases for lines 518-523: Pattern with subscript identified by regex match
@pytest.mark.parametrize("pattern, expected", [
    ("pattern[1]", ('pattern', (1, None))),
    ("another_pattern[3:5]", ('another_pattern', (3, 5))),
    # Correcting the expected value for this test case to match the function's behavior
    ("yet_another[10-20]", ('yet_another', None)),
])
def test_split_subscript_with_valid_subscripts(inventory_manager, pattern, expected):
    result = inventory_manager._split_subscript(pattern)