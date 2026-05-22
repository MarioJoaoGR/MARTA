
import pytest
from unittest.mock import patch, MagicMock
from httpie.manager.tasks.plugins import PluginInstaller, Environment, ExitStatus

@pytest.fixture
def setup_plugin_installer():
    env = MagicMock()
    env.config.plugins_dir = "/path/to/plugins"
    installer = PluginInstaller(env=env)
    return installer

def test_install_plugins(setup_plugin_installer):
    installer = setup_plugin_installer
    with patch('httpie.manager.tasks.plugins.subprocess') as mock_subprocess:
        mock_subprocess.run.return_value = (MagicMock(), ExitStatus.SUCCESS)
        
        result = installer.install(['plugin1', 'plugin2'])
        
        assert result == ExitStatus.SUCCESS
        mock_subprocess.run.assert_called_with(
            ['pip', 'install', '--upgrade', 'plugin1', 'plugin2'],
            stdout=installer.env.stdout,
            stderr=installer.env.stderr
        )

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

httpie/Test4DT_tests_codestral/test_httpie_manager_tasks_plugins_PluginInstaller_install_0_test_valid_input.py E [100%]

==================================== ERRORS ====================================
____________________ ERROR at setup of test_install_plugins ____________________

    @pytest.fixture
    def setup_plugin_installer():
        env = MagicMock()
        env.config.plugins_dir = "/path/to/plugins"
>       installer = PluginInstaller(env=env)

httpie/Test4DT_tests_codestral/test_httpie_manager_tasks_plugins_PluginInstaller_install_0_test_valid_input.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
httpie/httpie/manager/tasks/plugins.py:28: in __init__
    self.setup_plugins_dir()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <httpie.manager.tasks.plugins.PluginInstaller object at 0x7f79a7a09510>

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
ERROR httpie/Test4DT_tests_codestral/test_httpie_manager_tasks_plugins_PluginInstaller_install_0_test_valid_input.py::test_install_plugins
=============================== 1 error in 0.25s ===============================
"""