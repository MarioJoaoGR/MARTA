
import pytest
from docstring_parser.tests.test_google import parse

def test_returns() -> None:
    """Test parsing returns of a Google-style docstring.

    This function tests the ability to parse different return types and descriptions in a Google-style docstring. It checks various scenarios including no return, single return type with description, multiple returns, return type with colon in description, explicit return type annotation, yield statement as return, and detailed return description with multiple lines and spacing.

    Examples:
        >>> from google_parser import parse
        >>> test_returns()  # This will run the function to check parsing capabilities of different docstring structures.

    Notes:
        - The function uses the `parse` function to parse various Google-style docstrings and asserts that the parsed returns match expected outcomes based on the content of the docstrings.
        - It is designed to ensure that the parser correctly handles different return formats, including those with colons in descriptions or detailed multi-line explanations.

    Parameters:
        None

    Returns:
        None

    Usage:
        This function is a part of the testing suite for the `docstring_parser` project and should not be called directly. It demonstrates expected behavior when parsing returns from various docstring formats.
    """
    # Test cases with no return
    docstring = parse(
        """
        Short description
        """
    )
    assert docstring.returns is None
    assert docstring.many_returns is not None
    assert len(docstring.many_returns) == 0

    # Test cases with single return type and description
    docstring = parse(
        """
        Short description
        Returns:
            description
        """
    )
    assert docstring.returns is not None
    assert docstring.returns.type_name is None
    assert docstring.returns.description == "description"
    assert docstring.many_returns is not None
    assert len(docstring.many_returns) == 1
    assert docstring.many_returns[0] == docstring.returns

    # Test cases with return type and description containing a colon
    docstring = parse(
        """
        Short description
        Returns:
            description with: a colon!
        """
    )
    assert docstring.returns is not None
    assert docstring.returns.type_name is None
    assert docstring.returns.description == "description with: a colon!"
    assert docstring.many_returns is not None
    assert len(docstring.many_returns) == 1
    assert docstring.many_returns[0] == docstring.returns

    # Test cases with explicit return type annotation
    docstring = parse(
        """
        Short description
        Returns:
            int: description
        """
    )
    assert docstring.returns is not None
    assert docstring.returns.type_name == "int"
    assert docstring.returns.description == "description"
    assert docstring.many_returns is not None
    assert len(docstring.many_returns) == 1
    assert docstring.many_returns[0] == docstring.returns

    # Test cases with detailed return description and multiple lines
    docstring = parse(
        """
        Returns:
            Optional[Mapping[str, List[int]]]: A description: with a colon
        """
    )
    assert docstring.returns is not None
    assert docstring.returns.type_name == "Optional[Mapping[str, List[int]]]"
    assert docstring.returns.description == "A description: with a colon"
    assert docstring.many_returns is not None
    assert len(docstring.many_returns) == 1
    assert docstring.many_returns[0] == docstring.returns

    # Test cases with yield statement as return
    docstring = parse(
        """
        Short description
        Yields:
            int: description
        """
    )
    assert docstring.returns is not None
    assert docstring.returns.type_name == "int"
    assert docstring.returns.description == "description"
    assert docstring.many_returns is not None
    assert len(docstring.many_returns) == 1
    assert docstring.many_returns[0] == docstring.returns

    # Test cases with detailed return description and multiple lines including spacing
    docstring = parse(
        """
        Short description
        Returns:
            int: description
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
