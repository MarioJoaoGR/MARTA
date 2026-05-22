
import pytest
from unittest.mock import patch, MagicMock
from httpie.plugins.manager import PluginManager

class TestPluginManagerIterEntryPoints:
    
    def test_invalid_path(self):
        pm = PluginManager()
        
        with patch('httpie.plugins.manager.enable_plugins') as mock_enable_plugins:
            mock_enable_plugins.return_value.__enter__.return_value = None
            
            with patch('httpie.plugins.manager.importlib_metadata.entry_points') as mock_eps:
                mock_eps.return_value = MagicMock()
                
                with pytest.raises(ValueError):
                    list(pm.iter_entry_points('invalid/path'))

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_plugins_manager_PluginManager_iter_entry_points_3_test_invalid_path.py F [100%]

=================================== FAILURES ===================================
______________ TestPluginManagerIterEntryPoints.test_invalid_path ______________

self = <test_httpie_plugins_manager_PluginManager_iter_entry_points_3_test_invalid_path.TestPluginManagerIterEntryPoints object at 0x7f6299787510>

    def test_invalid_path(self):
        pm = PluginManager()
    
        with patch('httpie.plugins.manager.enable_plugins') as mock_enable_plugins:
            mock_enable_plugins.return_value.__enter__.return_value = None
    
            with patch('httpie.plugins.manager.importlib_metadata.entry_points') as mock_eps:
                mock_eps.return_value = MagicMock()
    
>               with pytest.raises(ValueError):
E               Failed: DID NOT RAISE <class 'ValueError'>

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_plugins_manager_PluginManager_iter_entry_points_3_test_invalid_path.py:17: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_plugins_manager_PluginManager_iter_entry_points_3_test_invalid_path.py::TestPluginManagerIterEntryPoints::test_invalid_path
============================== 1 failed in 0.21s ===============================
"""