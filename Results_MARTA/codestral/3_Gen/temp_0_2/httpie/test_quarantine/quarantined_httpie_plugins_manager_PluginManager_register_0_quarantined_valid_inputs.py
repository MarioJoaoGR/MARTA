
import pytest
from unittest.mock import patch, MagicMock
from httpie.plugins.manager import PluginManager

class ExamplePlugin:
    pass

@patch('httpie.plugins.manager.PluginManager')
def test_register_valid_inputs(MockPluginManager):
    # Arrange
    plugin_manager = MockPluginManager()
    
    # Act
    plugin_manager.register(ExamplePlugin)
    
    # Assert
    assert ExamplePlugin in plugin_manager._registered_plugins

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

httpie/Test4DT_tests_codestral/test_httpie_plugins_manager_PluginManager_register_0_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
__________________________ test_register_valid_inputs __________________________

MockPluginManager = <MagicMock name='PluginManager' id='139698154185616'>

    @patch('httpie.plugins.manager.PluginManager')
    def test_register_valid_inputs(MockPluginManager):
        # Arrange
        plugin_manager = MockPluginManager()
    
        # Act
        plugin_manager.register(ExamplePlugin)
    
        # Assert
>       assert ExamplePlugin in plugin_manager._registered_plugins
E       AssertionError: assert ExamplePlugin in <MagicMock name='PluginManager()._registered_plugins' id='139698154321872'>
E        +  where <MagicMock name='PluginManager()._registered_plugins' id='139698154321872'> = <MagicMock name='PluginManager()' id='139698154191184'>._registered_plugins

httpie/Test4DT_tests_codestral/test_httpie_plugins_manager_PluginManager_register_0_test_valid_inputs.py:18: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_plugins_manager_PluginManager_register_0_test_valid_inputs.py::test_register_valid_inputs
============================== 1 failed in 0.11s ===============================
"""