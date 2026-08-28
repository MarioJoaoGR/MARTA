
import pytest
from flutils.namedtupleutils import to_namedtuple
from collections import namedtuple, OrderedDict, SimpleNamespace
from typing import List, Union, Tuple

# Helper function to create a namedtuple from an object
def _to_namedtuple(obj):
    if isinstance(obj, dict):
        fields = sorted({k: None for k in obj.keys()}.keys())  # Sort keys alphabetically
        NamedTupleClass = namedtuple('NamedTuple', fields)
        return NamedTupleClass(**{k: _to_namedtuple(v) for k, v in obj.items()})
    elif isinstance(obj, list):
        return [_to_namedtuple(item) for item in obj]
    elif isinstance(obj, tuple):
        return tuple(_to_namedtuple(item) for item in obj)
    elif isinstance(obj, SimpleNamespace):
        fields = sorted({k: None for k in dir(obj) if not k.startswith('_') and k != 'items'} + list(obj.__dict__.keys()))
        NamedTupleClass = namedtuple('NamedTuple', fields)
        return NamedTupleClass(**{k: _to_namedtuple(getattr(obj, k)) for k in fields})
    else:
        return obj

# Test cases
def test_convert_dictionary_to_namedtuple():
    dic = {'a': 1, 'b': 2}
    result = to_namedtuple(dic)
    assert isinstance(result, namedtuple)
    assert result.a == 1
    assert result.b == 2

def test_convert_list_of_dictionaries_to_list_of_namedtuples():
    lst = [{"key": "value"}, {"another_key": "another_value"}]
    result = to_namedtuple(lst)
    assert isinstance(result, list)
    for item in result:
        assert isinstance(item, namedtuple)
    assert len(result) == 2

def test_convert_tuple_of_dictionaries_to_tuple_of_namedtuples():
    tup = ({"key": "value"}, {"another_key": "another_value"})
    result = to_namedtuple(tup)
    assert isinstance(result, tuple)
    for item in result:
        assert isinstance(item, namedtuple)
    assert len(result) == 2

def test_convert_simplenamespace_to_namedtuple():
    obj = SimpleNamespace(a=1, b=2)
    result = to_namedtuple(obj)
    assert isinstance(result, namedtuple)
    assert result.a == 1
    assert result.b == 2

def test_convert_list_of_lists_to_list_of_namedtuples():
    lst_of_lsts = [[{"key": "value"}], [{"another_key": "another_value"}]]
    result = to_namedtuple(lst_of_lsts)
    assert isinstance(result, list)
    for item in result:
        assert isinstance(item, namedtuple)
    assert len(result) == 2

def test_convert_nested_structure_to_namedtuple():
    nested_dict = {"outer": {"inner1": 1, "inner2": 2}}
    result = to_namedtuple(nested_dict)
    assert isinstance(result.outer, namedtuple)
    assert result.outer.inner1 == 1
    assert result.outer.inner2 == 2

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_______ ERROR collecting test_flutils_namedtupleutils_to_namedtuple_0.py _______
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_namedtupleutils_to_namedtuple_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_namedtupleutils_to_namedtuple_0.py:4: in <module>
    from collections import namedtuple, OrderedDict, SimpleNamespace
E   ImportError: cannot import name 'SimpleNamespace' from 'collections' (/opt/conda/envs/test4py_env/lib/python3.10/collections/__init__.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_namedtupleutils_to_namedtuple_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.13s ===============================
"""