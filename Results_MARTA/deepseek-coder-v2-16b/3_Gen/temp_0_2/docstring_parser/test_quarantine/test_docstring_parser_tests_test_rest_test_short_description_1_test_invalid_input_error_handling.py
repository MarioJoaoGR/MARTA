
import pytest
from docstring_parser.tests.test_rest import parse

def test_short_description(source: T.Optional[str], expected: T.Optional[str]) -> None:
    """Test parsing short description."""
    with pytest.raises(ValueError):
        docstring = parse(source)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_rest_test_short_description_1_test_invalid_input_error_handling
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_short_description_1_test_invalid_input_error_handling.py:5:35: E0602: Undefined variable 'T' (undefined-variable)
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_short_description_1_test_invalid_input_error_handling.py:5:62: E0602: Undefined variable 'T' (undefined-variable)


"""