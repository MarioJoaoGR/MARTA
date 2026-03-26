
import pytest
from isort._vendored.tomli._parser import TOMLDecodeError

def suffixed_err(src: str, pos: int, msg: str) -> TOMLDecodeError:
    """Return a `TOMLDecodeError` where error message is suffixed with coordinates in source."""
    
    def coord_repr(src: str, pos: int) -> str:
        if pos >= len(src):
            return "end of document"
        line = src.count("\n", 0, pos) + 1
        column = pos - src.rindex("\n", 0, pos) if line > 1 else pos + 1
        return f"line {line}, column {column}"
    
    error_msg = f"{msg} (at {coord_repr(src, pos)})"
    raise TOMLDecodeError(error_msg)

def test_invalid_input():
    src = "def example():\n    return x\n"
    pos = 10
    msg = "Unexpected token 'x'"
    
    with pytest.raises(TOMLDecodeError):
        suffixed_err(src, pos, msg)
