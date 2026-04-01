
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
