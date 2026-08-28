
import pytest
from flutils.txtutils import AnsiTextWrapper
import textwrap
import re

# Helper function to remove ANSI escape codes from a string
def len_without_ansi(s):
    ansi_escape = re.compile(r'(?:\x1b\[[\d;]*m)')
    return len(ansi_escape.sub('', s))

# Test case for initial_indent_len method
@pytest.mark.parametrize("initial_indent, expected", [
    ('', 0),
    ('\x1b[31mHello\x1b[0m', len('Hello')),
    ('Initial \x1b[31mText\x1b[0m', len('Initial Text'))
])
def test_initial_indent_len(initial_indent, expected):
    wrapper = AnsiTextWrapper()
    wrapper.initial_indent = initial_indent
    assert wrapper.initial_indent_len() == expected

# Test case for wrapping text with ANSI codes
@pytest.mark.parametrize("text, width, expected", [
    ('\x1b[31mLorem ipsum dolor sit amet,\x1b[0m \x1b[32mconsectetur adipiscing elit.\x1b[0m', 40, '\x1b[31mLorem ipsum dolor sit amet,\x1b[0m\n\x1b[32mconsectetur adipiscing elit.\x1b[0m'),
    ('\x1b[31mLorem ipsum\x1b[0m \x1b[32mdolor sit amet,\x1b[0m \x1b[33mconsectetur adipiscing elit.\x1b[0m', 20, '\x1b[31mLorem ipsum\x1b[0m\n\x1b[32mdolor sit amet,\x1b[0m\n\x1b[33mconsectetur adipiscing elit.\x1b[0m')
])
def test_wrap_ansi_text(text, width, expected):
    wrapper = AnsiTextWrapper(width=width)
    with pytest.raises(SystemExit):  # Assuming the function should not raise an error for this specific case
        assert wrapper.fill(text) == expected

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