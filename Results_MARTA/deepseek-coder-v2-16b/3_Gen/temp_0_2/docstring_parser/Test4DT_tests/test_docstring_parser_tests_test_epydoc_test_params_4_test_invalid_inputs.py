
from docstring_parser.tests.test_epydoc import parse

def test_params() -> None:
    """Test parsing params.

    This function tests the ability to parse parameters from an epydoc-style docstring. It constructs two different docstrings, one without any parameters and another with multiple parameters including their descriptions, types, default values, and whether they are optional or not. The function then asserts that the parsed parameters match the expected results based on the provided docstrings.

    Parameters:
        None.

    Returns:
        None.

    Examples:
        >>> test_params()  # This will run the function to check if it can parse the parameters correctly from a docstring.

    Notes:
        - The function constructs two different docstrings, one without any parameters and another with multiple parameters including their descriptions, types, default values, and whether they are optional or not.
        - It then asserts that the parsed parameters match the expected results based on the provided docstrings.
        - This test helps ensure that the parsing logic for epydoc-style docstrings is working correctly and can handle various configurations of parameter information.
    """
    # Test case with no parameters
    docstring = parse("Short description")
    assert len(docstring.params) == 0

    # Test case with multiple parameters
    docstring = parse(
        """
        Short description

        @param name: description 1
        @param priority: description 2
        @type priority: int
        @param sender: description 3
        @type sender: str?
        @param message: description 4, defaults to 'hello'
        @type message: str?
        @param multiline: long description 5,
        defaults to 'bye'
        @type multiline: str?
        """
    )
    assert len(docstring.params) == 5
    assert docstring.params[0].arg_name == "name"
    assert docstring.params[0].type_name is None
    assert docstring.params[0].description == "description 1"
    assert docstring.params[0].default is None
    assert not docstring.params[0].is_optional
    assert docstring.params[1].arg_name == "priority"
    assert docstring.params[1].type_name == "int"
    assert docstring.params[1].description == "description 2"
    assert not docstring.params[1].is_optional
    assert docstring.params[1].default is None
    assert docstring.params[2].arg_name == "sender"
    assert docstring.params[2].type_name == "str"
    assert docstring.params[2].description == "description 3"
    assert docstring.params[2].is_optional
    assert docstring.params[2].default is None
    assert docstring.params[3].arg_name == "message"
    assert docstring.params[3].type_name == "str"
    assert (
        docstring.params[3].description == "description 4, defaults to 'hello'"
    )
    assert docstring.params[3].is_optional
    assert docstring.params[3].default == "'hello'"
    assert docstring.params[4].arg_name == "multiline"
    assert docstring.params[4].type_name == "str"
    assert (
        docstring.params[4].description
        == "long description 5,\ndefaults to 'bye'"
    )
    assert docstring.params[4].is_optional
    assert docstring.params[4].default == "'bye'"
