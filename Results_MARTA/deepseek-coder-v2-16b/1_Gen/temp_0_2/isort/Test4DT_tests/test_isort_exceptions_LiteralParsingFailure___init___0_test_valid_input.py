
import pytest
from isort.exceptions import LiteralParsingFailure

def test_valid_input():
    code = "some_literal"
    original_error = ValueError("Unable to parse")
    
    try:
        raise LiteralParsingFailure(code, original_error)
    except LiteralParsingFailure as e:
        assert e.code == code
        assert isinstance(e.original_error, type(original_error))
        assert str(e.original_error) == "Unable to parse"
