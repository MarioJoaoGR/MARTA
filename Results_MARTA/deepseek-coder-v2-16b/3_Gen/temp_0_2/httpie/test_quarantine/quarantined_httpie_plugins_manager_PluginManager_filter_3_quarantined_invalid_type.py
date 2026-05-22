
import pytest
from httpie.plugins.manager import PluginManager

def test_invalid_type():
    manager = PluginManager()
    
    with pytest.raises(TypeError):
        manager.filter(by_type=int)  # This should raise TypeError because int is not a subclass of BasePlugin

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

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_plugins_manager_PluginManager_filter_3_test_invalid_type.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_type _______________________________

    def test_invalid_type():
        manager = PluginManager()
    
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_plugins_manager_PluginManager_filter_3_test_invalid_type.py:8: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_plugins_manager_PluginManager_filter_3_test_invalid_type.py::test_invalid_type
============================== 1 failed in 0.21s ===============================
"""