
import pytest
from unittest.mock import patch, MagicMock
from httpie.manager.tasks.plugins import PluginInstaller

@pytest.fixture
def mock_environment():
    env = MagicMock()
    env.config.plugins_dir = "/path/to/plugins"
    return env

def test_valid_input(mock_environment):
    with patch('httpie.manager.tasks.plugins.Path', autospec=True) as mock_path:
        # Mock the Path object to have a mkdir method
        mock_path_instance = mock_path.return_value
        mock_path_instance.mkdir.side_effect = FileExistsError("Directory already exists")
        
        installer = PluginInstaller(env=mock_environment)
        assert hasattr(installer, 'dir')

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

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_manager_tasks_plugins_PluginInstaller__uninstall_2_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

mock_environment = <MagicMock id='140640867289872'>

    def test_valid_input(mock_environment):
        with patch('httpie.manager.tasks.plugins.Path', autospec=True) as mock_path:
            # Mock the Path object to have a mkdir method
            mock_path_instance = mock_path.return_value
            mock_path_instance.mkdir.side_effect = FileExistsError("Directory already exists")
    
>           installer = PluginInstaller(env=mock_environment)

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_manager_tasks_plugins_PluginInstaller__uninstall_2_test_valid_input.py:18: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
httpie/httpie/manager/tasks/plugins.py:28: in __init__
    self.setup_plugins_dir()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <httpie.manager.tasks.plugins.PluginInstaller object at 0x7fe9817749d0>

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
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_manager_tasks_plugins_PluginInstaller__uninstall_2_test_valid_input.py::test_valid_input
============================== 1 failed in 0.33s ===============================
"""