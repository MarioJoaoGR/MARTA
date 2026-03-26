
# Module: docstring_parser.tests.test_rest
from docstring_parser import parse

def test_returns():
    """Test parsing returns from various styles of docstrings."""
    
    # Test case 6: No return specified in the docstring (line 334)
    docstring = parse(
        """
        Short description
        """
    )
    assert docstring.returns is None
    assert docstring.many_returns is not None
    assert len(docstring.many_returns) == 0
    
    # Test case 7: Single return specified without type name (line 349)
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
    
    # Test case 8: Single return specified with type name but no description (line 350)
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
    
    # Test case 9: Single return specified with type name and description (line 364)
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
    
    # Test case 10: Single return specified with type name, description, and no generator (line 377)
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
    
    # Test case 11: Multiple returns specified (line 340)
    docstring = parse(
        """
        Short description
        :returns: description1
        :returns: description2
        """
    )
    assert len(docstring.many_returns) == 2
    assert docstring.many_returns[0].type_name is None
    assert docstring.many_returns[0].description == "description1"
    assert not docstring.many_returns[0].is_generator
    assert docstring.many_returns[1].type_name is None
    assert docstring.many_returns[1].description == "description2"
    assert not docstring.many_returns[1].is_generator
    
    # Test case 12: Multiple returns with type names and descriptions (line 364)
    docstring = parse(
        """
        Short description
        :returns int: description1
        :returns str: description2
        """
    )
    assert len(docstring.many_returns) == 2
    assert docstring.many_returns[0].type_name == "int"
    assert docstring.many_returns[0].description == "description1"
    assert not docstring.many_returns[0].is_generator
    assert docstring.many_returns[1].type_name == "str"
    assert docstring.many_returns[1].description == "description2"
    assert not docstring.many_returns[1].is_generator
    
    # Test case 13: Multiple returns with type names, descriptions, and no generators (line 377)
    docstring = parse(
        """
        Short description
        :returns: description1
        :rtype: int
        :returns: description2
        :rtype: str
        """
    )
    assert len(docstring.many_returns) == 2