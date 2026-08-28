
import pytest
from flutils.codecs.raw_utf8_escape import _each_utf8_hex

def test_each_utf8_hex_ascii():
    text = "Hello, World!"
    result = list(_each_utf8_hex(text))
    expected = ['H', 'e', 'l', 'l', 'o', ',', ' ', 'W', 'o', 'r', 'l', 'd', '!']
    assert result == expected, f"Expected {expected}, but got {result}"

def test_each_utf8_hex_non_ascii():
    text = "中文文本"
    result = list(_each_utf8_hex(text))
    expected = ['\xe4', '\xb8', '\xad', '\xe6', '\x96', '\x87', '\xe6', '\x9c', '\xac', '\xe6', '\x96', '\x87']
    assert result == expected, f"Expected {expected}, but got {result}"

def test_each_utf8_hex_empty():
    text = ""
    result = list(_each_utf8_hex(text))
    expected = []
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