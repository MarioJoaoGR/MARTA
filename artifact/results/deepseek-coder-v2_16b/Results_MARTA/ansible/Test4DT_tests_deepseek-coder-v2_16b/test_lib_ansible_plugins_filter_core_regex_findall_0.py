
import re
from ansible.plugins.filter.core import regex_findall
import pytest

def test_regex_findall_basic():
    # Test basic functionality without any special flags
    assert regex_findall("hello world", r"o") == ['o']
    
    # Test case-insensitive search
    assert regex_findall("hello world", r"[a-z]+", ignorecase=True) == ['hello', 'world']
    
    # Test multiline search
    assert regex_findall("hello\nworld", r".+", multiline=True) == ['hello', 'world']
    
    # Test mixed parameters
    assert regex_findall("Hello World!", r"[a-z]+", ignorecase=True, multiline=False) == ['ello', 'orld']
    
    # Test handling non-string values
    assert regex_findall(12345, r"\d") == ['1', '2', '3', '4', '5']
    
    # Test error handling for non-string types
    with pytest.raises(TypeError):
        regex_findall("hello world", r"\d", errors="surrogate_or_strict")
