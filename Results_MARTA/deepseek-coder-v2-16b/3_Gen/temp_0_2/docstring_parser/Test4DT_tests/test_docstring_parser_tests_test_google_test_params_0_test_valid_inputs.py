
import pytest
from docstring_parser.tests.test_google import parse

def test_params() -> None:
    """Test parsing parameters in a Google-style docstring.

    This function demonstrates how to parse multiple parameters within a Google-style docstring and verifies that they are correctly identified and parsed. It checks the presence of parameters, their types, whether they are optional, and their descriptions. The function includes examples showing different scenarios for parameter parsing.

    Examples:
        >>> from docstring_parser.tests.test_google import parse
        >>> test_params()  # This will run a series of assertions to check if the docstring parameters are parsed correctly.

    Notes:
        - The `parse` function is used internally to parse different Google-style docstrings, including those with varying numbers and types of parameters.
        - The examples provided in this function can be adapted or expanded based on additional test cases or specific requirements for parameter parsing.

    Args:
        None specified explicitly in this example; typically used with a docstring containing 'Args:' section for parsing parameters.

    Returns:
        A structured object (likely a custom class or dictionary) containing the parsed details of each parameter from the provided docstring. This includes the argument name, type annotation if present, and its description.

    Usage:
        The function is typically called with a Python module or function that contains a docstring annotated with 'Args:' for parsing parameters. Example usage involves integration with automated documentation tools or direct extraction of parameter details in applications requiring such information.
    """
    # Test empty docstring
    docstring = parse("Short description")
    assert len(docstring.params) == 0

    # Test multiple parameters
    docstring = parse(
        """
        Short description

        Args:
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

    # Test multi-line description in a parameter
    docstring = parse(
        """
        Short description

        Args:
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
