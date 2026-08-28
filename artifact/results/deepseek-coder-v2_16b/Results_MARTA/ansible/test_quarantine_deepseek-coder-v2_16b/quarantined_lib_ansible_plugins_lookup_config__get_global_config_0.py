
import pytest
from ansible.errors import AnsibleLookupError, MissingSetting
from ansible.plugins.lookup.config import _get_global_config  # Assuming this is the correct module path

# Test case for retrieving a valid global configuration setting
def test_get_valid_global_config():
    class C:
        setting_name = "value"
    
    result = _get_global_config('setting_name', obj=C)
    assert result == "value"

# Test case for retrieving a non-existent global configuration setting
def test_get_non_existent_global_config():
    class C:
        pass
    
    with pytest.raises(MissingSetting):
        _get_global_config('non_existent_setting', obj=C)

# Test case for retrieving a callable global configuration setting
def test_get_callable_global_config():
    class C:
        def callable_setting():
            pass
    
    with pytest.raises(AnsibleLookupError):
        _get_global_config('callable_setting', obj=C)

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
_ ERROR collecting test_lib_ansible_plugins_lookup_config__get_global_config_0.py _
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_lookup_config__get_global_config_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_lookup_config__get_global_config_0.py:3: in <module>
    from ansible.errors import AnsibleLookupError, MissingSetting
E   ImportError: cannot import name 'MissingSetting' from 'ansible.errors' (/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/errors/__init__.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_lookup_config__get_global_config_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.39s ===============================
"""