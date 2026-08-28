
import pytest
from unittest.mock import patch
from ansible.plugins.inventory.generator import InventoryModule
import os

# Constants for testing
C = type('Constants', (), {'YAML_FILENAME_EXTENSIONS': ['.yaml', '.yml']})()

@pytest.fixture(scope="module")
def inventory_module():
    return InventoryModule()

def test_valid_file_extension(inventory_module):
    with patch('os.path.splitext', return_value=('', '.config')):
        assert inventory_module.verify_file('path/to/example.config') is True

def test_invalid_file_extension(inventory_module):
    with patch('os.path.splitext', return_value=('', '.txt')):
        assert inventory_module.verify_file('path/to/example.txt') is False

def test_missing_file_extension(inventory_module):
    with patch('os.path.splitext', return_value=('', '')):
        assert inventory_module.verify_file('path/to/example') is True
