
import unittest
from unittest.mock import patch, MagicMock
from httpie.manager.tasks.plugins import PluginInstaller

class TestPluginInstallerUninstall(unittest.TestCase):
    @patch('httpie.manager.tasks.plugins.importlib_metadata')
    def test_uninstall_invalid_target(self, mock_importlib_metadata):
        # Mock the environment object
        env = MagicMock()
        installer = PluginInstaller(env)
        
        # Mock importlib_metadata to raise PackageNotFoundError
        mock_importlib_metadata.distribution.side_effect = importlib_metadata.PackageNotFoundError
        
        result = installer._uninstall("invalid_target")
        
        self.assertIsNone(result)
        mock_importlib_metadata.distribution.assert_called_once_with("invalid_target")
        env.stdout.write.assert_called_once_with('Successfully uninstalled invalid_target\n')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_manager_tasks_plugins_PluginInstaller__uninstall_0_test_invalid_target
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_manager_tasks_plugins_PluginInstaller__uninstall_0_test_invalid_target.py:14:59: E0602: Undefined variable 'importlib_metadata' (undefined-variable)


"""