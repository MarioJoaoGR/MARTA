
import unittest
from unittest.mock import patch, MagicMock
from httpie.plugins.manager import PluginManager
from pathlib import Path
import importlib_metadata

class TestPluginManager(unittest.TestCase):
    
    @patch('httpie.plugins.manager.find_entry_points')
    @patch('httpie.plugins.manager.ENTRY_POINT_NAMES', ['group1', 'group2'])
    def test_iter_entry_points_invalid_path(self, mock_find_entry_points):
        pm = PluginManager()
        
        # Mock the importlib_metadata.entry_points to return a list of entry points
        with patch('httpie.plugins.manager.importlib_metadata.entry_points', return_value=MagicMock()) as mock_eps:
            eps = mock_eps.return_value
            
            # Mock the find_entry_points to yield some values
            def side_effect(eps, group):
                if group == 'group1':
                    yield from [MagicMock(), MagicMock()]
                elif group == 'group2':
                    yield from [MagicMock(), MagicMock()]
            
            mock_find_entry_points.side_effect = side_effect
            
            # Call the method under test
            result = list(pm.iter_entry_points(Path('/invalid/path')))
            
            # Assertions to verify the behavior
            self.assertEqual(len(result), 4)  # Since we mocked two groups with 2 entry points each, there should be 4 results
            mock_find_entry_points.assert_called()
            mock_eps.assert_called()
