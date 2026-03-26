
import pytest
from isort._vendored.tomli._parser import parse_basic_str, Pos

def test_invalid_input():
    with pytest.raises(ValueError) as excinfo:
        parse_basic_str('hello world', Pos(0), multiline=False)
    assert str(excinfo.value) == "Unterminated string (at end of document)"
