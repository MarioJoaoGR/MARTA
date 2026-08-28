
import pytest
from youtube_dl.jsinterp import JSInterpreter
from pytest import raises  # Importing raises from pytest for clarity and consistency

# Assuming the module is correctly imported as described in the function documentation

@pytest.fixture
def interpreter():
    return JSInterpreter("let x = 5; let y = x + 3;", {"print": print})

def test_interpret_expression_basic(interpreter):
    result = interpreter.interpret_expression('5 + 3', {'x': 5}, allow_recursion=10)
    assert result == 8, f"Expected 8 but got {result}"

def test_interpret_expression_variable_access(interpreter):
    result = interpreter.interpret_expression('x + 3', {'x': 5}, allow_recursion=10)
    assert result == 8, f"Expected 8 but got {result}"

def test_interpret_expression_function_call(interpreter):
    # Assuming the function is defined as per Example 3 in the documentation
    interpreter = JSInterpreter("function add(a, b) { return a + b; }", {"add": lambda a, b: a + b})
    result = interpreter.interpret_expression('add(2, 3)', {}, allow_recursion=10)
    assert result == 5, f"Expected 5 but got {result}"

def test_interpret_expression_object_property_access(interpreter):
    # Assuming the object is defined as per Example 4 in the documentation
    interpreter = JSInterpreter("obj = { value: 10 };", {"obj": {"value": 10}})
    result = interpreter.interpret_expression('obj.value', {'obj': {'value': 10}}, allow_recursion=10)
    assert result == 10, f"Expected 10 but got {result}"

def test_interpret_expression_complex_expression(interpreter):
    result = interpreter.interpret_expression('(2 * (3 + 4)) / 2 - 1', {}, allow_recursion=10)