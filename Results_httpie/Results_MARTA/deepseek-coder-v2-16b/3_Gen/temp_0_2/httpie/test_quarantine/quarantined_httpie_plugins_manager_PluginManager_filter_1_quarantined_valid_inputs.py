
import pytest
from unittest.mock import patch
from httpie.plugins.manager import PluginManager

class BasePlugin: pass
class SomePluginType(BasePlugin): pass

def test_valid_inputs():
    class BasePlugin: pass
    class SomePluginType(BasePlugin): pass

    manager = PluginManager()
    with patch('httpie.plugins.manager.PluginManager.__iter__', return_value=[SomePluginType(), BasePlugin()]):
        filtered_plugins = manager.filter(by_type=SomePluginType)
        assert len(filtered_plugins) == 1

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

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_plugins_manager_PluginManager_filter_1_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        class BasePlugin: pass
        class SomePluginType(BasePlugin): pass
    
        manager = PluginManager()
        with patch('httpie.plugins.manager.PluginManager.__iter__', return_value=[SomePluginType(), BasePlugin()]):
>           filtered_plugins = manager.filter(by_type=SomePluginType)

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_plugins_manager_PluginManager_filter_1_test_valid_inputs.py:15: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <PluginManager {'adapters': [], 'auth': [], 'converters': [], 'formatters': []}>
by_type = <class 'test_httpie_plugins_manager_PluginManager_filter_1_test_valid_inputs.test_valid_inputs.<locals>.SomePluginType'>

    def filter(self, by_type=Type[BasePlugin]):
>       return [plugin for plugin in self if issubclass(plugin, by_type)]
E       TypeError: iter() returned non-iterator of type 'list'

httpie/httpie/plugins/manager.py:57: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_plugins_manager_PluginManager_filter_1_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.16s ===============================
"""