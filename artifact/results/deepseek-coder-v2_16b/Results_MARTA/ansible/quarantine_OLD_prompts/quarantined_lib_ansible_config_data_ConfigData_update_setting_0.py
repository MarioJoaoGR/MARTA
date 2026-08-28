
import pytest
from unittest.mock import patch, MagicMock
from ansible.config.data import ConfigData, ConfigSetting

# Test case for updating a global setting
def test_update_global_setting():
    config = ConfigData()
    setting = ConfigSetting(name='log_level', value='DEBUG')
    
    with patch('ansible.config.data.ConfigSetting', return_value=setting):
        config.update_setting(setting)
        assert config._global_settings == {'log_level': setting}

# Test case for updating a plugin-specific setting
def test_update_plugin_setting():
    config = ConfigData()
    plugin = MagicMock()
    plugin.type = 'logging'
    plugin.name = 'file_logger'
    setting = ConfigSetting(name='log_level', value='INFO')
    
    with patch('ansible.config.data.ConfigSetting', return_value=setting):
        config.update_setting(setting, plugin)
        assert config._plugins == {'logging': {'file_logger': {'log_level': setting}}}

# Test case for updating a global setting without providing a plugin
def test_update_global_setting_without_plugin():
    config = ConfigData()
    setting = ConfigSetting(name='log_level', value='DEBUG')
    
    with patch('ansible.config.data.ConfigSetting', return_value=setting):
        config.update_setting(setting)
        assert config._global_settings == {'log_level': setting}

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
_ ERROR collecting test_lib_ansible_config_data_ConfigData_update_setting_0.py _
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_config_data_ConfigData_update_setting_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_config_data_ConfigData_update_setting_0.py:4: in <module>
    from ansible.config.data import ConfigData, ConfigSetting
E   ImportError: cannot import name 'ConfigSetting' from 'ansible.config.data' (/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/config/data.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_config_data_ConfigData_update_setting_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.32s ===============================
"""