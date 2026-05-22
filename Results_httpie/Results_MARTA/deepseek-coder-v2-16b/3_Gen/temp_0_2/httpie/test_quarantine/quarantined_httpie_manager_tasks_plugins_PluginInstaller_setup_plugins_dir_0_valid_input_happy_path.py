
import pytest
from unittest.mock import patch, MagicMock
from httpie.manager.tasks.plugins import PluginInstaller
from pathlib import Path

@pytest.fixture
def valid_env():
    env = MagicMock()
    env.config.plugins_dir = Path('/some/directory')
    return env

def test_setup_plugins_dir_happy_path(valid_env):
    with patch('httpie.manager.tasks.plugins.Path.mkdir') as mkdir_mock:
        mkdir_mock.return_value = None
        installer = PluginInstaller(env=valid_env, debug=False)
        assert isinstance(installer.dir, Path)
        installer.setup_plugins_dir()
        mkdir_mock.assert_called_once_with(exist_ok=True, parents=True)

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

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_manager_tasks_plugins_PluginInstaller_setup_plugins_dir_0_valid_input_happy_path.py F [100%]

=================================== FAILURES ===================================
______________________ test_setup_plugins_dir_happy_path _______________________

valid_env = <MagicMock id='140155063328464'>

    def test_setup_plugins_dir_happy_path(valid_env):
        with patch('httpie.manager.tasks.plugins.Path.mkdir') as mkdir_mock:
            mkdir_mock.return_value = None
            installer = PluginInstaller(env=valid_env, debug=False)
            assert isinstance(installer.dir, Path)
            installer.setup_plugins_dir()
>           mkdir_mock.assert_called_once_with(exist_ok=True, parents=True)

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_manager_tasks_plugins_PluginInstaller_setup_plugins_dir_0_valid_input_happy_path.py:19: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <MagicMock name='mkdir' id='140155045941968'>, args = ()
kwargs = {'exist_ok': True, 'parents': True}
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
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_manager_tasks_plugins_PluginInstaller_setup_plugins_dir_0_valid_input_happy_path.py::test_setup_plugins_dir_happy_path
============================== 1 failed in 0.24s ===============================
"""