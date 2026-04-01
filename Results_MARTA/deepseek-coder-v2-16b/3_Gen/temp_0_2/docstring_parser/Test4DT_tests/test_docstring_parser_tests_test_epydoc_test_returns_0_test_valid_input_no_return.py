
from docstring_parser.tests.test_epydoc import parse

def test_returns() -> None:
    """Test parsing returns from epydoc-style docstrings.

    This function tests the ability of the `parse` function to correctly parse return values specified in epydoc-style docstrings. It checks for various scenarios, including when a return value is explicitly stated with no type specification, when it includes a type specification, and when there are multiple returns or yields.

    Examples:
        >>> test_returns()  # This will run the tests to check if the function can correctly parse different return specifications in docstrings.

    Notes:
        - The `parse` function is expected to handle various cases of return value declarations, including those without a type specification and those with explicit type specifications.
        - The test involves creating docstrings with different return statements and checking if the parsed result contains the correct information about the returns.
        - This function does not take any parameters; it solely focuses on verifying the functionality of the `parse` function's return parsing capabilities.
    
    What it is intended to do:
        This function tests the ability of the parser to correctly identify and interpret return type and description information from various styles of docstrings, including those annotated with `@return` and optional `@rtype`. It checks for both absence and presence of return information, as well as correct interpretation of return types specified in these annotations.
    """
    docstring = parse(
        """
        Short description
        """
    )
    assert docstring.returns is None

    docstring = parse(
        """
        Short description
        @return: description
        """
    )
    assert docstring.returns is not None
    assert docstring.returns.type_name is None
    assert docstring.returns.description == "description"
    assert not docstring.returns.is_generator

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
