
# Module: pytutils.lazy.lazy_regex
import pytest
from pytutils.lazy.lazy_regex import LazyRegex, _real_re_compile, InvalidPattern
import re

# Helper function to create a compiled regex for testing purposes
def compile_regex(*args, **kwargs):
    return _real_re_compile(*args, **kwargs)

# Test cases for LazyRegex class
def test_lazy_regex_basic():
    lazy_regex = LazyRegex(r'\d+')
    matches = lazy_regex.findall("123abc")  # The regex is now compiled and used to find all digit sequences in the string
    assert matches == ['123']

def test_lazy_regex_with_kwargs():
    lazy_regex = LazyRegex(r'\w+', ignorecase=True)
    matches = lazy_regex.findall("Hello World")  # The regex is now compiled and used to find all word characters in the string, case-insensitively
    assert matches == ['Hello', 'World']

def test_lazy_regex_invalid():
    try:
        lazy_regex = LazyRegex(r'[invalid-pattern')  # This will cause a compilation error
    except InvalidPattern as e:
        assert str(e) == '"[invalid-pattern" [None, None]'

def test_lazy_regex_with_different_args():
    lazy_regex = LazyRegex(r'^[A-Z]+', multiline=True, dotall=True)
    matches = lazy_regex.findall("HELLO WORLD")  # The regex is now compiled with specific flags and used to find all uppercase letters at the start of the string
    assert matches == ['HELLO']

def test_lazy_regex_in_class():
    class MyClass:
        def __init__(self):
            self.lazy_regex = LazyRegex(r'\d+')

    obj = MyClass()
    matches = obj.lazy_regex.findall("123abc")  # The regex is now compiled and used to find all digit sequences in the string
    assert matches == ['123']

# Additional test cases for _real_re_compile function
def test_real_re_compile():
    pattern = r'\d+'
    compiled_regex = compile_regex(pattern)
    assert isinstance(compiled_regex, re.Pattern)

def test_invalid_pattern():
    with pytest.raises(InvalidPattern):
        compile_regex('[invalid-pattern')  # This should raise an InvalidPattern error

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_lazy_lazy_regex_LazyRegex__real_re_compile_0
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_LazyRegex__real_re_compile_0.py:18:17: E1123: Unexpected keyword argument 'ignorecase' in constructor call (unexpected-keyword-arg)
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_LazyRegex__real_re_compile_0.py:29:17: E1123: Unexpected keyword argument 'multiline' in constructor call (unexpected-keyword-arg)
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_LazyRegex__real_re_compile_0.py:29:17: E1123: Unexpected keyword argument 'dotall' in constructor call (unexpected-keyword-arg)


"""