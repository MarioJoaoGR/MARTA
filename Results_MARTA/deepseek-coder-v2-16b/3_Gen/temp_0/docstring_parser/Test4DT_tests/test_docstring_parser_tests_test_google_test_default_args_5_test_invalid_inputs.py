
from docstring_parser.tests.test_google import parse
import pytest
from typing import Any, Dict, Optional, Mapping

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

    arg4 = docstring.params[3]
    assert arg4.arg_name == "arg4"
    assert arg4.is_optional
    assert arg4.type_name == "Optional[Dict[str, Any]]"
    assert arg4.default == "None"
    assert arg4.description == "The last arg. Defaults to None."
