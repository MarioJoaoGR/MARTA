
import pytest
from unittest.mock import patch
from youtube_dl.jsinterp import JSInterpreter, ExtractorError


def test_edge_case():
    interpreter = JSInterpreter("")
    with pytest.raises(ExtractorError):
        interpreter.call_function('nonExistentFunction')

def test_invalid_input():
    interpreter = JSInterpreter("function add(a, b) { return a + b; }")
    with pytest.raises(ExtractorError):
        interpreter.call_function('nonExistentFunction')