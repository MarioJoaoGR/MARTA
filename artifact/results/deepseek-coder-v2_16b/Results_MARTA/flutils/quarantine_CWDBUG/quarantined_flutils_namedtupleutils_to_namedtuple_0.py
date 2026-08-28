
import pytest
from flutils.namedtupleutils import to_namedtuple
from collections import namedtuple
from types import SimpleNamespace
from typing import List, Tuple, Dict, Union

# Helper function to create a namedtuple from an object
def make_namedtuple(obj):
    if isinstance(obj, dict):
        fields = sorted({k: None for k in obj.keys()}.keys())
        NamedTupleClass = namedtuple('NamedTuple', fields)
        return NamedTupleClass(**obj)
    elif isinstance(obj, list):
        items = [make_namedtuple(item) for item in obj]
        return tuple(items) if len(items) > 1 else items[0]
    elif isinstance(obj, tuple):
        items = [make_namedtuple(item) for item in obj]
        return tuple(items)
    elif isinstance(obj, SimpleNamespace):
        fields = {k: getattr(obj, k) for k in dir(obj) if not k.startswith('_')}
        sorted_fields = dict(sorted(fields.items(), key=lambda item: item[0]))
        return make_namedtuple(sorted_fields)
    else:
        return obj

# Test cases
def test_convert_dictionary_to_namedtuple():
    dic = {'a': 1, 'b': 2}
    result = to_namedtuple(dic)
    expected = make_namedtuple(dic)
    assert isinstance(result, namedtuple), "Result should be a namedtuple"
    assert result == expected, f"Expected {expected}, but got {result}"

def test_convert_list_of_dictionaries_to_list_of_namedtuples():
    lst = [{"key": "value"}, {"another_key": "another_value"}]
    result = to_namedtuple(lst)
    expected = [make_namedtuple({"key": "value"}), make_namedtuple({"another_key": "another_value"})]
    assert isinstance(result, list), "Result should be a list of namedtuples"
    for r, e in zip(result, expected):
        assert isinstance(r, namedtuple), f"Item {r} in result is not a namedtuple"
        assert r == e, f"Expected {e}, but got {r}"

def test_convert_tuple_of_dictionaries_to_tuple_of_namedtuples():
    tup = ({"key": "value"}, {"another_key": "another_value"})
    result = to_namedtuple(tup)
    expected = (make_namedtuple({"key": "value"}), make_namedtuple({"another_key": "another_value"}))
    assert isinstance(result, tuple), "Result should be a tuple of namedtuples"
    for r, e in zip(result, expected):
        assert isinstance(r, namedtuple), f"Item {r} in result is not a namedtuple"
        assert r == e, f"Expected {e}, but got {r}"

def test_convert_simplenamespace_to_namedtuple():
    obj = SimpleNamespace(a=1, b=2)
    result = to_namedtuple(obj)
    expected = make_namedtuple({"a": 1, "b": 2})
    assert isinstance(result, namedtuple), "Result should be a namedtuple"
    assert result == expected, f"Expected {expected}, but got {result}"

def test_convert_list_of_lists_to_list_of_namedtuples():
    lst_of_lsts = [[{"key": "value"}], [{"another_key": "another_value"}]]
    result = to_namedtuple(lst_of_lsts)
    expected = [make_namedtuple({"key": "value"}), make_namedtuple({"another_key": "another_value"})]
    assert isinstance(result, list), "Result should be a list of namedtuples"
    for r, e in zip(result, expected):
        assert isinstance(r, namedtuple), f"Item {r} in result is not a namedtuple"
        assert r == e, f"Expected {e}, but got {r}"

def test_convert_nested_structure_to_namedtuple():
    nested_dict = {"outer": {"inner1": 1, "inner2": 2}}
    result = to_namedtuple(nested_dict)
    expected = namedtuple('NamedTuple', 'outer')(make_namedtuple({"inner1": 1, "inner2": 2}))
    assert isinstance(result, namedtuple), "Result should be a namedtuple"
    assert result == expected, f"Expected {expected}, but got {result}"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
Traceback (most recent call last):
  File "/opt/conda/envs/test4py_env/lib/python3.10/runpy.py", line 196, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "/opt/conda/envs/test4py_env/lib/python3.10/runpy.py", line 86, in _run_code
    exec(code, run_globals)
  File "/data/pydeps/marta/pytest/__main__.py", line 9, in <module>
    raise SystemExit(pytest.console_main())
  File "/data/pydeps/marta/_pytest/config/__init__.py", line 201, in console_main
    code = main()
  File "/data/pydeps/marta/_pytest/config/__init__.py", line 156, in main
    config = _prepareconfig(args, plugins)
  File "/data/pydeps/marta/_pytest/config/__init__.py", line 332, in _prepareconfig
    config = get_config(args, plugins)
  File "/data/pydeps/marta/_pytest/config/__init__.py", line 293, in get_config
    dir=pathlib.Path.cwd(),
  File "/opt/conda/envs/test4py_env/lib/python3.10/pathlib.py", line 993, in cwd
    return cls(cls._accessor.getcwd())
FileNotFoundError: [Errno 2] No such file or directory
"""