
# Module: docstring_parser.tests.test_rest
# test_rest.py
from docstring_parser.tests.test_rest import parse, test_yields
import pytest

def test_yields():
    # Test when there is no yield declaration in the docstring
    docstring = parse(
        """
        Short description
        """
    )
    assert docstring.returns is None
    assert len(docstring.many_returns) == 0, "Expected no returns but found some"

    # Test when there is a yield declaration with only a description
    docstring = parse(
        """
        Short description
        :yields: description
        """
    )
    assert docstring.returns is not None
    assert docstring.returns.type_name is None, "Expected type name to be None"
    assert docstring.returns.description == "description", f"Expected description 'description' but got {docstring.returns.description}"
    assert docstring.returns.is_generator, "Expected the return value to be a generator"
    assert len(docstring.many_returns) == 1, "Expected one return but found more"
    assert docstring.many_returns[0] == docstring.returns, "The first many_return does not match the single return"

    # Test when there is a yield declaration with an specific type and description
    docstring = parse(
        """
        Short description
        :yields int: description
        """
    )
    assert docstring.returns is not None
    assert docstring.returns.type_name == "int", f"Expected type name 'int' but got {docstring.returns.type_name}"
    assert docstring.returns.description == "description", f"Expected description 'description' but got {docstring.returns.description}"
    assert docstring.returns.is_generator, "Expected the return value to be a generator"
    assert len(docstring.many_returns) == 1, "Expected one return but found more"
    assert docstring.many_returns[0] == docstring.returns, "The first many_return does not match the single return"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_rest_test_yields_0
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_yields_0.py:7:0: E0102: function already defined line 4 (function-redefined)

"""