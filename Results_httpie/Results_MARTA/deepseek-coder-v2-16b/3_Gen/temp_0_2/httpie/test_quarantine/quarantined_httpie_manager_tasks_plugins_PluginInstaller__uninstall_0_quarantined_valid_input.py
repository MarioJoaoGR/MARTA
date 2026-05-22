
import pytest
from unittest.mock import patch, MagicMock
from httpie.manager.tasks.plugins import PluginInstaller

@pytest.fixture
def mock_env():
    env = MagicMock()
    env.config.plugins_dir = "/path/to/plugins"
    return env

def test_valid_input(mock_env):
    with patch('httpie.manager.tasks.plugins.Path', spec=True) as mock_path:
        # Mock the Path object to have a mkdir method
        mock_dir = mock_path.return_value
        mock_dir.mkdir.side_effect = FileExistsError  # Ensure it raises FileExistsError if called again
        
        installer = PluginInstaller(env=mock_env, debug=True)
        with pytest.raises(FileExistsError):
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

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_manager_tasks_plugins_PluginInstaller__uninstall_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

mock_env = <MagicMock id='139658640721616'>

    def test_valid_input(mock_env):
        with patch('httpie.manager.tasks.plugins.Path', spec=True) as mock_path:
            # Mock the Path object to have a mkdir method
            mock_dir = mock_path.return_value
            mock_dir.mkdir.side_effect = FileExistsError  # Ensure it raises FileExistsError if called again
    
>           installer = PluginInstaller(env=mock_env, debug=True)

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_manager_tasks_plugins_PluginInstaller__uninstall_0_test_valid_input.py:18: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
httpie/httpie/manager/tasks/plugins.py:28: in __init__
    self.setup_plugins_dir()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <httpie.manager.tasks.plugins.PluginInstaller object at 0x7f04cfaa9510>

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
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_manager_tasks_plugins_PluginInstaller__uninstall_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.25s ===============================
"""