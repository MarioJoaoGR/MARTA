
import pytest
from docstring_parser.tests.test_numpydoc import parse

def test_warns() -> None:
    """Test parsing warns."""
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
