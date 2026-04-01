
from docstring_parser import parse
import pytest

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
    # Test 1: No returns section
    docstring = parse(
        """
        Short description
        """
    )
    assert docstring.returns is None
    assert docstring.many_returns is not None
    assert len(docstring.many_returns) == 0

    # Test 2: Single return type with no description
    docstring = parse(
        """
        Short description
        Returns
        -------
        int
        """
    )
    assert docstring.returns is not None
    assert docstring.returns.type_name == "int"
    assert docstring.returns.description is None
    assert docstring.many_returns is not None
    assert len(docstring.many_returns) == 1
    assert docstring.many_returns[0] == docstring.returns

    # Test 3: Single return type with description
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

    # Test 4: Multiple return types in one block with descriptions
    docstring = parse(
        """
        Returns
        -------
        int : description for a
        str : description for b
        """
    )
    assert docstring.returns is not None
    assert docstring.returns.type_name == "int"
    assert docstring.returns.description == "description for a"
    assert docstring.many_returns is not None
    assert len(docstring.many_returns) == 2
    assert docstring.many_returns[0].type_name == "int"
    assert docstring.many_returns[0].description == "description for a"
    assert docstring.many_returns[1].type_name == "str"
    assert docstring.many_returns[1].description == "description for b"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_numpydoc_test_returns_7_test_valid_inputs
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_returns_7_test_valid_inputs.py:2:0: E0611: No name 'parse' in module 'docstring_parser' (no-name-in-module)


"""