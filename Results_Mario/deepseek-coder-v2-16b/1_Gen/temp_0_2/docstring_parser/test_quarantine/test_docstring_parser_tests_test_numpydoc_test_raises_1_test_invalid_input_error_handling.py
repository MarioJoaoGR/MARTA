
import pytest
from your_module import parse

def test_raises() -> None:
    """Test parsing raises."""
    docstring = parse(
        """
        Short description
        Raises
        ------
        ValueError
            description
        """
    )
    assert len(docstring.raises) == 1
    assert docstring.raises[0].type_name == "ValueError"
    assert docstring.raises[0].description == "description"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_numpydoc_test_raises_1_test_invalid_input_error_handling
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_raises_1_test_invalid_input_error_handling.py:3:0: E0401: Unable to import 'your_module' (import-error)


"""