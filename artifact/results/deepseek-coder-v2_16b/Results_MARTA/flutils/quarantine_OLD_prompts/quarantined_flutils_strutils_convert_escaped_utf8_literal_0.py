
import pytest
from flutils.strutils import convert_escaped_utf8_literal

def test_basic_usage():
    a = 'test\\\\xc2\\\\xa9'
    result = convert_escaped_utf8_literal(a)
    assert result == 'test©'

def test_environment_variable():
    import os
    os.environ['TEST'] = 'test\\\\xc2\\\\xa9'
    with pytest.raises(UnicodeDecodeError):
        a = os.getenv('TEST')
        convert_escaped_utf8_literal(a)

def test_empty_string():
    text = ''
    result = convert_escaped_utf8_literal(text)
    assert result == ''

def test_non_utf8_escaped_characters():
    text = 'test\\\\x00'
    with pytest.raises(UnicodeDecodeError):
        convert_escaped_utf8_literal(text)

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