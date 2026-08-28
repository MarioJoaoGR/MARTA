
import pytest
from flutils.namedtupleutils import to_namedtuple
from collections import namedtuple, OrderedDict, SimpleNamespace
from typing import List, Union, Tuple

# Helper function to create a namedtuple from an object
def _to_namedtuple(obj):
    if isinstance(obj, dict):
        keys = sorted([k for k in obj.keys() if not k.startswith('_')])
        nt_fields = tuple(keys)
        nt_values = tuple(obj[key] for key in keys)
        return namedtuple('NamedTuple', ' '.join(nt_fields))(*nt_values)
    elif isinstance(obj, (list, tuple)):
        converted_items = []
        for item in obj:
            if isinstance(item, dict):
                converted_items.append(_to_namedtuple(item))
            else:
                raise ValueError("Unsupported type inside list or tuple")
        return type(obj)(converted_items)  # Preserve the original type (list or tuple)
    elif isinstance(obj, SimpleNamespace):
        fields = sorted([f for f in dir(obj) if not f.startswith('_')])
        nt_fields = tuple(fields)
        nt_values = tuple(getattr(obj, field) for field in fields)
        return namedtuple('NamedTuple', ' '.join(nt_fields))(*nt_values)
    else:
        raise ValueError("Unsupported type")

# Test cases
def test_convert_dictionary_to_namedtuple():
    dic = {'a': 1, 'b': 2}
    result = to_namedtuple(dic)
    assert isinstance(result, namedtuple)
    assert result.a == 1 and result.b == 2

def test_convert_list_of_dictionaries_to_list_of_namedtuples():
    lst = [{"key": "value"}, {"another_key": "another_value"}]
    result = to_namedtuple(lst)
    assert isinstance(result, list)
    for item in result:
        assert isinstance(item, namedtuple)

def test_convert_tuple_of_dictionaries_to_tuple_of_namedtuples():
    tup = ({"key": "value"}, {"another_key": "another_value"})
    result = to_namedtuple(tup)
    assert isinstance(result, tuple)
    for item in result:
        assert isinstance(item, namedtuple)

def test_convert_simplenamespace_to_namedtuple():
    obj = SimpleNamespace(a=1, b=2)
    result = to_namedtuple(obj)
    assert isinstance(result, namedtuple)
    assert result.a == 1 and result.b == 2

def test_convert_list_of_lists_to_list_of_namedtuples():
    lst_of_lsts = [[{"key": "value"}], [{"another_key": "another_value"}]]
    result = to_namedtuple(lst_of_lsts)
    assert isinstance(result, list)
    for item in result:
        assert isinstance(item, namedtuple)

def test_convert_nested_structure_to_namedtuple():
    nested_dict = {"outer": {"inner1": 1, "inner2": 2}}
    result = to_namedtuple(nested_dict)
    assert isinstance(result, namedtuple)
    inner_nt = getattr(result, 'outer')
    assert isinstance(inner_nt, namedtuple) and inner_nt.inner1 == 1 and inner_nt.inner2 == 2

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