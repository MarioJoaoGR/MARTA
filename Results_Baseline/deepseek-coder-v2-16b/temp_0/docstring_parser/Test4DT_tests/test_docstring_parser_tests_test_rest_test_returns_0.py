# Module: docstring_parser.tests.test_rest
# test_rest.py
from docstring_parser import parse

def test_returns():
    """Test parsing returns from various styles of docstrings."""
    
    # Test case 1: No return specified in the docstring
    docstring = parse(
        """
        Short description
        """
    )
    assert docstring.returns is None
    assert docstring.many_returns is not None
    assert len(docstring.many_returns) == 0
    
    # Test case 2: Single return specified without type name
    docstring = parse(
        """
        Short description
        :returns: description
        """
    )
    assert docstring.returns is not None
    assert docstring.returns.type_name is None
    assert docstring.returns.description == "description"
    assert not docstring.returns.is_generator
    assert docstring.many_returns == [docstring.returns]
    
    # Test case 3: Single return specified with type name but no description
    docstring = parse(
        """
        Short description
        :returns int: 
        """
    )
    assert docstring.returns is not None
    assert docstring.returns.type_name == "int"
    assert docstring.returns.description == ""
    assert not docstring.returns.is_generator
    assert docstring.many_returns == [docstring.returns]
    
    # Test case 4: Single return specified with type name and description
    docstring = parse(
        """
        Short description
        :returns int: description
        """
    )
    assert docstring.returns is not None
    assert docstring.returns.type_name == "int"
    assert docstring.returns.description == "description"
    assert not docstring.returns.is_generator
    assert docstring.many_returns == [docstring.returns]
    
    # Test case 5: Single return specified with type name, description, and no generator
    docstring = parse(
        """
        Short description
        :returns: description
        :rtype: int
        """
    )
    assert docstring.returns is not None
    assert docstring.returns.type_name == "int"
    assert docstring.returns.description == "description"
    assert not docstring.returns.is_generator
    assert docstring.many_returns == [docstring.returns]
