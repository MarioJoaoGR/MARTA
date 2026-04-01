
import pytest
from isort.exceptions import LiteralParsingFailure

def test_edge_case_none():
    code = None
    original_error = ValueError("Unable to parse")
    
    with pytest.raises(LiteralParsingFailure) as exc_info:
        raise LiteralParsingFailure(code, original_error)
    
    assert str(exc_info.value) == (
        f"isort failed to parse the given literal {code}. It's important to note "
        "that isort literal sorting only supports simple literals parsable by "
        f"ast.literal_eval which gave the exception of {original_error}."
    )
