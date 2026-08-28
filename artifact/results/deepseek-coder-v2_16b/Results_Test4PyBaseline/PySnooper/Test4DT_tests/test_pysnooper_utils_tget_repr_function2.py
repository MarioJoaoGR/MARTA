
import pytest
from pysnooper.utils import get_repr_function

# Test cases for get_repr_function

def test_get_repr_function_basic():
    result = get_repr_function(42, [(int, lambda x: f"Int({x}"), (lambda x: isinstance(x, str), lambda x: f"Str({x}")])
    assert callable(result)
    assert repr(42) == "42"  # Built-in repr for int

def test_get_repr_function_string():
    result = get_repr_function("hello", [(str, lambda x: f"CustomStr({x}"), (len, lambda x: len(x) > 5 and f"LongStr({x}")])
    assert callable(result)
    assert repr("hello") == "'hello'"  # Built-in repr for str

def test_get_repr_function_custom_obj():
    custom_obj = {"type": "example", "value": [1, 2, 3]}
    result = get_repr_function(custom_obj, [(dict, lambda x: f"Dict({x}"), (lambda x: isinstance(x.get("type"), str) and x["type"] == "example", lambda x: f"ExampleDict({x})")])
    assert callable(result)

# Additional test cases to cover line 56 and edge cases

def test_get_repr_function_default():
    result = get_repr_function("test", [(int, "Int"), (str, "Str")])