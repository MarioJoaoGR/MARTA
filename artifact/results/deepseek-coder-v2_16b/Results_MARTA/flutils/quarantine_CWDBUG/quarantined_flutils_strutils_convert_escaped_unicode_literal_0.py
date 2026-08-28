
import pytest
from flutils.strutils import convert_escaped_unicode_literal

def test_convert_escaped_unicode_literal_basic():
    a = '\\x31\\x2e\\u2605\\x20\\U0001f6d1'
    result = convert_escaped_unicode_literal(a)
    assert result == '1.★ 🛑'

def test_convert_escaped_unicode_literal_env_var():
    import os
    os.environ['TEST'] = '\\x31\\x2e\\u2605\\x20\\U0001f6d1'
    result = convert_escaped_unicode_literal(os.getenv('TEST'))
    assert result == '1.★ 🛑'

def test_convert_escaped_unicode_literal_escaped_backslashes():
    a = '\\\\x31\\\\x2e\\\\u2605\\\\x20\\\\U0001f6d1'
    result = convert_escaped_unicode_literal(a)
    assert result == '1.★ 🛑'

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