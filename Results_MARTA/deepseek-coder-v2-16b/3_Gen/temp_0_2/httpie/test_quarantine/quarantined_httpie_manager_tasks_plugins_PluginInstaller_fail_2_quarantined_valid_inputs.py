
import pytest
from unittest.mock import patch, MagicMock
from httpie.manager.tasks.plugins import PluginInstaller
from httpie.environment import Environment
from pathlib import Path

@pytest.fixture
def setup_env():
    env = Environment()
    env.config = MagicMock()
    env.config.plugins_dir = Path('/some/directory')
    return env

@patch('httpie.manager.tasks.plugins.os.makedirs')
def test_setup_plugins_dir(mock_makedirs, setup_env):
    mock_makedirs.side_effect = OSError("Permission denied")
    installer = PluginInstaller(setup_env)
    
    with pytest.raises(OSError):
        installer.setup_plugins_dir()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_manager_tasks_plugins_PluginInstaller_fail_2_test_valid_inputs
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_manager_tasks_plugins_PluginInstaller_fail_2_test_valid_inputs.py:5:0: E0401: Unable to import 'httpie.environment' (import-error)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_manager_tasks_plugins_PluginInstaller_fail_2_test_valid_inputs.py:5:0: E0611: No name 'environment' in module 'httpie' (no-name-in-module)


"""