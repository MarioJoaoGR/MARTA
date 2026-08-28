
import pytest
from ansible.utils.vars import merge_hash
from collections import MutableMapping, MutableSequence

def test_merge_hash_basic():
    merged = merge_hash({'a': 1}, {'b': 2})
    assert merged == {'a': 1, 'b': 2}

def test_merge_hash_recursive_false():
    merged = merge_hash({'a': [1, 2]}, {'a': {'b': 3}}, recursive=False)
    assert merged == {'a': {'b': 3}}

def test_merge_hash_list_merge_append():
    merged = merge_hash({'a': [1, 2]}, {'a': {'b': [3, 4]}}, list_merge='append')
    assert merged == {'a': {'b': [3, 4, 3, 4]}}

def test_merge_hash_list_merge_prepend():
    merged = merge_hash({'a': [1, 2]}, {'a': {'b': [3, 4]}}, list_merge='prepend')
    assert merged == {'a': {'b': [3, 4, 1, 2]}}

def test_merge_hash_list_merge_append_rp():
    merged = merge_hash({'a': [1, 2]}, {'a': {'b': [2, 3]}}, list_merge='append_rp')
    assert merged == {'a': {'b': [1, 2]}}

def test_merge_hash_list_merge_prepend_rp():
    merged = merge_hash({'a': [1, 2]}, {'a': {'b': [2, 3]}}, list_merge='prepend_rp')
    assert merged == {'a': {'b': [2, 3]}}

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
_________ ERROR collecting test_lib_ansible_utils_vars_merge_hash_0.py _________
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_vars_merge_hash_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_vars_merge_hash_0.py:4: in <module>
    from collections import MutableMapping, MutableSequence
E   ImportError: cannot import name 'MutableMapping' from 'collections' (/opt/conda/envs/test4py_env/lib/python3.10/collections/__init__.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_vars_merge_hash_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.46s ===============================
"""