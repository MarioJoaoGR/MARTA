
import pytest
from docstring_parser.tests.test_google import parse

def test_attributes() -> None:
    """Test parsing attributes from a Google-style docstring.

    This function tests the ability to parse attribute details, including their names, types, descriptions, and optional flags, from a Google-style docstring. It uses the `parse` function to parse various examples of docstrings with different structures and verifies that the parsed parameters match the expected attributes.

    Parameters:
        None

    Returns:
        None

    Examples:
        ```python
        def test_attributes():
            # Call the function to run the tests
            test_attributes()
        ```

    The `test_attributes` function is designed to validate the parsing of attributes from a docstring, ensuring that both single-line and multi-line attribute descriptions are correctly interpreted. It plays a crucial role in the testing suite for any project aiming to parse and interpret Google-style docstrings, providing robust validation of the parser's functionality through predefined examples.
    """
    # Test handling of missing attributes in the docstring
    docstring = parse("Short description")
    assert len(docstring.params) == 0

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
    assert docstring.params[1].arg_name == "priority"
    assert docstring.params[1].type_name == "int"
    assert docstring.params[1].description == "description 2"
