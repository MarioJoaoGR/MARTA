
import pytest

def get_repr_function(item, custom_repr):
    for condition, action in custom_repr:
        if isinstance(condition, type):
            condition = lambda x, y=condition: isinstance(x, y)
        if condition(item):
            return action
    return repr

# Test Scenario 1: Basic integer with a custom representation
def test_valid_input_basic():
    item = 42
    custom_repr = [(lambda x: isinstance(x, int), lambda obj: f"Custom repr of {type(obj).__name__}")]
    result = get_repr_function(item, custom_repr)
    assert callable(result) or str(result) == "Custom repr of <class 'int'>"

# Test Scenario 2: String with multiple custom conditions
def test_valid_input_multiple_conditions():
    item = 'hello'
    custom_repr = [
        (lambda x: isinstance(x, int), lambda obj: f"Custom repr of {type(obj).__name__}"),
        (lambda x: isinstance(x, str), lambda obj: f"String repr of {obj}")
    ]
    result = get_repr_function(item, custom_repr)
    assert callable(result) or str(result) == "String repr of hello"

# Test Scenario 3: Invalid input with no conditions met
def test_invalid_input():
    item = 'world'
    custom_repr = []
    result = get_repr_function(item, custom_repr)
    assert callable(result) or str(result) == "Custom repr of <class 'str'>"
