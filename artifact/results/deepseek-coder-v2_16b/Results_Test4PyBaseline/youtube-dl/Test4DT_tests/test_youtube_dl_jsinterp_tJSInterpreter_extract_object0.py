
import pytest
from youtube_dl.jsinterp import JSInterpreter

# Test initialization with default objects
def test_init_default_objects():
    interpreter = JSInterpreter("print('Hello, World!');")
    assert interpreter._functions == {}
    assert interpreter._objects == {}

# Test initialization with provided objects
def test_init_provided_objects():
    interpreter = JSInterpreter("print('Hello, World!');", {"print": print})