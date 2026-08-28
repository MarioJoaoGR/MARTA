
import pytest
from collections import Mapping, Iterable
from ansible.plugins.filter.mathstuff import rekey_on_member  # Import the function from its module

# Test case for successful rekeying on a specific key from a dictionary of dictionaries
def test_rekey_on_member_dict_of_dicts():
    data = {'a': {'id': 1, 'name': 'Alice'}, 'b': {'id': 2, 'name': 'Bob'}}
    key = 'id'
    result = rekey_on_member(data, key)
    assert result == {1: {'id': 1, 'name': 'Alice'}, 2: {'id': 2, 'name': 'Bob'}}

# Test case for successful rekeying on a specific key from a list of dictionaries
def test_rekey_on_member_list_of_dicts():
    data = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
    key = 'id'
    result = rekey_on_member(data, key)
    assert result == {1: {'id': 1, 'name': 'Alice'}, 2: {'id': 2, 'name': 'Bob'}}

# Test case for handling duplicates with the 'error' option
def test_rekey_on_member_duplicates_error():
    data = [{'id': 1, 'name': 'Alice'}, {'id': 1, 'name': 'Bob'}]
    key = 'id'
    with pytest.raises(AnsibleFilterError) as e:
        rekey_on_member(data, key, 'error')
    assert str(e.value) == "Key 1 is not unique, cannot correctly turn into dict"

# Test case for handling duplicates with the 'overwrite' option
def test_rekey_on_member_duplicates_overwrite():
    data = [{'id': 1, 'name': 'Alice'}, {'id': 1, 'name': 'Bob'}]
    key = 'id'
    result = rekey_on_member(data, key, 'overwrite')
    assert result == {1: {'id': 1, 'name': 'Bob'}}

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
_ ERROR collecting test_lib_ansible_plugins_filter_mathstuff_rekey_on_member_0.py _
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_filter_mathstuff_rekey_on_member_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_filter_mathstuff_rekey_on_member_0.py:3: in <module>
    from collections import Mapping, Iterable
E   ImportError: cannot import name 'Mapping' from 'collections' (/opt/conda/envs/test4py_env/lib/python3.10/collections/__init__.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_filter_mathstuff_rekey_on_member_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.35s ===============================
"""