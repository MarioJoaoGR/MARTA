
import unittest
from unittest.mock import patch, MagicMock
from httpie.manager.tasks.plugins import PluginInstaller, ExitStatus

class TestPluginInstallerUninstall(unittest.TestCase):
    @patch('httpie.manager.tasks.plugins.os')
    def test_uninstall_success(self, mock_os):
        # Mock the environment and plugin installer
        env = MagicMock()
        env.config.plugins_dir = "/path/to/plugins"
        installer = PluginInstaller(env)
        
        # Mock successful uninstallation
        def mock_uninstall(target):
            return ExitStatus.SUCCESS
        
        with patch('httpie.manager.tasks.plugins.PluginInstaller._uninstall', side_effect=mock_uninstall):
            result = installer.uninstall(["plugin1", "plugin2"])
            
        self.assertEqual(result, ExitStatus.SUCCESS)

    @patch('httpie.manager.tasks.plugins.os')
    def test_uninstall_failure(self, mock_os):
        # Mock the environment and plugin installer
        env = MagicMock()
        env.config.plugins_dir = "/path/to/plugins"
        installer = PluginInstaller(env)
        
        # Mock failed uninstallation
        def mock_uninstall(target):
            if target == "plugin1":
                return ExitStatus.SUCCESS
            else:
                return ExitStatus.FAILURE
        
        with patch('httpie.manager.tasks.plugins.PluginInstaller._uninstall', side_effect=mock_uninstall):
            result = installer.uninstall(["plugin1", "plugin2"])
            
        self.assertEqual(result, ExitStatus.FAILURE)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_manager_tasks_plugins_PluginInstaller_uninstall_1_test_edge_cases
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_manager_tasks_plugins_PluginInstaller_uninstall_1_test_edge_cases.py:35:23: E1101: Class 'ExitStatus' has no 'FAILURE' member (no-member)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_manager_tasks_plugins_PluginInstaller_uninstall_1_test_edge_cases.py:40:33: E1101: Class 'ExitStatus' has no 'FAILURE' member (no-member)


"""