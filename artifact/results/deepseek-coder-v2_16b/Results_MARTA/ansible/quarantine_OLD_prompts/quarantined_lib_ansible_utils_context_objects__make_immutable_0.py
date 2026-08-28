
import pytest
from ansible.utils.context_objects import _make_immutable
from collections import Mapping, Sequence, Set
from unittest.mock import patch

def test_make_immutable_string():
    with patch('ansible.utils.context_objects._make_immutable', return_value='hello'):
        result = _make_immutable('hello')
        assert result == 'hello'

def test_make_immutable_dict():
    input_dict = {'a': [1, 2, 3], 'b': {4, 5, 6}}
    expected_output = {'a': (1, 2, 3), 'b': frozenset({4, 5, 6})}
    with patch('ansible.utils.context_objects._make_immutable', side_effect=_make_immutable):
        result = _make_immutable(input_dict)
        assert result == expected_output

def test_make_immutable_frozenset():
    input_frozenset = frozenset([[7, 8], {'x': 'y'}])
    expected_output = frozenset({frozenset({7, 8}), ImmutableDict({'x': 'y'})})
    with patch('ansible.utils.context_objects._make_immutable', side_effect=_make_immutable):
        result = _make_immutable(input_frozenset)
        assert result == expected_output

def test_make_immutable_nested_structure():
    nested_structure = {
        'outer_dict': {'inner_list': [1, 2, 3], 'inner_set': {4, 5, 6}},
        'outer_list': [[7, 8], {'x': 'y'}],
        'outer_set': {(9,), ('z',)}
    }
    expected_output = {
        'outer_dict': ImmutableDict({'inner_list': (1, 2, 3), 'inner_set': frozenset({4, 5, 6})}),
        'outer_list': (frozenset({7, 8}), ImmutableDict({'x': 'y'})),
        'outer_set': (frozenset({9,}), frozenset({('z',)}))
    }
    with patch('ansible.utils.context_objects._make_immutable', side_effect=_make_immutable):
        result = _make_immutable(nested_structure)
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
_ ERROR collecting test_lib_ansible_utils_context_objects__make_immutable_0.py _
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_context_objects__make_immutable_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_context_objects__make_immutable_0.py:4: in <module>
    from collections import Mapping, Sequence, Set
E   ImportError: cannot import name 'Mapping' from 'collections' (/opt/conda/envs/test4py_env/lib/python3.10/collections/__init__.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_context_objects__make_immutable_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.41s ===============================
"""