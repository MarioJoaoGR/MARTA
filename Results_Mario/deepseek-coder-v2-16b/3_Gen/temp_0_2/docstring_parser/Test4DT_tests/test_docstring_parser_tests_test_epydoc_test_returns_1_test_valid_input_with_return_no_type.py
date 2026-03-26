
from docstring_parser.tests.test_epydoc import parse

def test_returns() -> None:
    """Test parsing returns from epydoc-style docstrings."""
    # Test when there is no return specified in the docstring
    docstring = parse("Short description")
    assert docstring.returns is None

    # Test when a return is specified without a type
    docstring = parse("Short description\n@return: description")
    assert docstring.returns is not None
    assert docstring.returns.type_name is None
    assert docstring.returns.description == "description"
    assert not docstring.returns.is_generator

    # Test when a return is specified with an explicit type
    docstring = parse("Short description\n@return: description\n@rtype: int")
    assert docstring.returns is not None
    assert docstring.returns.type_name == "int"
    assert docstring.returns.description == "description"
    assert not docstring.returns.is_generator
