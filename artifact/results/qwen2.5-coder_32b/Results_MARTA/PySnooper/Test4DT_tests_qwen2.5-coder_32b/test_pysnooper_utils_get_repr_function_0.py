
import pytest

def get_repr_function(item, custom_repr):
    for condition, action in custom_repr:
        if isinstance(condition, type):
            condition = lambda x, y=condition: isinstance(x, y)
        if condition(item):
            return action
    return repr

# Test file containing one test function per scenario

def test_get_repr_function_basic():
    def custom_repr_int(x):
        return f"Integer: {x}"

    conditions = [(int, custom_repr_int)]
    repr_func = get_repr_function(42, conditions)
    assert repr_func(42) == 'Integer: 42'
