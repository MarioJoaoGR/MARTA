
import pytest
from isort._vendored.tomli._parser import TOMLDecodeError

def suffixed_err(src: str, pos: int, msg: str) -> TOMLDecodeError:
    """Return a `TOMLDecodeError` where error message is suffixed with coordinates in source."""

    def coord_repr(src: str, pos: int) -> str:
        if pos >= len(src):
            return "end of document"
        line = src.count("\n", 0, pos) + 1
        if line == 1:
            column = pos + 1
        else:
            column = pos - src.rindex("\n", 0, pos)
        return f"line {line}, column {column}"

    return TOMLDecodeError(f"{msg} (at {coord_repr(src, pos)})")

def test_suffixed_err_basic():
    src = "key=value"
    pos = 4
    msg = "Test error message"
    
    err = suffixed_err(src, pos, msg)
    
    assert str(err) == f"{msg} (at line 1, column 5)"
