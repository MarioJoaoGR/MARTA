
import pytest
from unittest.mock import patch
from flutils.namedtupleutils import _to_namedtuple

def test_convert_dict_with_started():
    result = _to_namedtuple({'key': 'value'}, _started=True)
    assert result == {'key': 'value'}

def test_convert_unsupported_type_without_started():
    with pytest.raises(TypeError):
        _to_namedtuple("not supported", _started=False)

def test_convert_list_with_started():
    result = _to_namedtuple([1, 2, 3], _started=True)
    assert result == [1, 2, 3]

def test_convert_tuple_with_started():
    result = _to_namedtuple((1, 2, 3), _started=True)
    assert result == (1, 2, 3)

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