
import pytest
from pathlib import Path
from unittest.mock import patch, MagicMock
import importlib_metadata

class PluginManager:
    def iter_entry_points(self, directory: Optional[Path] = None):
        with enable_plugins(directory):
            eps = importlib_metadata.entry_points()

            for entry_point_name in ENTRY_POINT_NAMES:
                yield from find_entry_points(eps, group=entry_point_name)

def test_invalid_path():
    pm = PluginManager()
    dir_path = Path('/nonexistent/directory')
    
    with patch('importlib_metadata.entry_points', return_value={}):
        with pytest.raises(FileNotFoundError):
            for ep in pm.iter_entry_points(dir_path):
                print(ep.name, ep.value)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_plugins_manager_PluginManager_iter_entry_points_0_test_invalid_path
httpie/Test4DT_tests_codestral/test_httpie_plugins_manager_PluginManager_iter_entry_points_0_test_invalid_path.py:8:43: E0602: Undefined variable 'Optional' (undefined-variable)
httpie/Test4DT_tests_codestral/test_httpie_plugins_manager_PluginManager_iter_entry_points_0_test_invalid_path.py:9:13: E0602: Undefined variable 'enable_plugins' (undefined-variable)
httpie/Test4DT_tests_codestral/test_httpie_plugins_manager_PluginManager_iter_entry_points_0_test_invalid_path.py:12:36: E0602: Undefined variable 'ENTRY_POINT_NAMES' (undefined-variable)
httpie/Test4DT_tests_codestral/test_httpie_plugins_manager_PluginManager_iter_entry_points_0_test_invalid_path.py:13:27: E0602: Undefined variable 'find_entry_points' (undefined-variable)


"""