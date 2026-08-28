
import pytest
from ansible.plugins.filter import unique
from ansible.errors import AnsibleFilterError

# Test case 1: Basic usage of the unique filter
def test_unique_basic():
    result = unique({'var': 'value'}, ['apple', 'banana', 'Apple', 'cherry'])
    assert sorted(result) == ['apple', 'banana', 'cherry']

# Test case 2: Case sensitivity specified
def test_unique_case_sensitive():
    result = unique({'var': 'value'}, ['apple', 'banana', 'Apple', 'cherry'], case_sensitive=False)
    assert sorted(result) == ['apple', 'banana', 'cherry']

# Test case 3: Attribute specified for comparison
def test_unique_attribute():
    result = unique({'var': 'value'}, [{'name': 'Alice'}, {'name': 'Bob'}, {'name': 'Alice'}], attribute='name')
    assert sorted(result, key=lambda x: x['name']) == [{'name': 'Alice'}, {'name': 'Bob'}]

# Test case 4: Both case sensitivity and attribute specified
def test_unique_both():
    result = unique({'var': 'value'}, ['apple', 'banana', 'Apple', 'cherry'], case_sensitive=False, attribute='name')
    assert sorted(result, key=lambda x: x['name']) == [{'name': 'Alice'}, {'name': 'Bob'}]

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
____ ERROR collecting test_lib_ansible_plugins_filter_mathstuff_unique_0.py ____
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_filter_mathstuff_unique_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_filter_mathstuff_unique_0.py:3: in <module>
    from ansible.plugins.filter import unique
E   ImportError: cannot import name 'unique' from 'ansible.plugins.filter' (/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/plugins/filter/__init__.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_filter_mathstuff_unique_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.48s ===============================
"""