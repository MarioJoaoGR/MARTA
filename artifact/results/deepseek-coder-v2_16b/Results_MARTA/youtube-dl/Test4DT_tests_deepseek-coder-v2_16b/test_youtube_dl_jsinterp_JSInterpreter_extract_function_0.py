
import pytest
from youtube_dl.jsinterp import JSInterpreter, ExtractorError



def test_invalid_function():
    with pytest.raises(ExtractorError):
        interpreter = JSInterpreter("function add(a, b) { return a + b; }")
        interpreter.extract_function('subtract')