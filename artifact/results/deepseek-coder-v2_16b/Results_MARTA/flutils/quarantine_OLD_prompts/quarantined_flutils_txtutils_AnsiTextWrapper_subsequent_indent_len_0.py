
import pytest
from flutils.txtutils import AnsiTextWrapper

# Test 1: Basic Initialization
def test_basic_initialization():
    wrapper = AnsiTextWrapper()
    assert wrapper.width == 70
    assert wrapper.initial_indent == ''
    assert wrapper.subsequent_indent == ''
    assert wrapper.expand_tabs is True
    assert wrapper.replace_whitespace is True
    assert wrapper.fix_sentence_endings is False
    assert wrapper.break_long_words is True
    assert wrapper.drop_whitespace is True
    assert wrapper.break_on_hyphens is True
    assert wrapper.tabsize == 8
    assert wrapper.max_lines is None
    assert wrapper.placeholder == ' [...]'

# Test 2: Custom Width and Indentations
def test_custom_width_and_indentations():
    wrapper = AnsiTextWrapper(width=50, initial_indent='> ', subsequent_indent='  ')
    assert wrapper.width == 50
    assert wrapper.initial_indent == '> '
    assert wrapper.subsequent_indent == '  '

# Test 3: Custom Placeholder
def test_custom_placeholder():
    wrapper = AnsiTextWrapper(placeholder=' [TRUNCATED]')
    assert wrapper.placeholder == ' [TRUNCATED]'

# Test 4: Calculate Subsequent Indent Length Without ANSI Codes
@pytest.mark.parametrize("input_indent, expected", [
    ('', 0),
    ('\x1b[31mSome text\x1b[0m', 0),
    (' Some text', len(' Some text')),
])
def test_subsequent_indent_len(input_indent, expected):
    wrapper = AnsiTextWrapper()
    wrapper.subsequent_indent = input_indent
    assert wrapper.subsequent_indent_len() == expected

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