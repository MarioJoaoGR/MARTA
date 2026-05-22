
import pytest
from unittest.mock import patch, MagicMock
from httpie.manager.tasks.plugins import PluginInstaller
from httpie.environment import Environment

@pytest.fixture
def setup_plugin_installer():
    env = MagicMock()
    env.config.plugins_dir = "/path/to/plugins"
    with patch('httpie.manager.tasks.plugins.Path', return_value=MagicMock(mkdir=lambda exist_ok, parents: None)):
        yield PluginInstaller(env=env, debug=True)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_manager_tasks_plugins_PluginInstaller_list_0_test_valid_case
httpie/Test4DT_tests_codestral/test_httpie_manager_tasks_plugins_PluginInstaller_list_0_test_valid_case.py:5:0: E0401: Unable to import 'httpie.environment' (import-error)
httpie/Test4DT_tests_codestral/test_httpie_manager_tasks_plugins_PluginInstaller_list_0_test_valid_case.py:5:0: E0611: No name 'environment' in module 'httpie' (no-name-in-module)


"""