
import pytest
from unittest.mock import patch, MagicMock
from httpie.manager.tasks.plugins import PluginInstaller

@pytest.fixture
def mock_environment():
    env = MagicMock()
    env.config.plugins_dir = "/tmp/test_plugins"
    return env

def test_invalid_input(mock_environment):
    with patch('httpie.manager.tasks.plugins.shutil', autospec=True) as shutil_mock:
        with pytest.raises(OSError):
            installer = PluginInstaller(env=mock_environment, debug=True)

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

httpie/Test4DT_tests_codestral/test_httpie_manager_tasks_plugins_PluginInstaller__clear_metadata_0_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

mock_environment = <MagicMock id='139804972539600'>

    def test_invalid_input(mock_environment):
        with patch('httpie.manager.tasks.plugins.shutil', autospec=True) as shutil_mock:
            with pytest.raises(OSError):
>               installer = PluginInstaller(env=mock_environment, debug=True)

httpie/Test4DT_tests_codestral/test_httpie_manager_tasks_plugins_PluginInstaller__clear_metadata_0_test_invalid_input.py:15: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
httpie/httpie/manager/tasks/plugins.py:28: in __init__
    self.setup_plugins_dir()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <httpie.manager.tasks.plugins.PluginInstaller object at 0x7f26e0647950>

    def setup_plugins_dir(self) -> None:
        try:
>           self.dir.mkdir(
                exist_ok=True,
                parents=True
            )
E           AttributeError: 'str' object has no attribute 'mkdir'

httpie/httpie/manager/tasks/plugins.py:32: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_manager_tasks_plugins_PluginInstaller__clear_metadata_0_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.25s ===============================
"""