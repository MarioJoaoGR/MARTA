
import pytest
from docstring_parser.tests.test_numpydoc import parse

def test_params() -> None:
    """Test parsing parameters from a docstring."""
    
    # Test case with no parameters
    docstring = parse("Short description")
    assert len(docstring.params) == 0

    # Test case with multiple parameters
    docstring = parse(
        """
        Short description

        Parameters
        ----------
        name
            description 1
        priority : int
            description 2
        sender : str, optional
            description 3
        ratio : Optional[float], optional
            description 4
        """
    )
    assert len(docstring.params) == 4
    assert docstring.params[0].arg_name == "name"
    assert docstring.params[0].type_name is None
    assert docstring.params[1].arg_name == "priority"
    assert docstring.params[1].type_name == "int"
    assert not docstring.params[1].is_optional
    assert docstring.params[2].arg_name == "sender"
    assert docstring.params[2].type_name == "str"
    assert docstring.params[2].is_optional
    assert docstring.params[3].arg_name == "ratio"
    assert docstring.params[3].type_name == "Optional[float]"
    assert docstring.params[3].is_optional

    # Test case with multi-line description for a parameter
    docstring = parse(
        """
        Short description

        Parameters
        ----------
        name
            description 1
            with multi-line text
        priority : int
            description 2
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
    assert not docstring.params[1].is_optional
