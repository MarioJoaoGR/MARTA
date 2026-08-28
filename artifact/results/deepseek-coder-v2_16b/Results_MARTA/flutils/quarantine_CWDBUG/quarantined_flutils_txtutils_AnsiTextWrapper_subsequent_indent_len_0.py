
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

# Test 2: Custom Width and Placeholder
def test_custom_width_and_placeholder():
    wrapper = AnsiTextWrapper(width=40, placeholder=' [CUSTOM]')
    assert wrapper.width == 40
    assert wrapper.placeholder == ' [CUSTOM]'

# Test 3: Custom Indentations
def test_custom_indentations():
    wrapper = AnsiTextWrapper(initial_indent='> ', subsequent_indent='  ')
    assert wrapper.initial_indent == '> '
    assert wrapper.subsequent_indent == '  '

# Test 4: Custom Indentation Length Calculation
def test_custom_indentation_length():
    wrapper = AnsiTextWrapper(subsequent_indent='---')
    assert wrapper.subsequent_indent_len() == len('---')

# Test 5: Disable Expand Tabs and Replace Whitespace
def test_disable_expand_tabs_and_replace_whitespace():
    wrapper = AnsiTextWrapper(expand_tabs=False, replace_whitespace=False)
    assert not wrapper.expand_tabs
    assert not wrapper.replace_whitespace

# Test 6: Wrap Text with ANSI Codes
def test_wrap_text_with_ansi_codes():
    text = (
        '\x1b[31m\x1b[1m\x1b[4mLorem ipsum dolor sit amet, consectetur adipiscing elit. Cras fermentum maximus auctor.\x1b[0m'
    )
    wrapper = AnsiTextWrapper(width=20)
    wrapped_text = wrapper.fill(text)
    assert isinstance(wrapped_text, str)  # Ensure it returns a string

# Test 7: Wrap Text with Custom Width and Indentations
def test_wrap_text_with_custom_width_and_indentations():
    text = (
        '\x1b[31m\x1b[1m\x1b[4mLorem ipsum dolor sit amet, consectetur adipiscing elit. Cras fermentum maximus auctor.\x1b[0m'
    )
    wrapper = AnsiTextWrapper(width=25, initial_indent='> ', subsequent_indent='  ')
    wrapped_text = wrapper.fill(text)
    assert isinstance(wrapped_text, str)  # Ensure it returns a string

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