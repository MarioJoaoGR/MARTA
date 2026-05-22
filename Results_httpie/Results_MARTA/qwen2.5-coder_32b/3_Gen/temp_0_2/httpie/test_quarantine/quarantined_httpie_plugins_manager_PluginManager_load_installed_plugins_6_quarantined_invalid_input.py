
import pytest
from httpie.plugins.manager import PluginManager
from pathlib import Path
from unittest.mock import patch, MagicMock

def test_invalid_input():
    pm = PluginManager()
    dir_path = '/nonexistent/directory'
    
    with patch('httpie.plugins.manager.warnings.warn') as mock_warn:
        with pytest.raises(FileNotFoundError):
            pm.load_installed_plugins(Path(dir_path))

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

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_plugins_manager_PluginManager_load_installed_plugins_6_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        pm = PluginManager()
        dir_path = '/nonexistent/directory'
    
        with patch('httpie.plugins.manager.warnings.warn') as mock_warn:
>           with pytest.raises(FileNotFoundError):
E           Failed: DID NOT RAISE <class 'FileNotFoundError'>

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_plugins_manager_PluginManager_load_installed_plugins_6_test_invalid_input.py:12: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_plugins_manager_PluginManager_load_installed_plugins_6_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.24s ===============================
"""