# Module: docstring_parser.tests.test_epydoc
# test_epydoc.py
from docstring_parser import parse

def test_returns() -> None:
    """Test parsing returns from an epydoc-style docstring."""
    
    # Test case 1: No return type specified
    docstring = parse(
        """
        Short description
        """
    )
    assert docstring.returns is None

    # Test case 2: Return type specified without a description
    docstring = parse(
        """
        Short description
        @return: 
        """
    )
    assert docstring.returns is not None
    assert docstring.returns.type_name is None
    assert docstring.returns.description == ""
    assert not docstring.returns.is_generator

    # Test case 3: Return type specified with both a description and a type
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
