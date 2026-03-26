
import pytest
from isort.exceptions import LiteralParsingFailure
import ast

def test_valid_input():
    # Test with a simple literal string that should be parsable by ast.literal_eval
    code = "[1, 2, 3]"
    
    try:
        parsed_literal = ast.literal_eval(code)
    except Exception as e:
        with pytest.raises(LiteralParsingFailure) as exc_info:
            raise LiteralParsingFailure(code, type(e))
        assert str(exc_info.value) == f"isort failed to parse the given literal {code}. It's important to note that isort literal sorting only supports simple literals parsable by ast.literal_eval which gave the exception of {type(e)}."
