
import pytest
from ansible.vars.clean import strip_internal_keys
from collections import MutableMapping, MutableSequence
from unittest.mock import patch

def test_strip_internal_keys_with_dictionary():
    data = {'a': 1, '_ansible_key': 'value', 'nested': {'_ansible_inner_key': 'inner_value'}}
    result = strip_internal_keys(data)
    assert '_ansible_key' not in result
    assert '_ansible_inner_key' not in result['nested']
    assert isinstance(result, dict)

def test_strip_internal_keys_with_exceptions():
    data_with_exceptions = {'a': 1, '_ansible_key': 'value', 'nested': {'_ansible_inner_key': 'inner_value'}}
    result_with_exceptions = strip_internal_keys(data_with_exceptions, exceptions=('_ansible_inner_key',))
    assert '_ansible_key' in result_with_exceptions
    assert '_ansible_inner_key' not in result_with_exceptions['nested']
    assert isinstance(result_with_exceptions, dict)

def test_strip_internal_keys_with_list():
    data_list = [{'a': 1, '_ansible_key': 'value'}, {'b': 2, '_ansible_other_key': 'other_value'}]
    result_list = strip_internal_keys(data_list)
    assert '_ansible_key' not in result_list[0]
    assert '_ansible_other_key' not in result_list[1]
    assert isinstance(result_list, list)

def test_strip_internal_keys_with_nested_lists():
    data_nested_lists = [[{'a': 1, '_ansible_key': 'value'}], [{'b': 2, '_ansible_other_key': 'other_value'}]]
    result_nested_lists = strip_internal_keys(data_nested_lists)
    assert '_ansible_key' not in result_nested_lists[0][0]
    assert '_ansible_other_key' not in result_nested_lists[1][0]
    assert isinstance(result_nested_lists, list)

@pytest.mark.xfail(raises=TypeError)
def test_strip_internal_keys_with_invalid_type():
    non_dict_list = [1, 2, 3]
    strip_internal_keys(non_dict_list)

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
____ ERROR collecting test_lib_ansible_vars_clean_strip_internal_keys_0.py _____
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_vars_clean_strip_internal_keys_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_vars_clean_strip_internal_keys_0.py:4: in <module>
    from collections import MutableMapping, MutableSequence
E   ImportError: cannot import name 'MutableMapping' from 'collections' (/opt/conda/envs/test4py_env/lib/python3.10/collections/__init__.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_vars_clean_strip_internal_keys_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.49s ===============================
"""