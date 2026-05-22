
import pytest
from unittest.mock import patch, MagicMock
from httpie.manager.tasks.plugins import PluginInstaller

@pytest.fixture
def setup_plugin_installer():
    env = MagicMock()
    env.config.plugins_dir = "/some/directory"
    return PluginInstaller(env=env)

def test_setup_plugins_dir_success(setup_plugin_installer):
    with patch('httpie.manager.tasks.plugins.Path.mkdir') as mkdir_mock:
        mkdir_mock.return_value = None
        setup_plugin_installer.setup_plugins_dir()
        assert not mkdir_mock.called

def test_setup_plugins_dir_failure(setup_plugin_installer):
    with patch('httpie.manager.tasks.plugins.Path.mkdir', side_effect=OSError("Permission denied")):
        with pytest.raises(OSError, match="Couldn't create"):
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
collected 2 items

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_manager_tasks_plugins_PluginInstaller_setup_plugins_dir_0_invalid_input_error_handling.py E [ 50%]
E                                                                        [100%]

==================================== ERRORS ====================================
_______________ ERROR at setup of test_setup_plugins_dir_success _______________

    @pytest.fixture
    def setup_plugin_installer():
        env = MagicMock()
        env.config.plugins_dir = "/some/directory"
>       return PluginInstaller(env=env)

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_manager_tasks_plugins_PluginInstaller_setup_plugins_dir_0_invalid_input_error_handling.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
httpie/httpie/manager/tasks/plugins.py:28: in __init__
    self.setup_plugins_dir()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <httpie.manager.tasks.plugins.PluginInstaller object at 0x7f7c11e43590>

    def setup_plugins_dir(self) -> None:
        try:
>           self.dir.mkdir(
                exist_ok=True,
                parents=True
            )
E           AttributeError: 'str' object has no attribute 'mkdir'

httpie/httpie/manager/tasks/plugins.py:32: AttributeError
_______________ ERROR at setup of test_setup_plugins_dir_failure _______________

    @pytest.fixture
    def setup_plugin_installer():
        env = MagicMock()
        env.config.plugins_dir = "/some/directory"
>       return PluginInstaller(env=env)

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_manager_tasks_plugins_PluginInstaller_setup_plugins_dir_0_invalid_input_error_handling.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
httpie/httpie/manager/tasks/plugins.py:28: in __init__
    self.setup_plugins_dir()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <httpie.manager.tasks.plugins.PluginInstaller object at 0x7f7c11c7ff90>

    def setup_plugins_dir(self) -> None:
        try:
>           self.dir.mkdir(
                exist_ok=True,
                parents=True
            )
E           AttributeError: 'str' object has no attribute 'mkdir'

httpie/httpie/manager/tasks/plugins.py:32: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
ERROR httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_manager_tasks_plugins_PluginInstaller_setup_plugins_dir_0_invalid_input_error_handling.py::test_setup_plugins_dir_success
ERROR httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_manager_tasks_plugins_PluginInstaller_setup_plugins_dir_0_invalid_input_error_handling.py::test_setup_plugins_dir_failure
============================== 2 errors in 0.28s ===============================
"""