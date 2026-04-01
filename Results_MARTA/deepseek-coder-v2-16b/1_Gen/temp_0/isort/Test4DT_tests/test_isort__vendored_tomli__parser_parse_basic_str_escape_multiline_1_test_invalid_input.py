
from isort._vendored.tomli._parser import parse_basic_str_escape
from isort._vendored.tomli._parser import Pos
import pytest

def test_invalid_input():
    with pytest.raises(ValueError):
        # This input string contains an invalid escape sequence that will cause a parsing error
        src = 'This is a test string with an invalid \\u1234 escape sequence.'
        parse_basic_str_escape(src, Pos(0))
