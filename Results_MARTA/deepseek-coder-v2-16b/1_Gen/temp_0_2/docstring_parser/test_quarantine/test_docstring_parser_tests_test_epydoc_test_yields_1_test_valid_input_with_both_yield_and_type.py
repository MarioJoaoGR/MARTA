
import pytest
from docstring_parser import parse

def test_yields() -> None:
    """Test parsing yields."""
    docstring = parse(
        """
        Short description
        """
    )
    assert docstring.returns is None

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
************* Module Test4DT_tests.test_docstring_parser_tests_test_epydoc_test_yields_1_test_valid_input_with_both_yield_and_type
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_yields_1_test_valid_input_with_both_yield_and_type.py:3:0: E0611: No name 'parse' in module 'docstring_parser' (no-name-in-module)


"""