
from docstring_parser.tests.test_rest import parse

def test_returns() -> None:
    """Test parsing returns from ReST-style docstrings.

    This function tests the behavior of the `parse` function when dealing with different return type annotations in ReST-style docstrings. It checks how the function handles various cases, including no return annotation, explicit return type annotation without description, and explicit return type annotation with a description. The test involves parsing several examples of ReST-style docstrings and asserting that the parsed results match expected outcomes based on the presence and content of the `:returns:` directive.

    Examples:
        >>> test_returns()
        
    This example demonstrates running the `test_returns` function, which will automatically parse the provided examples and assert the expected outcomes for each case. The exact output may vary depending on the implementation details of the `parse` function and how it interprets the ReST-style docstrings.

    Parameters:
        None

    Returns:
        None

    Usage:
        The function is designed to be run directly without specific parameters. It will parse the provided docstrings and assert expected outcomes based on the content of the docstrings. This helps in verifying that the parsing logic correctly handles different formats and extracts relevant information about return types and descriptions.
    """
    # Test case for no return annotation
    docstring = parse(
        """
        Short description
        """
    )
    assert docstring.returns is None
    assert docstring.many_returns is not None
    assert len(docstring.many_returns) == 0

    # Test case for return annotation with no description
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

    # Test case for return annotation with type specified
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

    # Test case for return annotation with type and description specified
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
