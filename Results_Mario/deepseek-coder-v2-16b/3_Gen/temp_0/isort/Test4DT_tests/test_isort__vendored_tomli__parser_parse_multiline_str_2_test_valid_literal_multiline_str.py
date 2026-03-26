
import pytest
from isort._vendored.tomli._parser import parse_multiline_str, skip_until
from isort._vendored.tomli._parser import TOMLDecodeError, ILLEGAL_MULTILINE_LITERAL_STR_CHARS
from isort._vendored.tomli._parser import Pos

def test_valid_literal_multiline_str():
    src = "'''This is a test string"
    pos = Pos(0)
    
    with pytest.raises(TOMLDecodeError):
        parse_multiline_str(src, pos, literal=True)
