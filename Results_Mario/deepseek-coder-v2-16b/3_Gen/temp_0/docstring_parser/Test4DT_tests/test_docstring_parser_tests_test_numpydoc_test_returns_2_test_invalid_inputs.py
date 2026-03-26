
from docstring_parser.tests.test_numpydoc import parse

def test_invalid_inputs():
    """Test parsing returns of a numpy-style docstring with invalid inputs."""
    
    # Test case 1: No returns specified
    docstring = parse("Short description")
    assert docstring.returns is None
    assert docstring.many_returns == []

    # Test case 2: Single return type without description
    parsed_docstring = parse("""
    Short description
    Returns
    -------
    int
    """)
    assert parsed_docstring.returns is not None
    assert parsed_docstring.returns.type_name == "int"
    assert parsed_docstring.returns.description is None
    assert len(parsed_docstring.many_returns) == 1
    assert parsed_docstring.many_returns[0] == parsed_docstring.returns

    # Test case 3: Single return type with a description
    parsed_docstring = parse("""
    Short description
    Returns
    -------
    int
        description
    """)
    assert parsed_docstring.returns is not None
    assert parsed_docstring.returns.type_name == "int"
    assert parsed_docstring.returns.description == "description"
    assert len(parsed_docstring.many_returns) == 1
    assert parsed_docstring.many_returns[0] == parsed_docstring.returns

    # Test case 4: Multiple return types with individual descriptions
    parsed_docstring = parse("""
    Short description
    Returns
    -------
    int
        description for a
    str
        description for b
    """)
    assert len(parsed_docstring.many_returns) == 2
    assert parsed_docstring.many_returns[0].type_name == "int"
    assert parsed_docstring.many_returns[0].description == "description for a"
    assert parsed_docstring.many_returns[1].type_name == "str"
    assert parsed_docstring.many_returns[1].description == "description for b"

    # Test case 5: Custom return type with detailed description including colon
    parsed_docstring = parse("""
    Short description
    Returns
    -------
    Optional[Mapping[str, List[int]]]
        A description: with a colon
    """)
    assert parsed_docstring.returns is not None
    assert parsed_docstring.returns.type_name == "Optional[Mapping[str, List[int]]]"
    assert parsed_docstring.returns.description == "A description: with a colon"
    assert len(parsed_docstring.many_returns) == 1
    assert parsed_docstring.many_returns[0] == parsed_docstring.returns

    # Test case 6: Multiple return types including nested structures
    parsed_docstring = parse("""
    Short description
    Returns
    -------
    int
        description for a
    str
        description for b
    """)
    assert len(parsed_docstring.many_returns) == 2
    assert parsed_docstring.many_returns[0].type_name == "int"
    assert parsed_docstring.many_returns[0].description == "description for a"
    assert parsed_docstring.many_returns[1].type_name == "str"
    assert parsed_docstring.many_returns[1].description == "description for b"
