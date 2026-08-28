
import pytest
from ansible.utils.context_objects import ImmutableDict, frozenset

def _make_immutable(obj):
    """Recursively convert a container and objects inside of it into immutable data types"""
    if isinstance(obj, (str, bytes)):  # Strings are already immutable
        return obj
    elif isinstance(obj, dict):
        temp_dict = {}
        for key, value in obj.items():
            if isinstance(value, (list, set, dict)):
                temp_dict[key] = _make_immutable(value)
            else:
                temp_dict[key] = value
        return ImmutableDict(temp_dict)
    elif isinstance(obj, set):
        temp_set = set()
        for value in obj:
            if isinstance(value, (list, set, dict)):
                temp_set.add(_make_immutable(value))
            else:
                temp_set.add(value)
        return frozenset(temp_set)
    elif isinstance(obj, list):
        temp_list = []
        for value in obj:
            if isinstance(value, (list, set, dict)):
                temp_list.append(_make_immutable(value))
            else:
                temp_list.append(value)
        return tuple(temp_list)
    elif isinstance(obj, tuple):
        temp_tuple = []
        for value in obj:
            if isinstance(value, (list, set, dict)):
                temp_tuple.append(_make_immutable(value))
            else:
                temp_tuple.append(value)
        return tuple(temp_tuple)
    else:
        return obj

# Test cases for _make_immutable function

def test_make_immutable_string():
    result = _make_immutable("hello")
    assert isinstance(result, str)
    assert result == "hello"

def test_make_immutable_dict():
    input_dict = {'a': [1, 2, 3], 'b': {4, 5, 6}}
    expected_output = ImmutableDict({'a': (1, 2, 3), 'b': frozenset({4, 5, 6})})
    result = _make_immutable(input_dict)
    assert isinstance(result, ImmutableDict)
    assert result == expected_output

def test_make_immutable_frozenset():
    input_set = frozenset([[7, 8], {'x': 'y'}])
    expected_output = frozenset({frozenset({7, 8}), ImmutableDict({'x': 'y'})})
    result = _make_immutable(input_set)
    assert isinstance(result, frozenset)
    assert result == expected_output

def test_make_immutable_nested_structure():
    nested_structure = {
        'outer_dict': {'inner_list': [1, 2, 3], 'inner_set': {4, 5, 6}},
        'outer_list': [[7, 8], {'x': 'y'}],
        'outer_set': {(9,), ('z',)}
    }
    expected_output = ImmutableDict({
        'outer_dict': ImmutableDict({'inner_list': (1, 2, 3), 'inner_set': frozenset({4, 5, 6})}),
        'outer_list': (frozenset({7, 8}), ImmutableDict({'x': 'y'})),
        'outer_set': (frozenset({9,}), frozenset({'z',}))
    })
    result = _make_immutable(nested_structure)
    assert isinstance(result, ImmutableDict)
    assert result == expected_output

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
_ ERROR collecting test_lib_ansible_utils_context_objects__make_immutable_1.py _
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_context_objects__make_immutable_1.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_context_objects__make_immutable_1.py:3: in <module>
    from ansible.utils.context_objects import ImmutableDict, frozenset
E   ImportError: cannot import name 'frozenset' from 'ansible.utils.context_objects' (/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/utils/context_objects.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_context_objects__make_immutable_1.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.78s ===============================
"""