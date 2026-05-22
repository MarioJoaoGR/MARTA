
import pytest
from unittest.mock import patch, MagicMock
from httpie.manager.tasks.plugins import PluginInstaller, ExitStatus

@pytest.fixture
def mock_environment():
    env = MagicMock()
    env.config.plugins_dir = "/path/to/plugins"
    return env

def test_uninstall(mock_environment):
    with patch('httpie.manager.tasks.plugins.os.makedirs'):
        installer = PluginInstaller(env=mock_environment)
        
        # Mocking the _uninstall method to always return ExitStatus.SUCCESS
        with patch.object(installer, '_uninstall', return_value=ExitStatus.SUCCESS):
            result = installer.uninstall(["plugin1", "plugin2"])
            
            assert result == ExitStatus.SUCCESS

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

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_manager_tasks_plugins_PluginInstaller_uninstall_0_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
________________________________ test_uninstall ________________________________

mock_environment = <MagicMock id='139674283308944'>

    def test_uninstall(mock_environment):
        with patch('httpie.manager.tasks.plugins.os.makedirs'):
>           installer = PluginInstaller(env=mock_environment)

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_manager_tasks_plugins_PluginInstaller_uninstall_0_test_valid_inputs.py:14: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
httpie/httpie/manager/tasks/plugins.py:28: in __init__
    self.setup_plugins_dir()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <httpie.manager.tasks.plugins.PluginInstaller object at 0x7f0872958550>

    def setup_plugins_dir(self) -> None:
        try:
>           self.dir.mkdir(
                exist_ok=True,
                parents=True
            )
E           AttributeError: 'str' object has no attribute 'mkdir'

httpie/httpie/manager/tasks/plugins.py:32: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_manager_tasks_plugins_PluginInstaller_uninstall_0_test_valid_inputs.py::test_uninstall
============================== 1 failed in 0.26s ===============================
"""