
import pytest
from flutils.strutils import as_escaped_utf8_literal

def test_as_escaped_utf8_literal_ascii():
    text = 'Hello, World!'
    expected_output = '\\x48\\x65\\x6c\\x6c\\x6f\\x2c\\x20\\x57\\x6f\\x72\\x6c\\x64\\x21'
    assert as_escaped_utf8_literal(text) == expected_output

def test_as_escaped_utf8_literal_unicode():
    text = '1.★ 🛑'
    expected_output = '\\x31\\x2e\\xe2\\x98\\x85\\x20\\xf0\\x9f\\x9b\\x91'
    assert as_escaped_utf8_literal(text) == expected_output

def test_as_escaped_utf8_literal_empty():
    text = ''
    expected_output = ''
    assert as_escaped_utf8_literal(text) == expected_output

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