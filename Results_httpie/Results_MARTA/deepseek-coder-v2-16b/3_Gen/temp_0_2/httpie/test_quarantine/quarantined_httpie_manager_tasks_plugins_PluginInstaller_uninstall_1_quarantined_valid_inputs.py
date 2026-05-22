
import pytest
from unittest.mock import patch, MagicMock
from httpie.manager.tasks.plugins import PluginInstaller, ExitStatus
from pathlib import Path

@pytest.fixture
def setup_env():
    env = MagicMock()
    env.config.plugins_dir = Path("/some/directory")
    return env

@patch('httpie.manager.tasks.plugins.os.makedirs')
def test_setup_plugins_dir(mock_makedirs, setup_env):
    mock_makedirs.side_effect = OSError("Permission denied")
    installer = PluginInstaller(env=setup_env)
    
    with pytest.raises(OSError):
        installer.setup_plugins_dir()

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

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_manager_tasks_plugins_PluginInstaller_uninstall_1_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
____________________________ test_setup_plugins_dir ____________________________

self = PosixPath('/some/directory'), mode = 511, parents = True, exist_ok = True

    def mkdir(self, mode=0o777, parents=False, exist_ok=False):
        """
        Create a new directory at this given path.
        """
        try:
>           os.mkdir(self, mode)
E           FileNotFoundError: [Errno 2] No such file or directory: '/some/directory'

/usr/local/lib/python3.11/pathlib.py:1116: FileNotFoundError

During handling of the above exception, another exception occurred:

mock_makedirs = <MagicMock name='makedirs' id='140526955074448'>
setup_env = <MagicMock id='140526981022992'>

    @patch('httpie.manager.tasks.plugins.os.makedirs')
    def test_setup_plugins_dir(mock_makedirs, setup_env):
        mock_makedirs.side_effect = OSError("Permission denied")
>       installer = PluginInstaller(env=setup_env)

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_manager_tasks_plugins_PluginInstaller_uninstall_1_test_valid_inputs.py:16: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
httpie/httpie/manager/tasks/plugins.py:28: in __init__
    self.setup_plugins_dir()
httpie/httpie/manager/tasks/plugins.py:32: in setup_plugins_dir
    self.dir.mkdir(
/usr/local/lib/python3.11/pathlib.py:1120: in mkdir
    self.parent.mkdir(parents=True, exist_ok=True)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = PosixPath('/some'), mode = 511, parents = True, exist_ok = True

    def mkdir(self, mode=0o777, parents=False, exist_ok=False):
        """
        Create a new directory at this given path.
        """
        try:
>           os.mkdir(self, mode)
E           OSError: [Errno 30] Read-only file system: '/some'

/usr/local/lib/python3.11/pathlib.py:1116: OSError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_manager_tasks_plugins_PluginInstaller_uninstall_1_test_valid_inputs.py::test_setup_plugins_dir
============================== 1 failed in 0.33s ===============================
"""