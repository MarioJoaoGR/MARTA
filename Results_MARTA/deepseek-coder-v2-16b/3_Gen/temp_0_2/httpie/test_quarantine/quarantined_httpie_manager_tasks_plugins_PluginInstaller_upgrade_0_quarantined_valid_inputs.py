
import pytest
from unittest.mock import patch, MagicMock
from httpie.manager.tasks.plugins import PluginInstaller, Environment, ExitStatus

@pytest.fixture
def setup_plugin_installer():
    env = MagicMock()
    env.config.plugins_dir = "/path/to/plugins"
    installer = PluginInstaller(env=env)
    return installer

def test_upgrade_successful(setup_plugin_installer):
    installer = setup_plugin_installer
    with patch('httpie.manager.tasks.plugins.PluginInstaller._install', return_value=("Successfully installed plugin1 plugin2\n", ExitStatus.SUCCESS)):
        result = installer.upgrade(['plugin1', 'plugin2'])
        assert result == ExitStatus.SUCCESS
        assert installer._clear_metadata.called

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

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_manager_tasks_plugins_PluginInstaller_upgrade_0_test_valid_inputs.py E [100%]

==================================== ERRORS ====================================
__________________ ERROR at setup of test_upgrade_successful ___________________

    @pytest.fixture
    def setup_plugin_installer():
        env = MagicMock()
        env.config.plugins_dir = "/path/to/plugins"
>       installer = PluginInstaller(env=env)

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_manager_tasks_plugins_PluginInstaller_upgrade_0_test_valid_inputs.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
httpie/httpie/manager/tasks/plugins.py:28: in __init__
    self.setup_plugins_dir()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <httpie.manager.tasks.plugins.PluginInstaller object at 0x7ff480697950>

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
ERROR httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_manager_tasks_plugins_PluginInstaller_upgrade_0_test_valid_inputs.py::test_upgrade_successful
=============================== 1 error in 0.32s ===============================
"""