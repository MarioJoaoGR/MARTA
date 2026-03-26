
# Module: docstring_parser.tests.test_rest
# Import the function from its module
from your_module import parse, DocstringReturns
import pytest

def test_parse_with_no_return():
    """Test parsing a ReST-style docstring without any return annotation."""
    docstring = parse(
        """
        Short description without return annotation.
        """
    )
    assert docstring.returns is None

def test_parse_with_single_return():
    """Test parsing a ReST-style docstring with a single return annotation."""
    docstring = parse(
        """
        Short description
        :returns: Description of the returned value.
        """
    )
    assert docstring.returns is not None
    assert docstring.returns.type_name is None
    assert docstring.returns.description == "Description of the returned value."
    assert not docstring.returns.is_generator

def test_parse_with_single_return_and_type():
    """Test parsing a ReST-style docstring with a return annotation and type."""
    docstring = parse(
        """
        Short description
        :returns int: Description of the returned value.
        """
    )
    assert docstring.returns is not None
    assert docstring.returns.type_name == "int"
    assert docstring.returns.description == "Description of the returned value."
    assert not docstring.returns.is_generator

def test_parse_with_multiple_returns():
    """Test parsing a ReST-style docstring with multiple return annotations."""
    docstring = parse(
        """
        Short description
        :returns: Description of the first returned value.
        :returns int: Description of the second returned value.
        """
    )
    assert len(docstring.many_returns) == 2
    assert docstring.many_returns[0].type_name is None
    assert docstring.many_returns[0].description == "Description of the first returned value."
    assert not docstring.many_returns[0].is_generator
    assert docstring.many_returns[1].type_name == "int"
    assert docstring.many_returns[1].description == "Description of the second returned value."
    assert not docstring.many_returns[1].is_generator

def test_parse_with_return_and_rtype():
    """Test parsing a ReST-style docstring with return and rtype annotations."""
    docstring = parse(
        """
        Short description
        :returns: Description of the returned value.
        :rtype: int
        """
    )
    assert docstring.returns is not None
    assert docstring.returns.type_name == "int"
    assert docstring.returns.description == "Description of the returned value."
    assert not docstring.returns.is_generator

def test_parse_with_invalid_return():
    """Test parsing a ReST-style docstring with an invalid return annotation."""
    docstring = parse(
        """
        Short description
        :returns: Description of the returned value.
        :rtype: str
        """
    )
    assert docstring.returns is not None
    assert docstring.returns.type_name == "int"  # Should default to int if rtype is invalid
    assert docstring.returns.description == "Description of the returned value."
    assert not docstring.returns.is_generator

if __name__ == "__main__":
    pytest.main()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_rest_test_returns_0
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_returns_0.py:4:0: E0401: Unable to import 'your_module' (import-error)

"""