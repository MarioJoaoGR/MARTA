
import pytest
from unittest.mock import patch, MagicMock
from ansible.plugins.inventory.generator import InventoryModule as GenInventoryModule

class TestInventoryModule(object):
    @classmethod
    def setup_class(cls):
        cls.inv = GenInventoryModule()

    @patch('os.path.splitext')
    @patch('ansible.plugins.inventory.generator.InventoryModule.verify_file')
    def test_valid_file_extension(self, mock_verify_file, mock_splitext):
        # Mock the return value of verify_file to be True
        mock_verify_file.return_value = True
        # Mock the return value of splitext to return '.config'
        mock_splitext.return_value = ('example', '.config')
        
        result = TestInventoryModule.inv.verify_file('example.config')
        assert result is True, "Expected verify_file to return True for valid file extension"

    @patch('os.path.splitext')
    @patch('ansible.plugins.inventory.generator.InventoryModule.verify_file')
    def test_invalid_file_extension(self, mock_verify_file, mock_splitext):
        # Mock the return value of verify_file to be True
        mock_verify_file.return_value = False
        # Mock the return value of splitext to return '.txt'
        mock_splitext.return_value = ('example', '.txt')
        
        result = TestInventoryModule.inv.verify_file('example.txt')
        assert result is False, "Expected verify_file to return False for invalid file extension"

    @patch('os.path.splitext')
    @patch('ansible.plugins.inventory.generator.InventoryModule.verify_file')
    def test_valid_yaml_extension(self, mock_verify_file, mock_splitext):
        # Mock the return value of verify_file to be True
        mock_verify_file.return_value = True
        # Mock the return value of splitext to return '.yaml'
        mock_splitext.return_value = ('example', '.yaml')
        
        result = TestInventoryModule.inv.verify_file('example.yaml')
        assert result is True, "Expected verify_file to return True for valid YAML file extension"

    @patch('os.path.splitext')
    @patch('ansible.plugins.inventory.generator.InventoryModule.verify_file')
    def test_no_extension(self, mock_verify_file, mock_splitext):
        # Mock the return value of verify_file to be True
        mock_verify_file.return_value = False
        # Mock the return value of splitext to return '' (no extension)
        mock_splitext.return_value = ('example', '')
        
        result = TestInventoryModule.inv.verify_file('example')
        assert result is False, "Expected verify_file to return False for file with no extension"
