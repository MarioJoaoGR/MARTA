
import pytest
from google_parser import parse

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
    # Test case 1: No return statement
    docstring = parse(
        """
        Short description
        """
    )
    assert docstring.returns is None
    assert docstring.many_returns is not None
    assert len(docstring.many_returns) == 0

    # Test case 2: Single return type with description
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

    # Test case 3: Return type with colon in description
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

    # Test case 4: Explicit return type annotation
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

    # Test case 5: Return type with detailed multi-line description
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

    # Test case 6: Yield statement as return
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

    # Test case 7: Detailed return description with multiple lines and spacing
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

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_google_test_returns_7_test_valid_case_1
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_returns_7_test_valid_case_1.py:3:0: E0401: Unable to import 'google_parser' (import-error)


"""