
# Module: youtube_dl.jsinterp
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