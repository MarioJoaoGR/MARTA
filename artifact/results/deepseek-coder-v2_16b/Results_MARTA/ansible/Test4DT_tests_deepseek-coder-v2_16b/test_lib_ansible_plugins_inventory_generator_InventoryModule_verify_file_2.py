
import pytest
from ansible.plugins.inventory.generator import InventoryModule
import os

@pytest.fixture(scope="module")
def inventory_module():
    return InventoryModule()

def test_valid_file_extension(inventory_module):
    with pytest.raises(AssertionError):
        assert inventory_module.verify_file('example.config') is True

def test_missing_extension(inventory_module):
    with pytest.raises(AssertionError):
        assert inventory_module.verify_file('example') is True
