
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
        # Mock _uninstall to return ExitStatus.SUCCESS for all targets
        mock_uninstall.return_value = ExitStatus.SUCCESS
        
        # Test uninstall with a list of successful uninstallations
        result = self.installer.uninstall(["plugin1", "plugin2"])
        self.assertEqual(result, ExitStatus.SUCCESS)

    @patch('httpie.manager.tasks.plugins._uninstall')
    def test_uninstall_failure(self, mock_uninstall):
        # Mock _uninstall to return ExitStatus.FAILURE for the first target and ExitStatus.SUCCESS for the second
        mock_uninstall.side_effect = [ExitStatus.FAILURE, ExitStatus.SUCCESS]
        
        # Test uninstall with a list that includes one failure
        result = self.installer.uninstall(["plugin1", "plugin2"])
        self.assertEqual(result, ExitStatus.FAILURE)

    @patch('httpie.manager.tasks.plugins._uninstall')
    def test_uninstall_all_failures(self, mock_uninstall):
        # Mock _uninstall to return ExitStatus.FAILURE for all targets
        mock_uninstall.return_value = ExitStatus.FAILURE
        
        # Test uninstall with a list that includes all failures
        result = self.installer.uninstall(["plugin1", "plugin2"])
        self.assertEqual(result, ExitStatus.FAILURE)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_manager_tasks_plugins_PluginInstaller_uninstall_0_test_edge_cases
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_manager_tasks_plugins_PluginInstaller_uninstall_0_test_edge_cases.py:5:0: E0401: Unable to import 'httpie.environment' (import-error)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_manager_tasks_plugins_PluginInstaller_uninstall_0_test_edge_cases.py:5:0: E0611: No name 'environment' in module 'httpie' (no-name-in-module)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_manager_tasks_plugins_PluginInstaller_uninstall_0_test_edge_cases.py:24:38: E1101: Class 'ExitStatus' has no 'FAILURE' member (no-member)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_manager_tasks_plugins_PluginInstaller_uninstall_0_test_edge_cases.py:28:33: E1101: Class 'ExitStatus' has no 'FAILURE' member (no-member)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_manager_tasks_plugins_PluginInstaller_uninstall_0_test_edge_cases.py:33:38: E1101: Class 'ExitStatus' has no 'FAILURE' member (no-member)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_manager_tasks_plugins_PluginInstaller_uninstall_0_test_edge_cases.py:37:33: E1101: Class 'ExitStatus' has no 'FAILURE' member (no-member)


"""