
from isort.exceptions import LiteralParsingFailure
import pytest

def test_invalid_input():
    with pytest.raises(LiteralParsingFailure) as excinfo:
        # This will cause an error since lists are not parsable by ast.literal_eval
        literal = "[1, [2, 3], 4]"
        parsed_literal = ast.literal_eval(literal)
    
    assert str(excinfo.value) == "isort failed to parse the given literal [1, [2, 3], 4]. It's important to note that isort literal sorting only supports simple literals parsable by ast.literal_eval which gave the exception of <class 'ValueError'>."

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_exceptions_LiteralParsingFailure___init___1_test_invalid_input
isort/Test4DT_tests/test_isort_exceptions_LiteralParsingFailure___init___1_test_invalid_input.py:9:25: E0602: Undefined variable 'ast' (undefined-variable)


"""