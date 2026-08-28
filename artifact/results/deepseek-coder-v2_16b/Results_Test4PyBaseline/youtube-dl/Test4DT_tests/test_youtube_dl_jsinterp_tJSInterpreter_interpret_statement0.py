
# Module: youtube_dl.jsinterp
import pytest
from youtube_dl.jsinterp import JSInterpreter
from pytest import raises  # Importing from pytest for clarity and consistency

# Test initialization of JSInterpreter with default objects
def test_init_default_objects():
    interpreter = JSInterpreter("code")
    assert interpreter._functions == {}
    assert interpreter._objects == {}

# Test initialization of JSInterpreter with provided objects
def test_init_provided_objects():
    provided_objects = {"print": print}
    interpreter = JSInterpreter("code", provided_objects)
    assert interpreter._functions == {}
    assert interpreter._objects == provided_objects

# Test interpret_statement with a variable declaration
def test_interpret_var_declaration():
    interpreter = JSInterpreter("")
    stmt = "let x = 5;"
    local_vars = {}
    result, should_abort = interpreter.interpret_statement(stmt, local_vars)
    assert result is None, f"Expected result to be None but got {result}"
    assert not should_abort, f"Expected should_abort to be False but got {should_abort}"

# Test interpret_statement with a return statement
def test_interpret_return_statement():
    interpreter = JSInterpreter("")
    stmt = "return x + 3;"
    local_vars = {"x": 5}
    result, should_abort = interpreter.interpret_statement(stmt, local_vars)
    assert result == 8, f"Expected result to be 8 but got {result}"
    assert should_abort, f"Expected should_abort to be True but got {should_abort}"

# Test interpret_statement with a complex expression
def test_interpret_complex_expression():
    interpreter = JSInterpreter("")
    stmt = "let y = (x * 2) + (z || 0);"
    local_vars = {"x": 5, "z": 10}
    result, should_abort = interpreter.interpret_statement(stmt, local_vars)