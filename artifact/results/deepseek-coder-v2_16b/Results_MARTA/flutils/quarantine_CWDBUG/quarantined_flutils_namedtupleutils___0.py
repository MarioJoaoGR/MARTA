
import pytest
from types import SimpleNamespace
from flutils.namedtupleutils import _to_namedtuple

def test_convert_simple_namespace_to_namedtuple():
    ns = SimpleNamespace(a=1, b='test')
    result = _to_namedtuple(ns)
    assert isinstance(result, tuple)
    assert hasattr(result, 'a') and getattr(result, 'a') == 1
    assert hasattr(result, 'b') and getattr(result, 'b') == 'test'

def test_convert_simple_namespace_with_different_attributes():
    ns = SimpleNamespace(x=42, y="example")
    result = _to_namedtuple(ns)
    assert isinstance(result, tuple)
    assert hasattr(result, 'x') and getattr(result, 'x') == 42
    assert hasattr(result, 'y') and getattr(result, 'y') == "example"

def test_convert_simple_namespace_with_already_defined_attributes():
    ns = SimpleNamespace(c=3.14, d="string")
    result = _to_namedtuple(ns)
    assert isinstance(result, tuple)
    assert hasattr(result, 'c') and getattr(result, 'c') == 3.14
    assert hasattr(result, 'd') and getattr(result, 'd') == "string"

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