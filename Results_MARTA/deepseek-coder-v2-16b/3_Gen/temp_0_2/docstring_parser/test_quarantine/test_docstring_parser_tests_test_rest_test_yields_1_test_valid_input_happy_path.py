
import pytest
from docstring_parser import parse

def test_yields() -> None:
    """Test parsing yields."""
    # Test case 1: No yield statements
    docstring = parse(
        """
        Short description
        """
    )
    assert docstring.returns is None
    assert docstring.many_returns is not None
    assert len(docstring.many_returns) == 0

    # Test case 2: Single yield statement without type
    docstring = parse(
        """
        Short description
        :yields: description
        """
    )
    assert docstring.returns is not None
    assert docstring.returns.type_name is None
    assert docstring.returns.description == "description"
    assert docstring.returns.is_generator
    assert docstring.many_returns is not None
    assert len(docstring.many_returns) == 1
    assert docstring.many_returns[0] == docstring.returns

    # Test case 3: Single yield statement with type
    docstring = parse(
        """
        Short description
        :yields int: description
        """
    )
    assert docstring.returns is not None
    assert docstring.returns.type_name == "int"
    assert docstring.returns.description == "description"
    assert docstring.returns.is_generator
    assert docstring.many_returns is not None
    assert len(docstring.many_returns) == 1
    assert docstring.many_returns[0] == docstring.returns

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_rest_test_yields_1_test_valid_input_happy_path
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_yields_1_test_valid_input_happy_path.py:3:0: E0611: No name 'parse' in module 'docstring_parser' (no-name-in-module)


"""