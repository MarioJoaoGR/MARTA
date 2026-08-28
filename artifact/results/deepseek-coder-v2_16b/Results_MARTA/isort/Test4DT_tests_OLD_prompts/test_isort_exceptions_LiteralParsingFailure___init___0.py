
import pytest
from isort.exceptions import LiteralParsingFailure

def test_valid_inputs():
    with pytest.raises(LiteralParsingFailure) as exc_info:
        raise LiteralParsingFailure("valid_literal", ValueError("Parsing error"))
    assert str(exc_info.value) == "isort failed to parse the given literal valid_literal. It's important to note that isort literal sorting only supports simple literals parsable by ast.literal_eval which gave the exception of Parsing error."

def test_edge_cases():
    with pytest.raises(LiteralParsingFailure) as exc_info:
        raise LiteralParsingFailure("edge_case", ValueError("Edge case parsing error"))
    assert str(exc_info.value) == "isort failed to parse the given literal edge_case. It's important to note that isort literal sorting only supports simple literals parsable by ast.literal_eval which gave the exception of Edge case parsing error."

def test_invalid_inputs():
    with pytest.raises(LiteralParsingFailure) as exc_info:
        raise LiteralParsingFailure("invalid_literal", TypeError("Invalid type"))
    assert str(exc_info.value) == "isort failed to parse the given literal invalid_literal. It's important to note that isort literal sorting only supports simple literals parsable by ast.literal_eval which gave the exception of Invalid type."
