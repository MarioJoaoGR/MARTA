
import unittest
from unittest.mock import patch, MagicMock
from httpie.plugins.manager import PluginManager
from pathlib import Path
import importlib_metadata

class TestPluginManager(unittest.TestCase):
    
    def test_iter_entry_points_invalid_directory(self):
        pm = PluginManager()
        
        with patch('httpie.plugins.manager.enable_plugins') as mock_enable_plugins:
            mock_enable_plugins.return_value.__enter__.return_value = None
            
            with patch('httpie.plugins.manager.importlib_metadata.entry_points') as mock_eps:
                mock_eps.return_value = MagicMock()
                
                with patch('httpie.plugins.manager.find_entry_points') as mock_find_entry_points:
                    mock_find_entry_points.return_value = iter([])
                    
                    for ep in pm.iter_entry_points(Path('/invalid/directory')):
                        self.fail("Expected no entry points, but got one")
