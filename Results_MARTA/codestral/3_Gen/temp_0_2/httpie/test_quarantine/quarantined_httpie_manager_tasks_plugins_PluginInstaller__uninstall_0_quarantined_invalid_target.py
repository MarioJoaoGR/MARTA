
import unittest
from unittest.mock import patch, MagicMock
from httpie.manager.tasks.plugins import PluginInstaller, ExitStatus
import importlib_metadata
import os
from pathlib import Path
from contextlib import suppress

class TestPluginInstallerUninstall(unittest.TestCase):
    def setUp(self):
        self.env = MagicMock()
        self.installer = PluginInstaller(env=self.env)

    @patch('importlib_metadata.distribution')
    @patch('os.unlink')
    @patch('pathlib.Path.rmdir')
    def test_uninstall_invalid_target(self, mock_rmdir, mock_unlink, mock_distribution):
        # Mock the distribution to raise PackageNotFoundError
        mock_distribution.side_effect = importlib_metadata.PackageNotFoundError()

        result = self.installer._uninstall("plugin_name")
        self.assertIsNone(result)
        self.env.stdout.write.assert_called_with('Successfully uninstalled plugin_name\n')

    @patch('importlib_metadata.distribution')
    @patch('os.unlink')
    @patch('pathlib.Path.rmdir')
    def test_uninstall_package_not_installed_through_httpie(self, mock_rmdir, mock_unlink, mock_distribution):
        # Mock the distribution to return a Path object with self.dir not in its parents
        base_dir = Path('/some/other/directory')
        mock_distribution.locate_file.return_value = base_dir / 'plugin_name'
        mock_distribution.files = None

        result = self.installer._uninstall("plugin_name")
        self.assertIsNone(result)
        self.env.stdout.write.assert_not_called()

    @patch('importlib_metadata.distribution')
    @patch('os.unlink')
    @patch('pathlib.Path.rmdir')
    def test_uninstall_failure(self, mock_rmdir, mock_unlink, mock_distribution):
        # Mock the distribution to return a Path object with self.dir in its parents
        base_dir = Path('/some/directory') / 'httpie' / 'plugins'
        mock_distribution.locate_file.return_value = base_dir / 'plugin_name'
        mock_distribution.files = ['file1', 'file2']

        # Mock os.unlink to raise FileNotFoundError for one of the files
        mock_unlink.side_effect = [None, FileNotFoundError()]

        result = self.installer._uninstall("plugin_name")
        self.assertIsNone(result)
        self.env.stdout.write.assert_not_called()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

httpie/Test4DT_tests_codestral/test_httpie_manager_tasks_plugins_PluginInstaller__uninstall_0_test_invalid_target.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_____________ TestPluginInstallerUninstall.test_uninstall_failure ______________

self = <Test4DT_tests_codestral.test_httpie_manager_tasks_plugins_PluginInstaller__uninstall_0_test_invalid_target.TestPluginInstallerUninstall testMethod=test_uninstall_failure>
mock_rmdir = <MagicMock name='rmdir' id='139814741762704'>
mock_unlink = <MagicMock name='unlink' id='139814741770960'>
mock_distribution = <MagicMock name='distribution' id='139814741776272'>

    @patch('importlib_metadata.distribution')
    @patch('os.unlink')
    @patch('pathlib.Path.rmdir')
    def test_uninstall_failure(self, mock_rmdir, mock_unlink, mock_distribution):
        # Mock the distribution to return a Path object with self.dir in its parents
        base_dir = Path('/some/directory') / 'httpie' / 'plugins'
        mock_distribution.locate_file.return_value = base_dir / 'plugin_name'
        mock_distribution.files = ['file1', 'file2']
    
        # Mock os.unlink to raise FileNotFoundError for one of the files
        mock_unlink.side_effect = [None, FileNotFoundError()]
    
        result = self.installer._uninstall("plugin_name")
>       self.assertIsNone(result)
E       AssertionError: <ExitStatus.ERROR: 1> is not None

httpie/Test4DT_tests_codestral/test_httpie_manager_tasks_plugins_PluginInstaller__uninstall_0_test_invalid_target.py:52: AssertionError
__________ TestPluginInstallerUninstall.test_uninstall_invalid_target __________

self = <Test4DT_tests_codestral.test_httpie_manager_tasks_plugins_PluginInstaller__uninstall_0_test_invalid_target.TestPluginInstallerUninstall testMethod=test_uninstall_invalid_target>
mock_rmdir = <MagicMock name='rmdir' id='139814752356112'>
mock_unlink = <MagicMock name='unlink' id='139814749461840'>
mock_distribution = <MagicMock name='distribution' id='139814753866256'>

    @patch('importlib_metadata.distribution')
    @patch('os.unlink')
    @patch('pathlib.Path.rmdir')
    def test_uninstall_invalid_target(self, mock_rmdir, mock_unlink, mock_distribution):
        # Mock the distribution to raise PackageNotFoundError
        mock_distribution.side_effect = importlib_metadata.PackageNotFoundError()
    
        result = self.installer._uninstall("plugin_name")
>       self.assertIsNone(result)
E       AssertionError: <ExitStatus.ERROR: 1> is not None

httpie/Test4DT_tests_codestral/test_httpie_manager_tasks_plugins_PluginInstaller__uninstall_0_test_invalid_target.py:23: AssertionError
_ TestPluginInstallerUninstall.test_uninstall_package_not_installed_through_httpie _

self = <Test4DT_tests_codestral.test_httpie_manager_tasks_plugins_PluginInstaller__uninstall_0_test_invalid_target.TestPluginInstallerUninstall testMethod=test_uninstall_package_not_installed_through_httpie>
mock_rmdir = <MagicMock name='rmdir' id='139814742135376'>
mock_unlink = <MagicMock name='unlink' id='139814742140880'>
mock_distribution = <MagicMock name='distribution' id='139814742145872'>

    @patch('importlib_metadata.distribution')
    @patch('os.unlink')
    @patch('pathlib.Path.rmdir')
    def test_uninstall_package_not_installed_through_httpie(self, mock_rmdir, mock_unlink, mock_distribution):
        # Mock the distribution to return a Path object with self.dir not in its parents
        base_dir = Path('/some/other/directory')
        mock_distribution.locate_file.return_value = base_dir / 'plugin_name'
        mock_distribution.files = None
    
        result = self.installer._uninstall("plugin_name")
>       self.assertIsNone(result)
E       AssertionError: <ExitStatus.ERROR: 1> is not None

httpie/Test4DT_tests_codestral/test_httpie_manager_tasks_plugins_PluginInstaller__uninstall_0_test_invalid_target.py:36: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_manager_tasks_plugins_PluginInstaller__uninstall_0_test_invalid_target.py::TestPluginInstallerUninstall::test_uninstall_failure
FAILED httpie/Test4DT_tests_codestral/test_httpie_manager_tasks_plugins_PluginInstaller__uninstall_0_test_invalid_target.py::TestPluginInstallerUninstall::test_uninstall_invalid_target
FAILED httpie/Test4DT_tests_codestral/test_httpie_manager_tasks_plugins_PluginInstaller__uninstall_0_test_invalid_target.py::TestPluginInstallerUninstall::test_uninstall_package_not_installed_through_httpie
============================== 3 failed in 0.29s ===============================
"""