
import pytest
from flutils.strutils import underscore_to_camel

def test_underscore_to_camel_basic():
    assert underscore_to_camel('foo_bar') == 'fooBar'

def test_underscore_to_camel_custom_first_char():
    assert underscore_to_camel('foo_bar', lower_first=True) == 'fooBar'
    assert underscore_to_camel('foo_bar', lower_first=False) == 'FooBar'

def test_underscore_to_camel_multiple_underscores():
    assert underscore_to_camel('_one__two___') == 'oneTwo'

def test_underscore_to_camel_explicit_first_char_case():
    assert underscore_to_camel('_one__two___', lower_first=True) == 'oneTwo'
    assert underscore_to_camel('_one__two___', lower_first=False) == 'OneTwo'

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