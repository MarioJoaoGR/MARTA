
import pytest
from isort.exceptions import LiteralParsingFailure

def test_valid_input():
    code = '1'
    try:
        # Simulate isort trying to parse the given code string, which should raise a LiteralParsingFailure
        raise LiteralParsingFailure(code=code, original_error=ValueError("Test error"))
    except LiteralParsingFailure as e:
        assert e.code == code
        assert str(e.original_error) == "Test error"
