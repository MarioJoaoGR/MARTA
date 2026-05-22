
import pytest
from unittest.mock import patch, MagicMock
from httpie.plugins.manager.tasks.plugins import PluginInstaller
from httpie.environment import Environment
from argparse import Namespace
from enum import Enum

class ExitStatus(Enum):
    SUCCESS = 0
    FAILURE = 1

def test_run_with_install_action():
    env = MagicMock()
    installer = PluginInstaller(env=env, debug=True)
    args = Namespace(targets=['plugin1', 'plugin2'])
    
    with patch('httpie.plugins.manager.tasks.plugins.PluginInstaller.install') as mock_install:
        mock_install.return_value = ExitStatus.SUCCESS
        result = installer.run('install', args)
        
        assert result == ExitStatus.SUCCESS
        mock_install.assert_called_once_with(['plugin1', 'plugin2'])

def test_run_with_upgrade_action():
    env = MagicMock()
    installer = PluginInstaller(env=env, debug=True)
    args = Namespace(targets=['plugin1', 'plugin2'])
    
    with patch('httpie.plugins.manager.tasks.plugins.PluginInstaller.upgrade') as mock_upgrade:
        mock_upgrade.return_value = ExitStatus.SUCCESS
        result = installer.run('upgrade', args)
        
        assert result == ExitStatus.SUCCESS
        mock_upgrade.assert_called_once_with(['plugin1', 'plugin2'])

def test_run_with_uninstall_action():
    env = MagicMock()
    installer = PluginInstaller(env=env, debug=True)
    args = Namespace(targets=['plugin1', 'plugin2'])
    
    with patch('httpie.plugins.manager.tasks.plugins.PluginInstaller.uninstall') as mock_uninstall:
        mock_uninstall.return_value = ExitStatus.SUCCESS
        result = installer.run('uninstall', args)
        
        assert result == ExitStatus.SUCCESS
        mock_uninstall.assert_called_once_with(['plugin1', 'plugin2'])

def test_run_with_list_action():
    env = MagicMock()
    installer = PluginInstaller(env=env, debug=True)
    
    with patch('httpie.plugins.manager.tasks.plugins.PluginInstaller.list') as mock_list:
        mock_list.return_value = None
        result = installer.run('list', Namespace())
        
        assert result == ExitStatus.SUCCESS
        mock_list.assert_called_once()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_manager_tasks_plugins_PluginInstaller_run_0_test_error_case
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_manager_tasks_plugins_PluginInstaller_run_0_test_error_case.py:4:0: E0401: Unable to import 'httpie.plugins.manager.tasks.plugins' (import-error)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_manager_tasks_plugins_PluginInstaller_run_0_test_error_case.py:4:0: E0611: No name 'tasks' in module 'httpie.plugins.manager' (no-name-in-module)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_manager_tasks_plugins_PluginInstaller_run_0_test_error_case.py:5:0: E0401: Unable to import 'httpie.environment' (import-error)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_manager_tasks_plugins_PluginInstaller_run_0_test_error_case.py:5:0: E0611: No name 'environment' in module 'httpie' (no-name-in-module)


"""