
import pytest
from unittest.mock import patch
from httpie.manager.tasks.plugins import PluginInstaller

@pytest.fixture
def setup_plugin_installer():
    env = type('Environment', (object,), {'config': type('Config', (object,), {'plugins_dir': '/tmp/plugins'}), 'stderr': type('Stderr', (object,), {'write': lambda _: None})()})()
    return PluginInstaller(env=env)

def test_setup_plugins_dir(setup_plugin_installer):
    with patch('pathlib.Path.mkdir') as mock_mkdir:
        mock_mkdir.side_effect = OSError("Permission denied")
        with pytest.raises(OSError):
            setup_plugin_installer.setup_plugins_dir()

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

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_manager_tasks_plugins_PluginInstaller_setup_plugins_dir_0_test_edge_case.py E [100%]

==================================== ERRORS ====================================
___________________ ERROR at setup of test_setup_plugins_dir ___________________

    @pytest.fixture
    def setup_plugin_installer():
        env = type('Environment', (object,), {'config': type('Config', (object,), {'plugins_dir': '/tmp/plugins'}), 'stderr': type('Stderr', (object,), {'write': lambda _: None})()})()
>       return PluginInstaller(env=env)

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_manager_tasks_plugins_PluginInstaller_setup_plugins_dir_0_test_edge_case.py:9: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
httpie/httpie/manager/tasks/plugins.py:28: in __init__
    self.setup_plugins_dir()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <httpie.manager.tasks.plugins.PluginInstaller object at 0x7f76d6fd4ed0>

    def setup_plugins_dir(self) -> None:
        try:
>           self.dir.mkdir(
                exist_ok=True,
                parents=True
            )
E           AttributeError: 'str' object has no attribute 'mkdir'

httpie/httpie/manager/tasks/plugins.py:32: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_manager_tasks_plugins_PluginInstaller_setup_plugins_dir_0_test_edge_case.py::test_setup_plugins_dir
=============================== 1 error in 0.27s ===============================
"""