
import pytest
from unittest.mock import patch
from httpie.manager.tasks.plugins import PluginInstaller
from httpie.environment import Environment

def test_setup_plugins_dir_success():
    mock_env = Environment(config={'plugins_dir': '/some/directory'}, stderr=None)
    with patch('httpie.manager.tasks.plugins.os.makedirs') as mock_makedirs:
        mock_makedirs.return_value = None  # makedirs returns None on success
        installer = PluginInstaller(env=mock_env, debug=True)
        assert hasattr(installer, 'dir'), "PluginInstaller should have a dir attribute"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_manager_tasks_plugins_PluginInstaller___init___1_edge_cases
httpie/Test4DT_tests_codestral/test_httpie_manager_tasks_plugins_PluginInstaller___init___1_edge_cases.py:5:0: E0401: Unable to import 'httpie.environment' (import-error)
httpie/Test4DT_tests_codestral/test_httpie_manager_tasks_plugins_PluginInstaller___init___1_edge_cases.py:5:0: E0611: No name 'environment' in module 'httpie' (no-name-in-module)


"""