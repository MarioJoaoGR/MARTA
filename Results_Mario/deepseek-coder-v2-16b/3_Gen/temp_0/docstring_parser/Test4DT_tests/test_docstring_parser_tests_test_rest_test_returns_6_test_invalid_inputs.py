
from docstring_parser.tests.test_rest import parse

def test_returns() -> None:
    """Test parsing returns from various styles of docstrings.

    This function tests the ability to parse return descriptions and types from different styles of docstrings, including those using ReST, Google-style, Numpydoc-style, and Epydoc notations. It checks for both single and multiple return values, as well as correct parsing of type names and descriptions.

    Parameters:
        None

    Returns:
        None

    Usage:
        The function does not take any parameters but tests the parsing capabilities by applying it to various docstring formats. It asserts that the parsed returns match expected outcomes based on the content of the docstrings provided.
    
    This function is designed to ensure that return values specified in different styles of docstrings are correctly parsed, regardless of whether the type name and description are present or not. It helps maintain consistency and correctness in how return values are documented and parsed across various documentation formats used in Python projects.
    """
    # Test for invalid inputs
    docstring = parse(
        """
        Short description
        """
    )
    assert docstring.returns is None
    assert docstring.many_returns is not None
    assert len(docstring.many_returns) == 0

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
