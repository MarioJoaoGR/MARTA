
# Module: pytutils.lazy.lazy_regex
import re
from pytutils.lazy import LazyRegex
import pytest

# Import the function from the module
from pytutils.lazy.lazy_regex import finditer_public

def test_basic_usage():
    pattern = r'\d+'
    string = '123abc456'
    matches = finditer_public(pattern, string)
    match_list = list(matches)
    assert len(match_list) == 2, "Expected 2 matches for the pattern '\\d+' in the string '123abc456'"
    assert str(match_list[0].group()) == '123', "First match should be '123' for the pattern '\\d+'"
    assert str(match_list[1].group()) == '456', "Second match should be '456' for the pattern '\\d+'"

def test_lazy_regex():
    lazy_pattern = LazyRegex(lambda: re.compile(r'\d+'))
    matches = finditer_public(lazy_pattern, '123abc456')
    match_list = list(matches)
    assert len(match_list) == 2, "Expected 2 matches for the pattern '\\d+' in the string '123abc456' when using LazyRegex"
    assert str(match_list[0].group()) == '123', "First match should be '123' for the pattern '\\d+' with LazyRegex"
    assert str(match_list[1].group()) == '456', "Second match should be '456' for the pattern '\\d+' with LazyRegex"

def test_specifying_flags():
    flags = re.IGNORECASE
    matches = finditer_public(r'\b\w+\b', 'hello world', flags)
    match_list = list(matches)
    assert len(match_list) == 2, "Expected 2 matches for the pattern '\\b\\w+\\b' in the string 'hello world' with IGNORECASE flag"
    assert str(match_list[0].group()) == 'hello', "First match should be 'hello' for the pattern '\\b\\w+\\b' with IGNORECASE"
    assert str(match_list[1].group()) == 'world', "Second match should be 'world' for the pattern '\\b\\w+\\b' with IGNORECASE"

def test_invalid_pattern():
    pattern = 123  # Invalid pattern type, should raise a TypeError
    string = 'validstring'
    with pytest.raises(TypeError):
        finditer_public(pattern, string)

def test_no_matches():
    pattern = r'\d+'
    string = 'abcdef'
    matches = finditer_public(pattern, string)
    match_list = list(matches)
    assert len(match_list) == 0, "Expected no matches for the pattern '\\d+' in the string 'abcdef'"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_lazy_lazy_regex_finditer_public_0
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_finditer_public_0.py:4:0: E0611: No name 'LazyRegex' in module 'pytutils.lazy' (no-name-in-module)


"""