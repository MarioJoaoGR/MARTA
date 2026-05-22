
import unittest
from unittest.mock import patch, MagicMock
from httpie.manager.tasks.plugins import PluginInstaller, ExitStatus
from httpie.environment import Environment

class TestPluginInstallerUninstall(unittest.TestCase):
    def setUp(self):
        self.env = Environment()
        self.installer = PluginInstaller(env=self.env)

    @patch('httpie.manager.tasks.plugins._uninstall')
    def test_uninstall_success(self, mock_uninstall):
        # Mock the uninstall method to return ExitStatus.SUCCESS for all targets
        mock_uninstall.return_value = ExitStatus.SUCCESS
        
        # Define a list of successful uninstall targets
        targets = ["plugin1", "plugin2", "plugin3"]
        
        # Call the uninstall method
        result = self.installer.uninstall(targets)
        
        # Assert that all targets were successfully uninstalled
        self.assertEqual(result, ExitStatus.SUCCESS)
        mock_uninstall.assert_called()

    @patch('httpie.manager.tasks.plugins._uninstall')
    def test_uninstall_failure(self, mock_uninstall):
        # Mock the uninstall method to return a non-success ExitStatus for one target
        mock_uninstall.side_effect = [ExitStatus.FAILURE, ExitStatus.SUCCESS]
        
        # Define a list of targets including one that will fail
        targets = ["plugin1", "plugin2", "plugin3"]
        
        # Call the uninstall method
        result = self.installer.uninstall(targets)
        
        # Assert that at least one target failed to uninstall
        self.assertEqual(result, ExitStatus.FAILURE)
        mock_uninstall.assert_called()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_manager_tasks_plugins_PluginInstaller_uninstall_2_test_edge_cases
httpie/Test4DT_tests_codestral/test_httpie_manager_tasks_plugins_PluginInstaller_uninstall_2_test_edge_cases.py:5:0: E0401: Unable to import 'httpie.environment' (import-error)
httpie/Test4DT_tests_codestral/test_httpie_manager_tasks_plugins_PluginInstaller_uninstall_2_test_edge_cases.py:5:0: E0611: No name 'environment' in module 'httpie' (no-name-in-module)
httpie/Test4DT_tests_codestral/test_httpie_manager_tasks_plugins_PluginInstaller_uninstall_2_test_edge_cases.py:30:38: E1101: Class 'ExitStatus' has no 'FAILURE' member (no-member)
httpie/Test4DT_tests_codestral/test_httpie_manager_tasks_plugins_PluginInstaller_uninstall_2_test_edge_cases.py:39:33: E1101: Class 'ExitStatus' has no 'FAILURE' member (no-member)


"""