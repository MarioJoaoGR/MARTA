
import pytest
from ansible.config.data import ConfigData, ConfigSetting

@pytest.fixture(scope="module")
def config_instance():
    return ConfigData()

def test_set_and_get_global_setting(config_instance):
    config_instance.set_global_setting('log_level', 'INFO')
    assert config_instance.get_global_setting('log_level') == 'INFO'

def test_add_plugin_and_get_plugin(config_instance):
    config_instance.add_plugin('logging', {'file': 'logs/app.log', 'level': 'DEBUG'})
    assert config_instance.get_plugin('logging') == {'file': 'logs/app.log', 'level': 'DEBUG'}

def test_get_setting_global(config_instance):
    config_instance.set_global_setting('timeout', 30)
    assert config_instance.get_setting('timeout') == 30

def test_get_setting_plugin(config_instance):
    plugin = ConfigSetting(name='timeout', value=30)
    config_instance.set_global_setting('timeout', 30)
    assert config_instance.get_setting('timeout', plugin) == 30

def test_update_setting_global(config_instance):
    config_instance.update_setting(ConfigSetting(name='log_level', value='DEBUG'))
    assert config_instance.get_global_setting('log_level') == 'DEBUG'

def test_update_setting_plugin(config_instance):
    plugin = ConfigSetting(name='timeout', value=30)
    config_instance.set_global_setting('timeout', 30)
    assert config_instance.get_setting('timeout', plugin) == 30

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
__ ERROR collecting test_lib_ansible_config_data_ConfigData_get_setting_1.py ___
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_config_data_ConfigData_get_setting_1.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_config_data_ConfigData_get_setting_1.py:3: in <module>
    from ansible.config.data import ConfigData, ConfigSetting
E   ImportError: cannot import name 'ConfigSetting' from 'ansible.config.data' (/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/config/data.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_config_data_ConfigData_get_setting_1.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.69s ===============================
"""