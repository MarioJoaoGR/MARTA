
import unittest
from unittest.mock import patch, MagicMock
from httpie.plugins.manager import PluginManager
from pathlib import Path
import importlib_metadata

class TestPluginManager(unittest.TestCase):
    
    def test_iter_entry_points_with_directory(self):
        pm = PluginManager()
        with patch('httpie.plugins.manager.find_entry_points') as mock_find_entry_points:
            mock_eps = MagicMock()
            with patch('httpie.plugins.manager.importlib_metadata.entry_points', return_value=mock_eps):
                for ep in pm.iter_entry_points(Path('/path/to/plugins')):
                    pass  # Add assertions if needed to verify the behavior
    
    def test_iter_entry_points_without_directory(self):
        pm = PluginManager()
        with patch('httpie.plugins.manager.find_entry_points') as mock_find_entry_points:
            with patch('httpie.plugins.manager.importlib_metadata.entry_points', return_value=MagicMock()):
                for ep in pm.iter_entry_points():
                    pass  # Add assertions if needed to verify the behavior
