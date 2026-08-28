
import pytest
from ansible.module_utils.common.parameters import sanitize_keys
from collections import deque, MutableSequence, Mapping, MutableSet

def test_sanitize_keys_dictionary():
    result = sanitize_keys({'key1': 'no_log', 'key2': 'loggable'}, no_log_strings={'no_log'})
    assert result == {'key1__': '***', 'key2': 'loggable'}

def test_sanitize_keys_list():
    result = sanitize_keys([{'key1': 'no_log'}, {'key2': 'loggable'}], no_log_strings={'no_log'})
    assert result == [{'key1__': '***'}, {'key2': 'loggable'}]

def test_sanitize_keys_dictionary_with_ignore():
    result = sanitize_keys({'key1': 'no_log', 'key2': 'loggable'}, no_log_strings={'no_log'}, ignore_keys={'key2'})
    assert result == {'key1__': '***', 'key2': 'loggable'}

def test_sanitize_keys_non_container():
    result = sanitize_keys('not a container', no_log_strings={'no_log'})
    assert result == 'not a container'

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
_ ERROR collecting test_lib_ansible_module_utils_common_parameters_sanitize_keys_0.py _
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_parameters_sanitize_keys_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_parameters_sanitize_keys_0.py:4: in <module>
    from collections import deque, MutableSequence, Mapping, MutableSet
E   ImportError: cannot import name 'MutableSequence' from 'collections' (/opt/conda/envs/test4py_env/lib/python3.10/collections/__init__.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_parameters_sanitize_keys_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.36s ===============================
"""