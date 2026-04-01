
import pytest
from docstring_parser import parse

def test_raises() -> None:
    """Test parsing raises."""
    with pytest.raises(TypeError):
        parse("""\nInvalid Docstring\nRaises:\n    TypeError: unexpected type")

    docstring = parse(
        """
        Short description
        Raises:
            ValueError: description
        """
    )
    assert len(docstring.raises) == 1
    assert docstring.raises[0].type_name == "ValueError"
    assert docstring.raises[0].description == "description"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_google_test_raises_2_test_invalid_input_error_handling
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_raises_2_test_invalid_input_error_handling.py:15:9: E0001: Parsing failed: 'unterminated triple-quoted string literal (detected at line 20) (Test4DT_tests.test_docstring_parser_tests_test_google_test_raises_2_test_invalid_input_error_handling, line 15)' (syntax-error)


"""