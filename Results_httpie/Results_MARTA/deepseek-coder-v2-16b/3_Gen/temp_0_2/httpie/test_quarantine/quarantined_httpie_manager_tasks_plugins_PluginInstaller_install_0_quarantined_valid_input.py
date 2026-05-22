
import pytest
from unittest.mock import patch, MagicMock
from httpie.manager.tasks.plugins import PluginInstaller
from httpie.manager.environment import Environment
from httpie.manager.tasks.exit_status import ExitStatus

@pytest.fixture
def setup_plugin_installer():
    env = MagicMock()
    env.config.plugins_dir = "/path/to/plugins"
    installer = PluginInstaller(env=env)
    return installer, env

def test_install_success(setup_plugin_installer):
    installer, env = setup_plugin_installer
    with patch('httpie.manager.tasks.plugins._pip_install', return_value=(None, ExitStatus.SUCCESS)):
        result = installer.install(['plugin1'])
        assert result == ExitStatus.SUCCESS
        env.stdout.write.assert_called_with("Installing plugin1...\n")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_manager_tasks_plugins_PluginInstaller_install_0_test_valid_input
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_manager_tasks_plugins_PluginInstaller_install_0_test_valid_input.py:5:0: E0401: Unable to import 'httpie.manager.environment' (import-error)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_manager_tasks_plugins_PluginInstaller_install_0_test_valid_input.py:5:0: E0611: No name 'environment' in module 'httpie.manager' (no-name-in-module)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_manager_tasks_plugins_PluginInstaller_install_0_test_valid_input.py:6:0: E0401: Unable to import 'httpie.manager.tasks.exit_status' (import-error)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_manager_tasks_plugins_PluginInstaller_install_0_test_valid_input.py:6:0: E0611: No name 'exit_status' in module 'httpie.manager.tasks' (no-name-in-module)


"""