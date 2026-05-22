
import pytest
from unittest.mock import patch, MagicMock
from httpie.plugins.manager import PluginManager, find_entry_points, ENTRY_POINT_NAMES
from pathlib import Path
import importlib_metadata

class TestPluginManager:
    
    @patch('httpie.plugins.manager.find_entry_points')
    @patch('httpie.plugins.manager.ENTRY_POINT_NAMES', ['group1', 'group2'])
    def test_none_input(self, mock_find_entry_points):
        # Create a mock entry point for testing
        ep = MagicMock()
        eps = {
            'group1': [ep],
            'group2': [ep]
        }
        
        with patch('httpie.plugins.manager.importlib_metadata.entry_points', return_value=eps):
            pm = PluginManager()
            result = list(pm.iter_entry_points())
    
            # Check that find_entry_points was called for each group
            self.assertEqual(len(mock_find_entry_points.call_args_list), 2)
            mock_find_entry_points.assert_any_call(eps, group='group1')
            mock_find_entry_points.assert_any_call(eps, group='group2')
    
            # Check that the result contains all entry points from both groups
            self.assertEqual(len(result), 4)  # Assuming each group has 2 entry points

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_plugins_manager_PluginManager_iter_entry_points_1_test_none_input
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_plugins_manager_PluginManager_iter_entry_points_1_test_none_input.py:25:12: E1101: Instance of 'TestPluginManager' has no 'assertEqual' member (no-member)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_plugins_manager_PluginManager_iter_entry_points_1_test_none_input.py:30:12: E1101: Instance of 'TestPluginManager' has no 'assertEqual' member (no-member)


"""