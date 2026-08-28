
import pytest
from youtube_dl.jsinterp import JSInterpreter


def test_invalid_input():
    with pytest.raises(KeyError):
        interpreter = JSInterpreter("function multiply(a, b) { return a * b; } var result = multiply(5, 3);")
        assert 'multiply' in str(interpreter._functions['multiply'])