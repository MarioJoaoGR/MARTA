
import pytest
from flutils.namedtupleutils import _to_namedtuple

# Test 1: Conversion of a dictionary to a named tuple when _started is True
def test_conversion_of_dict_when_started_is_true():
    obj = {'key': 'value'}
    result = _to_namedtuple(obj, _started=True)
    assert result == obj

# Test 2: Conversion of a list to a named tuple when _started is True
def test_conversion_of_list_when_started_is_true():
    obj = [1, 2, 3]
    result = _to_namedtuple(obj, _started=True)
    assert result == obj

# Test 3: Conversion of a tuple to a named tuple when _started is True
def test_conversion_of_tuple_when_started_is_true():
    obj = (1, 2, 3)
    result = _to_namedtuple(obj, _started=True)
    assert result == obj

# Test 4: Attempt to convert an unsupported type when _started is False
def test_attempt_conversion_with_unsupported_type():
    obj = "not supported"
    with pytest.raises(TypeError):
        _to_namedtuple(obj, _started=False)

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