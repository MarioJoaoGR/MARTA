
from pathlib import Path
import pytest
from unittest.mock import patch, MagicMock
from httpie.plugins.manager import PluginManager

class TestPluginManagerIterEntryPoints:
    
    @patch('httpie.plugins.manager.importlib_metadata.entry_points')
    def test_iter_entry_points_invalid_directory(self, mock_eps):
        # Mock the entry points to return an empty set
        mock_eps.return_value = MagicMock()
        mock_eps.return_value.select.return_value = []
        
        pm = PluginManager()
        with pytest.raises(ValueError):
            list(pm.iter_entry_points(Path('/invalid/directory')))

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

httpie/Test4DT_tests_codestral/test_httpie_plugins_manager_PluginManager_iter_entry_points_0_test_invalid_directory.py F [100%]

=================================== FAILURES ===================================
__ TestPluginManagerIterEntryPoints.test_iter_entry_points_invalid_directory ___

self = <Test4DT_tests_codestral.test_httpie_plugins_manager_PluginManager_iter_entry_points_0_test_invalid_directory.TestPluginManagerIterEntryPoints object at 0x7f34117dc310>
mock_eps = <MagicMock name='entry_points' id='139861604341328'>

    @patch('httpie.plugins.manager.importlib_metadata.entry_points')
    def test_iter_entry_points_invalid_directory(self, mock_eps):
        # Mock the entry points to return an empty set
        mock_eps.return_value = MagicMock()
        mock_eps.return_value.select.return_value = []
    
        pm = PluginManager()
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

httpie/Test4DT_tests_codestral/test_httpie_plugins_manager_PluginManager_iter_entry_points_0_test_invalid_directory.py:16: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_plugins_manager_PluginManager_iter_entry_points_0_test_invalid_directory.py::TestPluginManagerIterEntryPoints::test_iter_entry_points_invalid_directory
============================== 1 failed in 0.16s ===============================
"""