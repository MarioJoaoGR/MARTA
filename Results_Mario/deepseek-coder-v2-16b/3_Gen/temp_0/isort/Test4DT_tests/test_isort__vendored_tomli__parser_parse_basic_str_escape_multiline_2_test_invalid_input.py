
from isort._vendored.tomli._parser import parse_basic_str_escape
from isort._vendored.tomli._parser import Pos
import pytest

def test_invalid_input():
    with pytest.raises(ValueError):
        # This input string contains an invalid escape sequence that will cause a parsing failure
        src = r'This is a test \u1234 string with an invalid unicode escape'
        parse_basic_str_escape(src, Pos(0))
