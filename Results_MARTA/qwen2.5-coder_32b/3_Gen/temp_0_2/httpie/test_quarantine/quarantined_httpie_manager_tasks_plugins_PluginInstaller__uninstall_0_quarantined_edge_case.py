
import unittest
from unittest.mock import patch, MagicMock
from httpie.manager.tasks.plugins import PluginInstaller

class TestPluginInstallerUninstall(unittest.TestCase):
    @patch('httpie.manager.tasks.plugins.importlib_metadata')
    def test_uninstall_package_not_installed(self, mock_importlib_metadata):
        # Arrange
        installer = PluginInstaller(env=MagicMock(), debug=False)
        mock_importlib_metadata.distribution.side_effect = importlib_metadata.PackageNotFoundError()
        
        # Act
        result = installer._uninstall("non_existent_package")
        
        # Assert
        self.assertIsNone(result)
        installer.fail.assert_called_once_with('uninstall', 'non_existent_package', 'package is not installed')

    @patch('httpie.manager.tasks.plugins.os')
    @patch('httpie.manager.tasks.plugins.importlib_metadata')
    def test_uninstall_package_installed_in_wrong_location(self, mock_importlib_metadata, mock_os):
        # Arrange
        installer = PluginInstaller(env=MagicMock(), debug=False)
        distribution = MagicMock()
        distribution.locate_file = lambda x: Path('/wrong/location') / x
        distribution.files = ['file1', 'file2']
        mock_importlib_metadata.distribution.return_value = distribution
        
        # Act
        result = installer._uninstall("installed_package")
        
        # Assert
        self.assertIsNone(result)
        installer.fail.assert_called_once_with('uninstall', 'installed_package', 'package is not installed through httpie plugins interface')

    @patch('httpie.manager.tasks.plugins.os')
    @patch('httpie.manager.tasks.plugins.importlib_metadata')
    def test_uninstall_successful(self, mock_importlib_metadata, mock_os):
        # Arrange
        installer = PluginInstaller(env=MagicMock(), debug=False)
        distribution = MagicMock()
        distribution.locate_file = lambda x: Path('/correct/location') / x
        distribution.files = ['file1', 'file2']
        mock_importlib_metadata.distribution.return_value = distribution
        
        # Act
        result = installer._uninstall("installed_package")
        
        # Assert
        self.assertIsNone(result)
        mock_os.unlink.assert_any_call('/correct/location/file1')
        mock_os.unlink.assert_any_call('/correct/location/file2')
        installer.env.stdout.write.assert_called_once_with('Successfully uninstalled installed_package\n')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_manager_tasks_plugins_PluginInstaller__uninstall_0_test_edge_case
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_manager_tasks_plugins_PluginInstaller__uninstall_0_test_edge_case.py:11:59: E0602: Undefined variable 'importlib_metadata' (undefined-variable)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_manager_tasks_plugins_PluginInstaller__uninstall_0_test_edge_case.py:18:8: E1101: Method 'fail' has no 'assert_called_once_with' member (no-member)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_manager_tasks_plugins_PluginInstaller__uninstall_0_test_edge_case.py:26:45: E0602: Undefined variable 'Path' (undefined-variable)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_manager_tasks_plugins_PluginInstaller__uninstall_0_test_edge_case.py:35:8: E1101: Method 'fail' has no 'assert_called_once_with' member (no-member)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_manager_tasks_plugins_PluginInstaller__uninstall_0_test_edge_case.py:43:45: E0602: Undefined variable 'Path' (undefined-variable)


"""