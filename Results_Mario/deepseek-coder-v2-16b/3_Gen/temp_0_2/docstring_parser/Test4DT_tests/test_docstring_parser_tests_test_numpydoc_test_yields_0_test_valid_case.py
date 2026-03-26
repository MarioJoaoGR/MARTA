
import pytest
from docstring_parser.tests.test_numpydoc import parse

def test_valid_case() -> None:
    """Test parsing yields."""
    docstring = parse(
        """
        Short description
        Yields
        ------
        int
            description
        """
    )
    assert len(docstring.meta) == 1
    assert docstring.meta[0].args == ["yields"]
    assert docstring.meta[0].type_name == "int"
    assert docstring.meta[0].description == "description"
    assert docstring.meta[0].return_name is None
    assert docstring.meta[0].is_generator
