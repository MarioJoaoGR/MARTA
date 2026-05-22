
import pytest
from httpie.plugins.manager import PluginManager

@pytest.fixture
def setup_plugin_manager():
    manager = PluginManager()
    with patch('httpie.plugins.manager.PluginManager.get_transport_plugins', return_value=['transport1', 'transport2']):
        with patch('httpie.plugins.manager.PluginManager.get_auth_plugins', return_value=['auth1', 'auth2']):
            with patch('httpie.plugins.manager.PluginManager.get_converters', return_value=['converter1', 'converter2']):
                with patch('httpie.plugins.manager.PluginManager.get_formatters', return_value=['formatter1', 'formatter2']):
                    yield manager

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_plugins_manager_PluginManager___str___0_test_edge_cases
httpie/Test4DT_tests_codestral/test_httpie_plugins_manager_PluginManager___str___0_test_edge_cases.py:8:9: E0602: Undefined variable 'patch' (undefined-variable)
httpie/Test4DT_tests_codestral/test_httpie_plugins_manager_PluginManager___str___0_test_edge_cases.py:9:13: E0602: Undefined variable 'patch' (undefined-variable)
httpie/Test4DT_tests_codestral/test_httpie_plugins_manager_PluginManager___str___0_test_edge_cases.py:10:17: E0602: Undefined variable 'patch' (undefined-variable)
httpie/Test4DT_tests_codestral/test_httpie_plugins_manager_PluginManager___str___0_test_edge_cases.py:11:21: E0602: Undefined variable 'patch' (undefined-variable)


"""