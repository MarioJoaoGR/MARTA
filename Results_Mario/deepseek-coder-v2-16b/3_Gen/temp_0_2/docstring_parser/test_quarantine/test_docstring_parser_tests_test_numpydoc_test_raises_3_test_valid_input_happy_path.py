
import pytest
from docstring_parser import parse

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
************* Module Test4DT_tests.test_docstring_parser_tests_test_numpydoc_test_raises_3_test_valid_input_happy_path
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_raises_3_test_valid_input_happy_path.py:3:0: E0611: No name 'parse' in module 'docstring_parser' (no-name-in-module)


"""