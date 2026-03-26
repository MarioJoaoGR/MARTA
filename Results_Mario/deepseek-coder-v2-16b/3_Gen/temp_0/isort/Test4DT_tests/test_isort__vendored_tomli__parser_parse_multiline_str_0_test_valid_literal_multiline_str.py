
import pytest
from isort._vendored.tomli._parser import parse_multiline_str, Pos

def test_valid_literal_multiline_str():
    src = "'''Hello\nWorld'''"
    pos = Pos(0)
    result = parse_multiline_str(src, pos, literal=True)
    assert result == (pos + len(src), "Hello\nWorld")
