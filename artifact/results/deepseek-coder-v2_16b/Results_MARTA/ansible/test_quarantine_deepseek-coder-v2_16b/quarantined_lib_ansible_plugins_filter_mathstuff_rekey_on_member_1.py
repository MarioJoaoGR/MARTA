
import pytest
from ansible.errors import AnsibleFilterError, AnsibleFilterTypeError
from collections import Mapping, Iterable
from typing import Text, BinaryType

# Assuming the function is defined in a module named 'ansible.plugins.filter.mathstuff'
def rekey_on_member(data, key, duplicates='error'):
    """
    Rekey a dict of dicts on another member

    May also create a dict from a list of dicts.

    duplicates can be one of ``error`` or ``overwrite`` to specify whether to error out if the key
    value would be duplicated or to overwrite previous entries if that's the case.
    """
    if duplicates not in ('error', 'overwrite'):
        raise AnsibleFilterError("duplicates parameter to rekey_on_member has unknown value: {0}".format(duplicates))

    new_obj = {}

    # Ensure the positional args are defined - raise jinja2.exceptions.UndefinedError if not
    bool(data) and bool(key)

    if isinstance(data, Mapping):
        iterate_over = data.values()
    elif isinstance(data, Iterable) and not isinstance(data, (Text, BinaryType)):
        iterate_over = data
    else:
        raise AnsibleFilterTypeError("Type is not a valid list, set, or dict")

    for item in iterate_over:
        if not isinstance(item, Mapping):
            raise AnsibleFilterTypeError("List item is not a valid dict")

        try:
            key_elem = item[key]
        except KeyError:
            raise AnsibleFilterError("Key {0} was not found".format(key))
        except TypeError as e:
            raise AnsibleFilterTypeError(str(e))
        except Exception as e:
            raise AnsibleFilterError(str(e))

        # Note: if new_obj[key_elem] exists it will always be a non-empty dict (it will at
        # minimum contain {key: key_elem}
        if new_obj.get(key_elem, None):
            if duplicates == 'error':
                raise AnsibleFilterError("Key {0} is not unique, cannot correctly turn into dict".format(key_elem))
            elif duplicates == 'overwrite':
                new_obj[key_elem] = item
        else:
            new_obj[key_elem] = item

    return new_obj

# Test cases for rekey_on_member function
def test_rekey_on_member_dict_of_dicts():
    data = {'a': {'id': 1, 'name': 'Alice'}, 'b': {'id': 2, 'name': 'Bob'}}
    key = 'id'
    result = rekey_on_member(data, key)
    assert result == {1: {'id': 1, 'name': 'Alice'}, 2: {'id': 2, 'name': 'Bob'}}

def test_rekey_on_member_list_of_dicts():
    data = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
    key = 'id'
    result = rekey_on_member(data, key)
    assert result == {1: {'id': 1, 'name': 'Alice'}, 2: {'id': 2, 'name': 'Bob'}}

def test_rekey_on_member_duplicates_error():
    data = [{'id': 1, 'name': 'Alice'}, {'id': 1, 'name': 'Bob'}]
    key = 'id'
    with pytest.raises(AnsibleFilterError) as excinfo:
        rekey_on_member(data, key, 'error')
    assert str(excinfo.value) == "Key 1 is not unique, cannot correctly turn into dict"

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
_ ERROR collecting test_lib_ansible_plugins_filter_mathstuff_rekey_on_member_1.py _
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_filter_mathstuff_rekey_on_member_1.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_filter_mathstuff_rekey_on_member_1.py:4: in <module>
    from collections import Mapping, Iterable
E   ImportError: cannot import name 'Mapping' from 'collections' (/opt/conda/envs/test4py_env/lib/python3.10/collections/__init__.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_filter_mathstuff_rekey_on_member_1.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.65s ===============================
"""