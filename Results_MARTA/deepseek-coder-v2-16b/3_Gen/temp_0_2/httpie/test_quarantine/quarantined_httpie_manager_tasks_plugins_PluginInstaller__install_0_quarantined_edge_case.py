
import unittest
from unittest.mock import patch, MagicMock
from httpie.manager.tasks.plugins import PluginInstaller
from httpie.environment import Environment
from httpie.exitstatus import ExitStatus

class TestPluginInstaller(unittest.TestCase):
    def setUp(self):
        self.env = Environment()
        self.installer = PluginInstaller(env=self.env, debug=True)

    @patch('httpie.manager.tasks.plugins.run_pip')
    @patch('httpie.manager.tasks.plugins.PipError')
    def test_install_success(self, MockPipError, MockRunPip):
        # Mock successful pip run
        mock_stdout = b"Success output"
        MockRunPip.return_value = mock_stdout
        
        result = self.installer._install(['plugin1'])
        self.assertEqual(result[1], ExitStatus.SUCCESS)
        self.assertEqual(self.env.stdout.write.call_count, 1)
        self.env.stdout.write.assert_called_with(mock_stdout.decode())

    @patch('httpie.manager.tasks.plugins.run_pip')
    @patch('httpie.manager.tasks.plugins.PipError')
    def test_install_failure(self, MockPipError, MockRunPip):
        # Mock failed pip run
        mock_error = MagicMock()
        mock_error.stdout = b"Failure output"
        mock_error.stderr = b"ERROR: Failed to install plugin1"
        MockPipError.return_value = mock_error
        
        result = self.installer._install(['plugin1'])
        self.assertEqual(result[1], ExitStatus.ERROR)
        self.assertEqual(self.env.stdout.write.call_count, 1)
        self.env.stdout.write.assert_called_with("Failure output")
        if self.installer.debug:
            self.env.stderr.write.assert_called_with('Command failed: pip install plugin1')
            self.env.stderr.write.assert_called_with(textwrap.indent('  ', "ERROR: Failed to install plugin1"))

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_manager_tasks_plugins_PluginInstaller__install_0_test_edge_case
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_manager_tasks_plugins_PluginInstaller__install_0_test_edge_case.py:5:0: E0401: Unable to import 'httpie.environment' (import-error)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_manager_tasks_plugins_PluginInstaller__install_0_test_edge_case.py:5:0: E0611: No name 'environment' in module 'httpie' (no-name-in-module)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_manager_tasks_plugins_PluginInstaller__install_0_test_edge_case.py:6:0: E0401: Unable to import 'httpie.exitstatus' (import-error)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_manager_tasks_plugins_PluginInstaller__install_0_test_edge_case.py:6:0: E0611: No name 'exitstatus' in module 'httpie' (no-name-in-module)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_manager_tasks_plugins_PluginInstaller__install_0_test_edge_case.py:40:53: E0602: Undefined variable 'textwrap' (undefined-variable)


"""