
import pytest
from pathlib import Path
from unittest.mock import patch, MagicMock
from httpie.plugins.manager import PluginManager

def test_invalid_directory():
    pm = PluginManager()
    invalid_dir = Path('/nonexistent/path')
    
    with patch('httpie.plugins.manager.warnings.warn') as mock_warn:
        pm.load_installed_plugins(invalid_dir)
        
        # Assert that the warning was called with the expected message
        assert mock_warn.call_count == 1

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

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_plugins_manager_PluginManager_load_installed_plugins_2_test_invalid_directory.py F [100%]

=================================== FAILURES ===================================
____________________________ test_invalid_directory ____________________________

    def test_invalid_directory():
        pm = PluginManager()
        invalid_dir = Path('/nonexistent/path')
    
        with patch('httpie.plugins.manager.warnings.warn') as mock_warn:
            pm.load_installed_plugins(invalid_dir)
    
            # Assert that the warning was called with the expected message
>           assert mock_warn.call_count == 1
E           AssertionError: assert 0 == 1
E            +  where 0 = <MagicMock name='warn' id='140140649714896'>.call_count

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_plugins_manager_PluginManager_load_installed_plugins_2_test_invalid_directory.py:15: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_plugins_manager_PluginManager_load_installed_plugins_2_test_invalid_directory.py::test_invalid_directory
============================== 1 failed in 0.15s ===============================
"""