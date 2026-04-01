
import pytest
from docstring_parser.tests.test_numpydoc import parse

def test_returns() -> None:
    """Test parsing returns from a numpy-style docstring.

    This function tests the ability of the `parse` function to correctly parse and interpret the "Returns" section of a numpy-style docstring. It checks various scenarios including no return, single return type with or without description, multiple return types listed in one block, and detailed descriptions for each return type. The function uses assertions to verify that the parsed results match expected outcomes based on the input docstrings.

    Parameters:
        None.

    Returns:
        None.

    Examples:
        >>> test_returns()  # Automatically run tests and assert expected outcomes
    
    Intended Purpose:
    --------------------------------------------------------------------------------
    Test parsing returns from various docstrings to ensure the parser handles different formats correctly.

    This function does not take any parameters and does not return a value itself, but it includes multiple test cases that check how the `parse` function processes different styles of docstrings related to 'returns'. It verifies that the parsed results match expected outcomes for each case.
    --------------------------------------------------------------------------------
"""
    # Test when there is no return type specified
    docstring = parse(
        """
        Short description
        """
    )
    assert docstring.returns is None
    assert docstring.many_returns is not None
    assert len(docstring.many_returns) == 0

    # Test when there is a single return type with no description
    docstring = parse(
        """
        Short description
        Returns
        -------
        type
        """
    )
    assert docstring.returns is not None
    assert docstring.returns.type_name == "type"
    assert docstring.returns.description is None
    assert docstring.many_returns is not None
    assert len(docstring.many_returns) == 1
    assert docstring.many_returns[0] == docstring.returns

    # Test when there is a single return type with a description
    docstring = parse(
        """
        Short description
        Returns
        -------
        int
            description
        """
    )
    assert docstring.returns is not None
    assert docstring.returns.type_name == "int"
    assert docstring.returns.description == "description"
    assert docstring.many_returns is not None
    assert len(docstring.many_returns) == 1
    assert docstring.many_returns[0] == docstring.returns

    # Test when there are multiple return types listed in one block with descriptions
    docstring = parse(
        """
        Returns
        -------
        Optional[Mapping[str, List[int]]]
            A description: with a colon
        """
    )
    assert docstring.returns is not None
    assert docstring.returns.type_name == "Optional[Mapping[str, List[int]]]"
    assert docstring.returns.description == "A description: with a colon"
    assert docstring.many_returns is not None
    assert len(docstring.many_returns) == 1
    assert docstring.many_returns[0] == docstring.returns

    # Test when there are multiple return types listed in one block with detailed descriptions
    docstring = parse(
        """
        Short description
        Returns
        -------
        int
            description
            with much text

            even some spacing
        """
    )
    assert docstring.returns is not None
    assert docstring.returns.type_name == "int"
    assert docstring.returns.description == (
        "description\nwith much text\n\neven some spacing"
    )
    assert docstring.many_returns is not None
    assert len(docstring.many_returns) == 1
    assert docstring.many_returns[0] == docstring.returns

    # Test when there are multiple return types listed in one block with detailed descriptions and names
    docstring = parse(
        """
        Short description
        Returns
        -------
        a : int
            description for a
        b : str
            description for b
        """
    )
    assert docstring.returns is not None
    assert docstring.returns.type_name == "int"
    assert docstring.returns.description == ("description for a")
    assert docstring.many_returns is not None
    assert len(docstring.many_returns) == 2
    assert docstring.many_returns[0].type_name == "int"
    assert docstring.many_returns[0].description == "description for a"
    assert docstring.many_returns[0].return_name == "a"
    assert docstring.many_returns[1].type_name == "str"
    assert docstring.many_returns[1].description == "description for b"
    assert docstring.many_returns[1].return_name == "b"
