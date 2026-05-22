
import pytest
from unittest.mock import patch, MagicMock
from pathlib import Path
from httpie.plugins.manager import PluginManager, find_entry_points, ENTRY_POINT_NAMES
import importlib_metadata

class TestPluginManager:
    @patch('httpie.plugins.manager.find_entry_points')
    @patch('httpie.plugins.manager.ENTRY_POINT_NAMES', ['group1', 'group2'])
    def test_iter_entry_points_with_directory(self, mock_find_entry_points):
        # Mock the entry points for testing
        eps = MagicMock()
        eps.groups = {'group1': [MagicMock(), MagicMock()], 'group2': [MagicMock(), MagicMock()]}
    
        with patch('httpie.plugins.manager.importlib_metadata.entry_points', return_value=eps):
            pm = PluginManager()
            result = list(pm.iter_entry_points(Path('/path/to/plugins')))
    
            # Check that find_entry_points was called with the correct arguments
            mock_find_entry_points.assert_has_calls([
                pytest.approx(call(eps, group='group1')),
                pytest.approx(call(eps, group='group2'))
            ])

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_plugins_manager_PluginManager_iter_entry_points_0_test_valid_inputs
httpie/Test4DT_tests_codestral/test_httpie_plugins_manager_PluginManager_iter_entry_points_0_test_valid_inputs.py:22:30: E0602: Undefined variable 'call' (undefined-variable)
httpie/Test4DT_tests_codestral/test_httpie_plugins_manager_PluginManager_iter_entry_points_0_test_valid_inputs.py:23:30: E0602: Undefined variable 'call' (undefined-variable)


"""