
import pytest
from httpie.manager.tasks.plugins import PluginInstaller
from unittest.mock import patch, MagicMock

@pytest.fixture(autouse=True)
def mock_environment():
    env = MagicMock()
    env.config.plugins_dir = "/path/to/plugins"
    yield env

@pytest.mark.parametrize("targets", [["plugin1-1.0"], ["plugin2-2.0"]])
def test_valid_inputs(mock_environment, targets):
    with patch('httpie.manager.tasks.plugins.get_site_paths', return_value=["/path/to/plugins/dist-info", "/path/to/plugins/egg-info"]):
        installer = PluginInstaller(env=mock_environment)
        installer._clear_metadata(targets)

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

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_manager_tasks_plugins_PluginInstaller__clear_metadata_1_test_valid_inputs.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_________________________ test_valid_inputs[targets0] __________________________

mock_environment = <MagicMock id='140462500838480'>, targets = ['plugin1-1.0']

    @pytest.mark.parametrize("targets", [["plugin1-1.0"], ["plugin2-2.0"]])
    def test_valid_inputs(mock_environment, targets):
        with patch('httpie.manager.tasks.plugins.get_site_paths', return_value=["/path/to/plugins/dist-info", "/path/to/plugins/egg-info"]):
>           installer = PluginInstaller(env=mock_environment)

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_manager_tasks_plugins_PluginInstaller__clear_metadata_1_test_valid_inputs.py:15: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
httpie/httpie/manager/tasks/plugins.py:28: in __init__
    self.setup_plugins_dir()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <httpie.manager.tasks.plugins.PluginInstaller object at 0x7fbff97828d0>

    def setup_plugins_dir(self) -> None:
        try:
>           self.dir.mkdir(
                exist_ok=True,
                parents=True
            )
E           AttributeError: 'str' object has no attribute 'mkdir'

httpie/httpie/manager/tasks/plugins.py:32: AttributeError
_________________________ test_valid_inputs[targets1] __________________________

mock_environment = <MagicMock id='140462511658256'>, targets = ['plugin2-2.0']

    @pytest.mark.parametrize("targets", [["plugin1-1.0"], ["plugin2-2.0"]])
    def test_valid_inputs(mock_environment, targets):
        with patch('httpie.manager.tasks.plugins.get_site_paths', return_value=["/path/to/plugins/dist-info", "/path/to/plugins/egg-info"]):
>           installer = PluginInstaller(env=mock_environment)

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_manager_tasks_plugins_PluginInstaller__clear_metadata_1_test_valid_inputs.py:15: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
httpie/httpie/manager/tasks/plugins.py:28: in __init__
    self.setup_plugins_dir()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <httpie.manager.tasks.plugins.PluginInstaller object at 0x7fbffa3a7150>

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
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_manager_tasks_plugins_PluginInstaller__clear_metadata_1_test_valid_inputs.py::test_valid_inputs[targets0]
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_manager_tasks_plugins_PluginInstaller__clear_metadata_1_test_valid_inputs.py::test_valid_inputs[targets1]
============================== 2 failed in 0.33s ===============================
"""