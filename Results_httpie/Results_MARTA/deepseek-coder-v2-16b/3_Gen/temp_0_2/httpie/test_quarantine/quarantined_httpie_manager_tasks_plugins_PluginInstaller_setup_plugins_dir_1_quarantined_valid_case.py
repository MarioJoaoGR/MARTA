
from unittest.mock import patch, MagicMock
import pytest
from httpie.manager.tasks.plugins import PluginInstaller

class TestPluginInstaller:
    @patch('httpie.manager.tasks.plugins.Environment')
    def test_setup_plugins_dir_valid_case(self, MockEnvironment):
        # Arrange
        mock_env = MockEnvironment.return_value
        mock_env.config.plugins_dir = MagicMock()
        installer = PluginInstaller(env=mock_env, debug=True)
    
        # Act
        with patch('pathlib.Path.mkdir') as mkdir_mock:
            mkdir_mock.side_effect = OSError("Permission denied")
            try:
                installer.setup_plugins_dir()
            except OSError:
                pass  # Expected exception, so we just pass
    
        # Assert
        mock_env.config.plugins_dir.mkdir.assert_called_once_with(exist_ok=True, parents=True)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_manager_tasks_plugins_PluginInstaller_setup_plugins_dir_1_test_valid_case.py F [100%]

=================================== FAILURES ===================================
____________ TestPluginInstaller.test_setup_plugins_dir_valid_case _____________

self = <test_httpie_manager_tasks_plugins_PluginInstaller_setup_plugins_dir_1_test_valid_case.TestPluginInstaller object at 0x7fa3307c3ed0>
MockEnvironment = <MagicMock name='Environment' id='140338878713296'>

    @patch('httpie.manager.tasks.plugins.Environment')
    def test_setup_plugins_dir_valid_case(self, MockEnvironment):
        # Arrange
        mock_env = MockEnvironment.return_value
        mock_env.config.plugins_dir = MagicMock()
        installer = PluginInstaller(env=mock_env, debug=True)
    
        # Act
        with patch('pathlib.Path.mkdir') as mkdir_mock:
            mkdir_mock.side_effect = OSError("Permission denied")
            try:
                installer.setup_plugins_dir()
            except OSError:
                pass  # Expected exception, so we just pass
    
        # Assert
>       mock_env.config.plugins_dir.mkdir.assert_called_once_with(exist_ok=True, parents=True)

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_manager_tasks_plugins_PluginInstaller_setup_plugins_dir_1_test_valid_case.py:23: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <MagicMock name='Environment().config.plugins_dir.mkdir' id='140338876349584'>
args = (), kwargs = {'exist_ok': True, 'parents': True}
msg = "Expected 'mkdir' to be called once. Called 2 times.\nCalls: [call(exist_ok=True, parents=True), call(exist_ok=True, parents=True)]."

    def assert_called_once_with(self, /, *args, **kwargs):
        """assert that the mock was called exactly once and that that call was
        with the specified arguments."""
        if not self.call_count == 1:
            msg = ("Expected '%s' to be called once. Called %s times.%s"
                   % (self._mock_name or 'mock',
                      self.call_count,
                      self._calls_repr()))
>           raise AssertionError(msg)
E           AssertionError: Expected 'mkdir' to be called once. Called 2 times.
E           Calls: [call(exist_ok=True, parents=True), call(exist_ok=True, parents=True)].

/usr/local/lib/python3.11/unittest/mock.py:950: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_manager_tasks_plugins_PluginInstaller_setup_plugins_dir_1_test_valid_case.py::TestPluginInstaller::test_setup_plugins_dir_valid_case
============================== 1 failed in 0.33s ===============================
"""