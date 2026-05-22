
import pytest
from unittest.mock import patch
from httpie.manager.tasks.plugins import PluginInstaller, Environment

@pytest.fixture
def mock_environment():
    class MockEnvironment:
        def __init__(self):
            self.config = type('Config', (object,), {'plugins_dir': '/tmp/plugins'})()
    
    return MockEnvironment()

def test_valid_inputs(mock_environment):
    with patch('httpie.manager.tasks.plugins.Environment', return_value=mock_environment):
        installer = PluginInstaller(env=mock_environment, debug=False)
        assert hasattr(installer, 'dir')

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

httpie/Test4DT_tests_codestral/test_httpie_manager_tasks_plugins_PluginInstaller_uninstall_0_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

mock_environment = <Test4DT_tests_codestral.test_httpie_manager_tasks_plugins_PluginInstaller_uninstall_0_test_valid_inputs.mock_environment.<locals>.MockEnvironment object at 0x7fc2b955fe10>

    def test_valid_inputs(mock_environment):
        with patch('httpie.manager.tasks.plugins.Environment', return_value=mock_environment):
>           installer = PluginInstaller(env=mock_environment, debug=False)

httpie/Test4DT_tests_codestral/test_httpie_manager_tasks_plugins_PluginInstaller_uninstall_0_test_valid_inputs.py:16: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
httpie/httpie/manager/tasks/plugins.py:28: in __init__
    self.setup_plugins_dir()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <httpie.manager.tasks.plugins.PluginInstaller object at 0x7fc2baa64ad0>

    def setup_plugins_dir(self) -> None:
        try:
>           self.dir.mkdir(
                exist_ok=True,
                parents=True
            )
E           AttributeError: 'str' object has no attribute 'mkdir'

httpie/httpie/manager/tasks/plugins.py:32: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_manager_tasks_plugins_PluginInstaller_uninstall_0_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.19s ===============================
"""