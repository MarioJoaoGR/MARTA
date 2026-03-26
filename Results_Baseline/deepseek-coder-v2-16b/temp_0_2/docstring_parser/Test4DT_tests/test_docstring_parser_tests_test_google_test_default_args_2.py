
# Module: docstring_parser.tests.test_google
from docstring_parser.tests.test_google import parse

def test_default_args():
    """Test parsing default arguments."""
    docstring = parse(
        """A sample function

A function the demonstrates docstrings

Args:
    arg1 (int): The firsty arg
    arg2 (str): The second arg
    arg3 (float, optional): The third arg. Defaults to 1.0.
    arg4 (Optional[Dict[str, Any]], optional): The last arg. Defaults to None.
    arg5 (str, optional): The fifth arg. Defaults to DEFAULT_ARG5.

Returns:
    Mapping[str, Any]: The args packed in a mapping
"""
    )
    
    assert docstring is not None
    assert len(docstring.params) == 5

    # Test each parameter's attributes
    arg1 = docstring.params[0]
    assert arg1.arg_name == "arg1"
    assert not arg1.is_optional
    assert arg1.type_name == "int"
    assert arg1.default is None
    assert arg1.description == "The firsty arg"

    arg2 = docstring.params[1]
    assert arg2.arg_name == "arg2"
    assert not arg2.is_optional
    assert arg2.type_name == "str"
    assert arg2.default is None
    assert arg2.description == "The second arg"

    arg3 = docstring.params[2]
    assert arg3.arg_name == "arg3"
    assert arg3.is_optional
    assert arg3.type_name == "float"
    assert arg3.default == "1.0"
    assert arg3.description == "The third arg. Defaults to 1.0."

    arg4 = docstring.params[3]
    assert arg4.arg_name == "arg4"
    assert arg4.is_optional
    assert arg4.type_name == "Optional[Dict[str, Any]]"
    assert arg4.default == "None"
    assert arg4.description == "The last arg. Defaults to None."

    arg5 = docstring.params[4]
    assert arg5.arg_name == "arg5"
    assert arg5.is_optional
    assert arg5.type_name == "str"
    assert arg5.default == "DEFAULT_ARG5"
    assert arg5.description == "The fifth arg. Defaults to DEFAULT_ARG5."
