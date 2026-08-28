
import pytest
from your_module_name import ConfigData  # Replace 'your_module_name' with the actual module name where ConfigData is defined

# Test case for setting and getting a global configuration setting
def test_set_and_get_global_setting():
    config = ConfigData()
    config.set_global_setting('log_level', 'INFO')
    assert config.get_global_setting('log_level') == 'INFO'

# Test case for adding a plugin and getting its configuration setting
def test_add_and_get_plugin():
    config = ConfigData()
    config.add_plugin('logging', {'file': 'logs/app.log', 'level': 'DEBUG'})
    assert config.get_plugin('logging') == {'file': 'logs/app.log', 'level': 'DEBUG'}

# Test case for getting a configuration setting either globally or by plugin
def test_get_setting():
    config = ConfigData()
    config.set_global_setting('log_level', 'INFO')
    assert config.get_setting('log_level') == 'INFO'
    
    plugin = type('Plugin', (object,), {'type': 'logging', 'name': 'file_logger'})()
    assert config.get_setting('log_level', plugin) == 'INFO'

# Test case for updating a global configuration setting
def test_update_global_setting():
    config = ConfigData()
    config.set_global_setting('log_level', 'INFO')
    config.update_setting(ConfigSetting('log_level', 'DEBUG'))
    assert config.get_global_setting('log_level') == 'DEBUG'

# Test case for updating a plugin-specific configuration setting
def test_update_plugin_setting():
    config = ConfigData()
    config.add_plugin('logging', {'file': 'logs/app.log', 'level': 'DEBUG'})
    plugin = type('Plugin', (object,), {'type': 'logging', 'name': 'file_logger'})()
    config.update_setting(ConfigSetting('log_level', 'INFO'), plugin)
    assert config.get_setting('log_level', plugin) == 'INFO'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
__ ERROR collecting test_lib_ansible_config_data_ConfigData_get_setting_0.py ___
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_config_data_ConfigData_get_setting_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_config_data_ConfigData_get_setting_0.py:3: in <module>
    from your_module_name import ConfigData  # Replace 'your_module_name' with the actual module name where ConfigData is defined
E   ModuleNotFoundError: No module named 'your_module_name'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_config_data_ConfigData_get_setting_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.30s ===============================
"""