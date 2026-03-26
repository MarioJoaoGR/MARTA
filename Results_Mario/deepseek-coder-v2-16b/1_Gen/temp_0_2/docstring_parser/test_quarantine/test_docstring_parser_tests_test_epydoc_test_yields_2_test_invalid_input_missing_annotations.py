
import pytest
from docstring_parser import parse

def test_yields():
    """Test parsing yields."""
    
    # Test case for missing yield annotation
    docstring = parse("Short description")
    assert docstring.returns is None

    # Test case for presence of only yield description
    docstring = parse(
        """
        Short description
        @yield: description
        """
    )
    assert docstring.returns is not None
    assert docstring.returns.type_name is None
    assert docstring.returns.description == "description"
    assert docstring.returns.is_generator

    # Test case for presence of yield description and type
    docstring = parse(
        """
        Short description
        @yield: description
        @ytype: int
        """
    )
    assert docstring.returns is not None
    assert docstring.returns.type_name == "int"
    assert docstring.returns.description == "description"
    assert docstring.returns.is_generator

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_epydoc_test_yields_2_test_invalid_input_missing_annotations
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_yields_2_test_invalid_input_missing_annotations.py:3:0: E0611: No name 'parse' in module 'docstring_parser' (no-name-in-module)


"""