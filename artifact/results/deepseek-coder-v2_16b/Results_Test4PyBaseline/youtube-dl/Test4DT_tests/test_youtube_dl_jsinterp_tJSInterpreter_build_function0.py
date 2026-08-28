
import pytest
from youtube_dl.jsinterp import JSInterpreter

# Test initialization with default objects
def test_init_default_objects():
    interpreter = JSInterpreter("code")
    assert interpreter.code == "code"
    assert interpreter._functions == {}
    assert interpreter._objects == {}

# Test initialization with provided objects
def test_init_with_objects():
    interpreter = JSInterpreter("code", {"print": print})
    assert interpreter.code == "code"
    assert interpreter._functions == {}
    assert interpreter._objects == {"print": print}

# Test build_function with simple code
def test_build_function_simple():
    interpreter = JSInterpreter("code", {"print": print})
    func = interpreter.build_function(['x'], "x = 5; return x;")
    result = func([0])
    assert result == 5

# Test build_function with multiple statements
def test_build_function_multiple_statements():
    interpreter = JSInterpreter("code", {"print": print})
    func = interpreter.build_function(['y', 'z'], "x = y + z; return x;")
    result = func([3, 4])