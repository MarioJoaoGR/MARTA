
# Module: pytutils.lazy.lazy_regex
import pytest
import re
from pytutils.lazy.lazy_regex import LazyRegex

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

# Test accessing an attribute that triggers compilation
def test_getattr_triggers_compilation():
    lazy_regex = LazyRegex(r'\d+')
    with pytest.raises(AttributeError):
        # This should raise an AttributeError because _real_regex is None and the attribute doesn't exist yet
        getattr(lazy_regex, 'findall')
    
    # After accessing __getattr__, _real_regex should be compiled
    lazy_regex.findall("123abc")
    assert isinstance(lazy_regex._real_regex, re.Pattern)

# Test using findall method after initialization and compilation
def test_findall():
    lazy_regex = LazyRegex(r'\d+')
    matches = lazy_regex.findall("123abc")
    assert matches == ['123']

# Test using findall with case-insensitive regex
def test_findall_case_insensitive():
    lazy_regex = LazyRegex(r'\d+', ignorecase=True)
    matches = lazy_regex.findall("abc123")
    assert matches == ['123']

# Test accessing a compiled attribute directly
def test_accessing_compiled_attribute():
    lazy_regex = LazyRegex(r'\d+')
    # Access an attribute that should trigger compilation
    compiled_regex = lazy_regex._real_regex
    assert isinstance(compiled_regex, re.Pattern)
    assert compiled_regex.pattern == r'\d+'

# Test using findall with a different regex pattern
def test_findall_different_pattern():
    lazy_regex = LazyRegex(r'[a-z]+')
    matches = lazy_regex.findall("hello world")
    assert matches == ['hello', 'world']

# Test initialization with an invalid regex pattern
def test_init_with_invalid_regex():
    with pytest.raises(re.error):
        LazyRegex(r'\d+*')  # Invalid regex pattern, should raise a re.error

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_lazy_lazy_regex_LazyRegex___getattr___0
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_LazyRegex___getattr___0.py:16:17: E1123: Unexpected keyword argument 'ignorecase' in constructor call (unexpected-keyword-arg)
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_LazyRegex___getattr___0.py:40:17: E1123: Unexpected keyword argument 'ignorecase' in constructor call (unexpected-keyword-arg)


"""