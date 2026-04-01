
import pytest
from docstring_parser.tests.test_numpydoc import parse

def test_warns() -> None:
    """Test parsing warns.

    This function is designed to parse a numpy-style docstring and check for warnings within it. It constructs a sample docstring with a UserWarning and parses it using the `parse` function. The parsed result is then validated to ensure that it contains exactly one warning of type "UserWarning" with the specified description.

    Parameters:
        None

    Returns:
        None

    Examples:
        To run this test, simply call the function `test_warns()`. It will automatically parse a sample docstring and assert that it contains one warning of type "UserWarning" with the description "description". If the assertions pass, the function completes successfully without raising any errors.

    Intended Usage:
        The function is designed for internal testing of the docstring parsing functionality, ensuring that warnings are correctly extracted from a given docstring format. It does not accept parameters but expects a specific structure in the provided docstring to perform its assertions.
    """
    docstring = parse(
        """
        Short description
        Warns
        -----
        UserWarning
            description
        """
    )
    assert len(docstring.meta) == 1
    assert docstring.meta[0].type_name == "UserWarning"
    assert docstring.meta[0].description == "description"
