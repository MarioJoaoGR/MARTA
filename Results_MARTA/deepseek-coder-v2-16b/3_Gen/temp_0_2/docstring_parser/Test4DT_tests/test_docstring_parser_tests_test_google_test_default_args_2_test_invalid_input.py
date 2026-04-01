
import pytest
from docstring_parser.tests.test_google import parse

def test_default_args() -> None:
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

    arg3 = docstring.params[2]
    assert arg3.arg_name == "arg3"
    assert arg3.is_optional
    assert arg3.type_name == "float"
    assert arg3.default == "1.0"
    assert arg3.description == "The third arg. Defaults to 1.0."

    arg5 = docstring.params[4]
    assert arg5.arg_name == "arg5"
    assert arg5.is_optional
    assert arg5.type_name == "str"
    assert arg5.default == "DEFAULT_ARG5"
    assert arg5.description == "The fifth arg. Defaults to DEFAULT_ARG5."
