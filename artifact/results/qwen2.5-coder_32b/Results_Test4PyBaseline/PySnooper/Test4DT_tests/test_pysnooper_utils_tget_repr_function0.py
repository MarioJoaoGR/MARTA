# Module: pysnooper.utils
import pytest
from pysnooper.utils import get_repr_function

def test_get_repr_function_with_custom_int_repr():
    def custom_int_repr(x):
        return f"Integer: {x}"
    
    custom_repr = [(int, custom_int_repr)]
    repr_func = get_repr_function(123, custom_repr)
    assert repr_func(123) == "Integer: 123"

def test_get_repr_function_with_custom_str_repr():
    def custom_str_repr(x):
        return f"String: '{x}'"
    
    custom_repr = [(str, custom_str_repr)]
    repr_func = get_repr_function("hello", custom_repr)
    assert repr_func("hello") == "String: 'hello'"

def test_get_repr_function_with_custom_list_repr():
    def custom_list_repr(x):
        return f"List: {x}"
    
    custom_repr = [(list, custom_list_repr)]
    repr_func = get_repr_function([1, 2, 3], custom_repr)
    assert repr_func([1, 2, 3]) == "List: [1, 2, 3]"

def test_get_repr_function_with_lambda_condition():
    def long_list_repr(x):
        return f"Long List: {x}"
    
    custom_repr = [(lambda x: isinstance(x, list) and len(x) > 2, long_list_repr)]
    repr_func = get_repr_function([1, 2, 3, 4], custom_repr)
    assert repr_func([1, 2, 3, 4]) == "Long List: [1, 2, 3, 4]"

def test_get_repr_function_no_matching_condition():
    def custom_int_repr(x):
        return f"Integer: {x}"
    
    custom_repr = [(int, custom_int_repr)]
    repr_func = get_repr_function("hello", custom_repr)
    assert repr_func("hello") == "'hello'"

def test_get_repr_function_with_multiple_conditions():
    def custom_int_repr(x):
        return f"Integer: {x}"
    
    def custom_str_repr(x):
        return f"String: '{x}'"
    
    custom_repr = [
        (int, custom_int_repr),
        (str, custom_str_repr)
    ]
    
    repr_func1 = get_repr_function(123, custom_repr)
    assert repr_func1(123) == "Integer: 123"
    
    repr_func2 = get_repr_function("hello", custom_repr)
    assert repr_func2("hello") == "String: 'hello'"

def test_get_repr_function_with_no_custom_repr():
    repr_func = get_repr_function([1, 2, 3], [])
    assert repr_func([1, 2, 3]) == "[1, 2, 3]"
