
import pytest
from youtube_dl.jsinterp import JSInterpreter

# Test initialization with a simple JavaScript-like code string
def test_initialization_with_simple_code():
    interpreter = JSInterpreter("print('Hello, World!');")
    assert interpreter.code == "print('Hello, World!');"
    assert interpreter._objects == {}

# Test initialization with an objects dictionary containing the print function
def test_initialization_with_objects_dictionary():
    interpreter = JSInterpreter("print('Hello, World!');", {"print": print})
    assert interpreter.code == "print('Hello, World!');"
    assert interpreter._objects == {'print': print}

# Test call_function method with a valid function name and arguments
def test_call_function_valid_function():
    interpreter = JSInterpreter("function add(a, b) { return a + b; }", {"add": lambda a, b: a + b})
    result = interpreter.call_function("add", 2, 3)