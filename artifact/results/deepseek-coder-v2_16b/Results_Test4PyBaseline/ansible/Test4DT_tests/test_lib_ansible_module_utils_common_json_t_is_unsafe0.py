
import pytest
from ansible.module_utils.common.json import _is_unsafe

# Test cases for _is_unsafe function

def test_is_unsafe_with_both_attributes():
    class TestValue:
        def __init__(self):
            self.__UNSAFE__ = True
            self.__ENCRYPTED__ = False
    
    test_value = TestValue()
    assert _is_unsafe(test_value) == True, "Expected True because both attributes are set"

def test_is_unsafe_with_only_one_attribute():
    class SafeValue:
        def __init__(self):
            self.__UNSAFE__ = False
            self.__ENCRYPTED__ = True
    
    safe_value = SafeValue()
    assert _is_unsafe(safe_value) == False, "Expected False because only one attribute is set"

def test_is_unsafe_with_simple_object():
    class SimpleObject:
        def __init__(self):
            self.__UNSAFE__ = True
    
    simple_object = SimpleObject()
    assert _is_unsafe(simple_object) == True, "Expected True because the attribute is set"

def test_is_unsafe_with_dict_like():
    class DictLike:
        def __init__(self):
            self.__UNSAFE__ = False
    
    dict_like = DictLike()
    assert _is_unsafe(dict_like) == False, "Expected False because the attribute is not set"

def test_is_unsafe_with_str_like():
    class StrLike:
        def __init__(self):
            self.__UNSAFE__ = True
    
    str_like = StrLike()