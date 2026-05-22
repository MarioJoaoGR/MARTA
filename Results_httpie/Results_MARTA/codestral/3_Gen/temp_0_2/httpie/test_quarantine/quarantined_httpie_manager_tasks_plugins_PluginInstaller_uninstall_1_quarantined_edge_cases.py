
import unittest
from unittest.mock import patch, MagicMock
from httpie.manager.tasks.plugins import PluginInstaller, ExitStatus
from httpie.environment import Environment

class TestPluginInstallerUninstall(unittest.TestCase):
    @patch('httpie.environment.Environment')
    def test_uninstall_success(self, MockEnvironment):
        # Arrange
        env = MockEnvironment.return_value
        installer = PluginInstaller(env=env)
        targets = ["plugin1", "plugin2"]
        
        # Act
        result = installer.uninstall(targets)
        
        # Assert
        self.assertEqual(result, ExitStatus.SUCCESS)
    
    @patch('httpie.environment.Environment')
    def test_uninstall_failure(self, MockEnvironment):
        # Arrange
        env = MockEnvironment.return_value
        installer = PluginInstaller(env=env)
        targets = ["plugin1", "plugin2"]
        
        # Act & Assert
        with patch('httpie.manager.tasks.plugins.PluginInstaller._uninstall', return_value=ExitStatus.FAILURE):
            result = installer.uninstall(targets)
            self.assertEqual(result, ExitStatus.FAILURE)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_manager_tasks_plugins_PluginInstaller_uninstall_1_test_edge_cases
httpie/Test4DT_tests_codestral/test_httpie_manager_tasks_plugins_PluginInstaller_uninstall_1_test_edge_cases.py:5:0: E0401: Unable to import 'httpie.environment' (import-error)
httpie/Test4DT_tests_codestral/test_httpie_manager_tasks_plugins_PluginInstaller_uninstall_1_test_edge_cases.py:5:0: E0611: No name 'environment' in module 'httpie' (no-name-in-module)
httpie/Test4DT_tests_codestral/test_httpie_manager_tasks_plugins_PluginInstaller_uninstall_1_test_edge_cases.py:29:91: E1101: Class 'ExitStatus' has no 'FAILURE' member (no-member)
httpie/Test4DT_tests_codestral/test_httpie_manager_tasks_plugins_PluginInstaller_uninstall_1_test_edge_cases.py:31:37: E1101: Class 'ExitStatus' has no 'FAILURE' member (no-member)


"""