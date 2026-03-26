
import pytest
from docstring_parser import parse

def test_raises() -> None:
    """Test parsing raises."""
    # Test with a valid docstring that does not raise any exceptions
    docstring = parse(
        """
        Short description
        """
    )
    assert len(docstring.raises) == 0

    # Test with a valid docstring that raises an exception
    docstring = parse(
        """
        Short description
        Raises
        ------
        ValueError
            Description of the error
        """
    )
    assert len(docstring.raises) == 1
    assert docstring.raises[0].type_name == "ValueError"
    assert docstring.raises[0].description == "Description of the error"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_numpydoc_test_raises_2_test_invalid_input_error_handling
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_raises_2_test_invalid_input_error_handling.py:3:0: E0611: No name 'parse' in module 'docstring_parser' (no-name-in-module)


"""