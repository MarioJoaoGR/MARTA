
import pytest
from httpie_plugins.manager import PluginManager

def test_plugin_manager_repr():
    manager = PluginManager()
    assert repr(manager) == '<PluginManager: []>'

def test_add_plugin():
    manager = PluginManager()
    class SomePluginClass: pass
    plugin1 = SomePluginClass()
    manager.add_plugin(plugin1)
    assert repr(manager) == f'<PluginManager: [{SomePluginClass.__name__}]>'

def test_register_plugin():
    manager = PluginManager()
    class MyPlugin(object): pass
    manager.register(MyPlugin)
    assert repr(manager) == f'<PluginManager: [{MyPlugin.__name__}]>'

def test_unregister_plugin():
    manager = PluginManager()
    class MyPlugin(object): pass
    manager.register(MyPlugin)
    manager.unregister(MyPlugin)
    assert repr(manager) == '<PluginManager: []>'

def test_filter_plugins():
    manager = PluginManager()
    class FormatterPlugin: pass
    class SomePluginClass: pass
    plugin1 = FormatterPlugin()
    plugin2 = SomePluginClass()
    manager.add_plugin(plugin1)
    manager.add_plugin(plugin2)
    filtered_plugins = manager.filter(by_type=FormatterPlugin)
    assert repr(manager) == f'<PluginManager: [{FormatterPlugin.__name__}, {SomePluginClass.__name__}]>'

def test_get_auth_plugins():
    manager = PluginManager()
    class AuthPlugin: pass
    manager.register(AuthPlugin)
    auth_plugins = manager.get_auth_plugins()
    assert repr(manager) == f'<PluginManager: [{AuthPlugin.__name__}]>'

def test_get_specific_auth_plugin():
    manager = PluginManager()
    class AuthPlugin: pass
    manager.register(AuthPlugin)
    specific_auth_plugin = manager.get_auth_plugin(auth_type="basic")
    assert repr(manager) == f'<PluginManager: [{AuthPlugin.__name__}]>'

def test_get_formatters_grouped():
    manager = PluginManager()
    class FormatterPlugin: pass
    formatter1 = FormatterPlugin()
    formatter2 = FormatterPlugin()
    manager.add_plugin(formatter1)
    manager.add_plugin(formatter2)
    grouped_formatters = manager.get_formatters_grouped()
    assert repr(manager) == f'<PluginManager: [{FormatterPlugin.__name__, FormatterPlugin.__name__}]>'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
___ ERROR collecting test_httpie_plugins_manager_PluginManager___repr___0.py ___
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_plugins_manager_PluginManager___repr___0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_plugins_manager_PluginManager___repr___0.py:3: in <module>
    from httpie_plugins.manager import PluginManager
E   ModuleNotFoundError: No module named 'httpie_plugins'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_plugins_manager_PluginManager___repr___0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.15s ===============================
"""