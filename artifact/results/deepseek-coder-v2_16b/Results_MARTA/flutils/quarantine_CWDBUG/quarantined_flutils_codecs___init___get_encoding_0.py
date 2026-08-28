
import pytest
from flutils.codecs import get_encoding, SYSTEM_ENCODING
import codecs

def test_get_encoding_default():
    encoding = get_encoding()
    assert encoding == SYSTEM_ENCODING

def test_get_encoding_valid_name():
    encoding = get_encoding('utf-8')
    assert encoding == 'utf-8'

def test_get_encoding_invalid_name_with_default():
    with pytest.raises(LookupError) as excinfo:
        get_encoding('invalid-encoding', 'utf-8')
    assert str(excinfo.value) == "The given 'name' of 'invalid-encoding' is an invalid encoding codec name."

def test_get_encoding_invalid_name_without_default():
    with pytest.raises(LookupError) as excinfo:
        get_encoding('invalid-encoding')
    assert str(excinfo.value) == "The given 'name' of 'invalid-encoding' is an invalid encoding codec name."

def test_get_encoding_valid_default():
    with pytest.raises(LookupError) as excinfo:
        get_encoding('utf-8', 'invalid-encoding')
    assert str(excinfo.value) == "The given 'name' of 'utf-8' is a valid encoding codec name."

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