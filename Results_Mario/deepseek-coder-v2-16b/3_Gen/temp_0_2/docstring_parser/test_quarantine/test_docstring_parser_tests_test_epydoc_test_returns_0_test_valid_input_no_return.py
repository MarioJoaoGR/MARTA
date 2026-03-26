
import pytest
from docstring_parser import parse

def test_returns() -> None:
    """Test parsing returns."""
    # Test case for no return statement in the docstring
    docstring = parse(
        """
        Short description
        """
    )
    assert docstring.returns is None

    # Test case for a return statement with no type specification
    docstring = parse(
        """
        Short description
        @return: description
        """
    )
    assert docstring.returns is not None
    assert docstring.returns.type_name is None
    assert docstring.returns.description == "description"
    assert not docstring.returns.is_generator

    # Test case for a return statement with type specification
    docstring = parse(
        """
        Short description
        @return: description
        @rtype: int
        """
    )
    assert docstring.returns is not None
    assert docstring.returns.type_name == "int"
    assert docstring.returns.description == "description"
    assert not docstring.returns.is_generator

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_epydoc_test_returns_0_test_valid_input_no_return
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_returns_0_test_valid_input_no_return.py:3:0: E0611: No name 'parse' in module 'docstring_parser' (no-name-in-module)


"""