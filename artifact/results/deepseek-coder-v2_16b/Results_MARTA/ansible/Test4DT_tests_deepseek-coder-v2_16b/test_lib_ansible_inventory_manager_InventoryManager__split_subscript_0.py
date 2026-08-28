
import pytest
from ansible.inventory.manager import InventoryManager


def test_split_subscript_with_empty_string():
    manager = InventoryManager(loader=None)
    with pytest.raises(IndexError):
        manager._split_subscript(pattern="")

