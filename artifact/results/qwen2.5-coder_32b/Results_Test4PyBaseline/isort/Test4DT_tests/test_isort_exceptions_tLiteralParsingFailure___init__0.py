# Module: isort.exceptions
import pytest
from isort.exceptions import LiteralParsingFailure

def test_literal_parsing_failure_initialization():
    # Test with a dictionary literal that has a syntax error
    code1 = "{'key': 'value',}"
    original_error1 = ValueError("malformed node or string")
    with pytest.raises(LiteralParsingFailure) as excinfo:
        raise LiteralParsingFailure(code1, original_error1)
    assert str(excinfo.value) == (f"isort failed to parse the given literal {code1}. "
                                  "It's important to note that isort literal sorting only supports simple literals parsable by ast.literal_eval which gave the exception of malformed node or string.")
    assert excinfo.value.code == code1
    assert isinstance(excinfo.value.original_error, ValueError)
    assert str(excinfo.value.original_error) == "malformed node or string"

    # Test with an unsupported complex data structure
    code2 = "[1, 2, {3, 4}]"
    original_error2 = TypeError("unhashable type: 'set'")
    with pytest.raises(LiteralParsingFailure) as excinfo:
        raise LiteralParsingFailure(code2, original_error2)
    assert str(excinfo.value) == (f"isort failed to parse the given literal {code2}. "
                                  "It's important to note that isort literal sorting only supports simple literals parsable by ast.literal_eval which gave the exception of unhashable type: 'set'.")
    assert excinfo.value.code == code2
    assert isinstance(excinfo.value.original_error, TypeError)
    assert str(excinfo.value.original_error) == "unhashable type: 'set'"

    # Test with a string that is not a valid literal
    code3 = "not_a_literal"
    original_error3 = SyntaxError("invalid syntax")
    with pytest.raises(LiteralParsingFailure) as excinfo:
        raise LiteralParsingFailure(code3, original_error3)
    assert str(excinfo.value) == (f"isort failed to parse the given literal {code3}. "
                                  "It's important to note that isort literal sorting only supports simple literals parsable by ast.literal_eval which gave the exception of invalid syntax.")
    assert excinfo.value.code == code3
    assert isinstance(excinfo.value.original_error, SyntaxError)
    assert str(excinfo.value.original_error) == "invalid syntax"
