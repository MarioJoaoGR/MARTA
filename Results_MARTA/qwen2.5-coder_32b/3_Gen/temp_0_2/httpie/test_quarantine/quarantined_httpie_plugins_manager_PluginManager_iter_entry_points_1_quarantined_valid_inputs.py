
from pathlib import Path
from unittest.mock import patch, MagicMock
import pytest
from httpie.plugins.manager import PluginManager, enable_plugins, find_entry_points
importlib_metadata

class TestPluginManager:
    def test_iter_entry_points_with_directory(self):
        pm = PluginManager()
        with patch('httpie.plugins.manager.enable_plugins') as mock_enable_plugins:
            mock_eps = MagicMock()
            mock_eps.__iter__.return_value = [MagicMock()]
            importlib_metadata.entry_points = lambda: mock_eps
    
            with patch('httpie.plugins.manager.find_entry_points') as mock_find_entry_points:
                mock_find_entry_points.side_effect = lambda eps, group: list(eps)[0]
    
                directory = Path('/path/to/plugins')
                result = list(pm.iter_entry_points(directory))
    
                assert len(result) == 1
    
    def test_iter_entry_points_without_directory(self):
        pm = PluginManager()
        with patch('httpie.plugins.manager.enable_plugins') as mock_enable_plugins:
            importlib_metadata.entry_points = lambda: MagicMock()
    
            result = list(pm.iter_entry_points())
    
            assert len(result) == 0
            mock_enable_plugins.assert_not_called()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_plugins_manager_PluginManager_iter_entry_points_1_test_valid_inputs
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_plugins_manager_PluginManager_iter_entry_points_1_test_valid_inputs.py:6:0: E0602: Undefined variable 'importlib_metadata' (undefined-variable)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_plugins_manager_PluginManager_iter_entry_points_1_test_valid_inputs.py:14:12: E0602: Undefined variable 'importlib_metadata' (undefined-variable)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_plugins_manager_PluginManager_iter_entry_points_1_test_valid_inputs.py:27:12: E0602: Undefined variable 'importlib_metadata' (undefined-variable)


"""