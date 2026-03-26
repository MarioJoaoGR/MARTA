
# Module: pytutils.lazy.lazy_regex
import pytest
from pytutils.lazy.lazy_regex import LazyRegex
import re

# Test initialization with default arguments
def test_init_default():
    lazy_regex = LazyRegex()
    assert lazy_regex._real_regex is None
    assert lazy_regex._regex_args == ()
    assert lazy_regex._regex_kwargs == {}

# Test initialization with provided args and kwargs
def test_init_with_args_and_kwargs():
    lazy_regex = LazyRegex(r'\d+', ignorecase=True)
    assert lazy_regex._real_regex is None
    assert lazy_regex._regex_args == (r'\d+',)
    assert lazy_regex._regex_kwargs == {'ignorecase': True}

# Test accessing _real_regex after initialization
def test_accessing_real_regex():
    lazy_regex = LazyRegex(r'\d+', ignorecase=True)
    compiled_regex = lazy_regex.get_compiled_regex()  # This should trigger compilation
    assert isinstance(compiled_regex, re.Pattern)
    assert compiled_regex.pattern == r'\d+'
    assert compiled_regex.flags & re.IGNORECASE != 0

# Test findall method
def test_findall():
    lazy_regex = LazyRegex(r'\d+', ignorecase=True)
    matches = lazy_regex.findall("123abc")
    assert matches == ['123']

# Test match method
def test_match():
    lazy_regex = LazyRegex(r'\d+', ignorecase=True)
    match_obj = lazy_regex.match("123abc")
    assert match_obj is not None
    assert match_obj.group() == '123'

# Test search method
def test_search():
    lazy_regex = LazyRegex(r'\d+', ignorecase=True)
    match_obj = lazy_regex.search("123abc")
    assert match_obj is not None
    assert match_obj.group() == '123'

# Test split method
def test_split():
    lazy_regex = LazyRegex(r'\d+', ignorecase=True)
    splits = lazy_regex.split("123abc")
    assert splits == ['', 'abc']

# Test sub method
def test_sub():
    lazy_regex = LazyRegex(r'\d+', ignorecase=True)
    result = lazy_regex.sub('X', "123abc")
    assert result == 'Xbc'

# Test subn method
def test_subn():
    lazy_regex = LazyRegex(r'\d+', ignorecase=True)
    result, count = lazy_regex.subn('X', "123abc")
    assert result == 'Xbc'
    assert count == 1

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_lazy_lazy_regex_LazyRegex___init___0
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_LazyRegex___init___0.py:16:17: E1123: Unexpected keyword argument 'ignorecase' in constructor call (unexpected-keyword-arg)
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_LazyRegex___init___0.py:23:17: E1123: Unexpected keyword argument 'ignorecase' in constructor call (unexpected-keyword-arg)
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_LazyRegex___init___0.py:31:17: E1123: Unexpected keyword argument 'ignorecase' in constructor call (unexpected-keyword-arg)
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_LazyRegex___init___0.py:37:17: E1123: Unexpected keyword argument 'ignorecase' in constructor call (unexpected-keyword-arg)
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_LazyRegex___init___0.py:44:17: E1123: Unexpected keyword argument 'ignorecase' in constructor call (unexpected-keyword-arg)
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_LazyRegex___init___0.py:51:17: E1123: Unexpected keyword argument 'ignorecase' in constructor call (unexpected-keyword-arg)
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_LazyRegex___init___0.py:57:17: E1123: Unexpected keyword argument 'ignorecase' in constructor call (unexpected-keyword-arg)
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_LazyRegex___init___0.py:63:17: E1123: Unexpected keyword argument 'ignorecase' in constructor call (unexpected-keyword-arg)


"""