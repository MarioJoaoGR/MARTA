
import pytest
from isort.exceptions import LiteralParsingFailure

def test_edge_cases_none():
    problematic_code = None
    original_error = SyntaxError("unexpected EOF while parsing")
    
    with pytest.raises(LiteralParsingFailure) as excinfo:
        raise LiteralParsingFailure(str(problematic_code), original_error)
    
    assert str(excinfo.value) == (
        "isort failed to parse the given literal None. It's important to note "
        "that isort literal sorting only supports simple literals parsable by ast.literal_eval which gave the exception of unexpected EOF while parsing."
    )

def test_invalid_inputs_unsupported_data_structure():
    problematic_code = "{1, 2}"
    original_error = SyntaxError("invalid syntax")
    
    with pytest.raises(LiteralParsingFailure) as excinfo:
        raise LiteralParsingFailure(problematic_code, original_error)
    
    assert str(excinfo.value) == (
        "isort failed to parse the given literal {1, 2}. It's important to note "
        "that isort literal sorting only supports simple literals parsable by ast.literal_eval which gave the exception of invalid syntax."
    )

def test_malformed_dictionary_literal():
    problematic_code = "{'key': 'value',"
    original_error = ValueError("malformed node or string: unexpected EOF while parsing")
    
    with pytest.raises(LiteralParsingFailure) as excinfo:
        raise LiteralParsingFailure(problematic_code, original_error)
    
    assert str(excinfo.value) == (
        "isort failed to parse the given literal {'key': 'value',. It's important to note "
        "that isort literal sorting only supports simple literals parsable by ast.literal_eval which gave the exception of malformed node or string: unexpected EOF while parsing."
    )

def test_incorrect_list_literal():
    problematic_code = "[1, 2, 3,"
    original_error = SyntaxError("unexpected EOF while parsing")
    
    with pytest.raises(LiteralParsingFailure) as excinfo:
        raise LiteralParsingFailure(problematic_code, original_error)
    
    assert str(excinfo.value) == (
        "isort failed to parse the given literal [1, 2, 3,. It's important to note "
        "that isort literal sorting only supports simple literals parsable by ast.literal_eval which gave the exception of unexpected EOF while parsing."
    )
