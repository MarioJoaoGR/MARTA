
from httpie.manager.tasks.plugins import PluginInstaller
from unittest.mock import patch, MagicMock
import pytest

@patch('httpie.manager.tasks.plugins.Environment')
def test_init(mock_env):
    # Arrange
    mock_env = mock_env.return_value
    mock_env.config.plugins_dir = "mocked_plugins_dir"
    
    # Act
    installer = PluginInstaller(env=mock_env)
    
    # Assert
    assert hasattr(installer, 'env')
    assert hasattr(installer, 'dir')
    assert hasattr(installer, 'debug')
    assert installer.dir == "mocked_plugins_dir"

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

httpie/Test4DT_tests_codestral/test_httpie_manager_tasks_plugins_PluginInstaller___init___4_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
__________________________________ test_init ___________________________________

mock_env = <MagicMock name='Environment()' id='140028813566160'>

    @patch('httpie.manager.tasks.plugins.Environment')
    def test_init(mock_env):
        # Arrange
        mock_env = mock_env.return_value
        mock_env.config.plugins_dir = "mocked_plugins_dir"
    
        # Act
>       installer = PluginInstaller(env=mock_env)

httpie/Test4DT_tests_codestral/test_httpie_manager_tasks_plugins_PluginInstaller___init___4_test_edge_cases.py:13: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
httpie/httpie/manager/tasks/plugins.py:28: in __init__
    self.setup_plugins_dir()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <httpie.manager.tasks.plugins.PluginInstaller object at 0x7f5b006d7750>

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
FAILED httpie/Test4DT_tests_codestral/test_httpie_manager_tasks_plugins_PluginInstaller___init___4_test_edge_cases.py::test_init
============================== 1 failed in 0.30s ===============================
"""