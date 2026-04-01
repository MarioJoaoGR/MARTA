
import pytest
from docstring_parser.tests.test_google import parse

def test_attributes() -> None:
    """Test parsing attributes of a docstring.

    This function tests the ability to parse and verify the attributes (parameters) in a Google-style docstring. It checks for both single-line and multi-line descriptions, as well as optional parameters. The function uses the `parse` function to parse different docstrings and then asserts that the parsed parameters match expected results.

    Examples:
        >>> from google_parser import test_attributes
        >>> test_attributes()  # This will run the tests for parsing attributes in various docstrings

    Notes:
        - The `parse` function is used to parse Google-style docstrings, which are expected to include sections like "Attributes" with detailed descriptions of each parameter.
        - The function checks that the number and details (name, type, description, and optional status) of parameters in the parsed docstring match the expected results.
        - This test is crucial for ensuring that the parsing logic correctly handles various formats of docstrings, including those with multi-line descriptions and optional parameters.
    """
    # Test case for empty docstring
    docstring = parse("Short description")
    assert len(docstring.params) == 0

    # Test case for multiple attributes
    docstring = parse(
        """
        Short description

        Attributes:
            name: description 1
            priority (int): description 2
            sender (str?): description 3
            ratio (Optional[float], optional): description 4
        """
    )
    assert len(docstring.params) == 4
    assert docstring.params[0].arg_name == "name"
    assert docstring.params[0].type_name is None
    assert docstring.params[0].description == "description 1"
    assert not docstring.params[0].is_optional
    assert docstring.params[1].arg_name == "priority"
    assert docstring.params[1].type_name == "int"
    assert docstring.params[1].description == "description 2"
    assert not docstring.params[1].is_optional
    assert docstring.params[2].arg_name == "sender"
    assert docstring.params[2].type_name == "str"
    assert docstring.params[2].description == "description 3"
    assert docstring.params[2].is_optional
    assert docstring.params[3].arg_name == "ratio"
    assert docstring.params[3].type_name == "Optional[float]"
    assert docstring.params[3].description == "description 4"
    assert docstring.params[3].is_optional

    # Test case for multi-line description in a single attribute
    docstring = parse(
        """
        Short description

        Attributes:
            name: description 1
                with multi-line text
            priority (int): description 2
        """
    )
    assert len(docstring.params) == 2
    assert docstring.params[0].arg_name == "name"
    assert docstring.params[0].type_name is None
    assert docstring.params[0].description == (
        "description 1\nwith multi-line text"
    )
    assert not docstring.params[0].is_optional
    assert docstring.params[1].arg_name == "priority"
    assert docstring.params[1].type_name == "int"
    assert docstring.params[1].description == "description 2"
    assert not docstring.params[1].is_optional
