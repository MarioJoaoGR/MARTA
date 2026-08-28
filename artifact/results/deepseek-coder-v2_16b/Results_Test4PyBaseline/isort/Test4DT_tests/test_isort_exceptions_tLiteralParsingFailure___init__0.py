# Module: isort.exceptions
import pytest
from isort.exceptions import LiteralParsingFailure

# Test raising the exception with a custom literal and error
def test_literal_parsing_failure():
    with pytest.raises(LiteralParsingFailure) as exc_info:
        raise LiteralParsingFailure("incorrect_literal", ValueError("parsing failed"))
    
    assert isinstance(exc_info.value, LiteralParsingFailure)
    assert exc_info.value.code == "incorrect_literal"
    assert str(exc_info.value.original_error) == "parsing failed"

# Test raising the exception with a different literal and error
def test_literal_parsing_failure_different():
    with pytest.raises(LiteralParsingFailure) as exc_info:
        raise LiteralParsingFailure("incorrect_syntax", SyntaxError("parsing failed"))
    
    assert isinstance(exc_info.value, LiteralParsingFailure)
    assert exc_info.value.code == "incorrect_syntax"
    assert str(exc_info.value.original_error) == "parsing failed"
