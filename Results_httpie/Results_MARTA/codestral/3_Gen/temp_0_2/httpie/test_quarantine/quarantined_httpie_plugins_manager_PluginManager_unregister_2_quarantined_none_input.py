
import pytest
from httpie.plugins.manager import PluginManager

@pytest.fixture(scope="module")
def setup_plugin_manager():
    manager = PluginManager()
    yield manager  # Provide the fixture value here

def test_none_input(setup_plugin_manager):
    with pytest.raises(TypeError) as excinfo:
        setup_plugin_manager.unregister(None)  # Test unregistering a None input
    assert "Plugin must be a subclass of BasePlugin" in str(excinfo.value)

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

httpie/Test4DT_tests_codestral/test_httpie_plugins_manager_PluginManager_unregister_2_test_none_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_none_input ________________________________

setup_plugin_manager = <PluginManager {'adapters': [], 'auth': [], 'converters': [], 'formatters': []}>

    def test_none_input(setup_plugin_manager):
        with pytest.raises(TypeError) as excinfo:
>           setup_plugin_manager.unregister(None)  # Test unregistering a None input

httpie/Test4DT_tests_codestral/test_httpie_plugins_manager_PluginManager_unregister_2_test_none_input.py:12: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <PluginManager {'adapters': [], 'auth': [], 'converters': [], 'formatters': []}>
plugin = None

    def unregister(self, plugin: Type[BasePlugin]):
>       self.remove(plugin)
E       ValueError: list.remove(x): x not in list

httpie/httpie/plugins/manager.py:54: ValueError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_plugins_manager_PluginManager_unregister_2_test_none_input.py::test_none_input
============================== 1 failed in 0.19s ===============================
"""