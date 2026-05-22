
from httpie.manager.tasks.plugins import PluginInstaller
from unittest.mock import patch
import pytest

class TestPluginInstallerInit:
    @patch('httpie.manager.tasks.plugins.Environment')
    def test_init(self, MockEnvClass):
        # Arrange
        mock_env = MockEnvClass.return_value
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

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_manager_tasks_plugins_PluginInstaller___init___3_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
______________________ TestPluginInstallerInit.test_init _______________________

self = <test_httpie_manager_tasks_plugins_PluginInstaller___init___3_test_edge_cases.TestPluginInstallerInit object at 0x7f6a4dc02290>
MockEnvClass = <MagicMock name='Environment' id='140094538562832'>

    @patch('httpie.manager.tasks.plugins.Environment')
    def test_init(self, MockEnvClass):
        # Arrange
        mock_env = MockEnvClass.return_value
        mock_env.config.plugins_dir = "mocked_plugins_dir"
    
        # Act
>       installer = PluginInstaller(env=mock_env)

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_manager_tasks_plugins_PluginInstaller___init___3_test_edge_cases.py:14: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
httpie/httpie/manager/tasks/plugins.py:28: in __init__
    self.setup_plugins_dir()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <httpie.manager.tasks.plugins.PluginInstaller object at 0x7f6a4dc02a50>

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
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_manager_tasks_plugins_PluginInstaller___init___3_test_edge_cases.py::TestPluginInstallerInit::test_init
============================== 1 failed in 0.31s ===============================
"""