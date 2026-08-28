
import pytest
from py_backwards.transformers.dict_unpacking import _py_backwards_merge_dicts

def test_basic_merging():
    d1 = {'a': 1, 'b': {'c': 2}}
    d2 = {'b': {'d': 3}, 'e': 4}
    expected = {'a': 1, 'b': {'c': 2, 'd': 3}, 'e': 4}
    assert _py_backwards_merge_dicts([d1, d2]) == expected

def test_empty_list():
    assert _py_backwards_merge_dicts([]) == {}

def test_nested_merging():
    d1 = {'a': 1, 'b': {'c': 2}}
    d2 = {'b': {'d': 3}, 'e': 4}
    d3 = {'f': 5, 'g': {'h': 6}}
    expected = {'a': 1, 'b': {'c': 2, 'd': 3}, 'e': 4, 'f': 5, 'g': {'h': 6}}
    assert _py_backwards_merge_dicts([d1, d2, d3]) == expected

def test_overlapping_keys():
    d1 = {'a': 1, 'b': {'c': 2}}
    d2 = {'b': {'c': 10}, 'e': 4}
    expected = {'a': 1, 'b': {'c': 10}, 'e': 4}
    assert _py_backwards_merge_dicts([d1, d2]) == expected

def test_different_data_types():
    d1 = {'a': 1, 'b': {'c': [1, 2]}}
    d2 = {'b': {'c': [3, 4]}, 'e': "string"}
    expected = {'a': 1, 'b': {'c': [3, 4]}, 'e': "string"}
    assert _py_backwards_merge_dicts([d1, d2]) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_ ERROR collecting test_py_backwards_transformers_dict_unpacking__py_backwards_merge_dicts_0.py _
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_transformers_dict_unpacking__py_backwards_merge_dicts_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_transformers_dict_unpacking__py_backwards_merge_dicts_0.py:3: in <module>
    from py_backwards.transformers.dict_unpacking import _py_backwards_merge_dicts
E   ImportError: cannot import name '_py_backwards_merge_dicts' from 'py_backwards.transformers.dict_unpacking' (/opt/marta/baselines/codamosa/replication/test-apps/py-backwards/py_backwards/transformers/dict_unpacking.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_transformers_dict_unpacking__py_backwards_merge_dicts_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.14s ===============================
"""