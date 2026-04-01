
import pytest
from docstring_parser.tests.test_google import parse

def test_unknown_meta() -> None:
    """Test parsing unknown meta."""
    docstring = parse(
        """Short desc

        Unknown 0:
            title0: content0

        Args:
            arg0: desc0
            arg1: desc1

        Unknown1:
            title1: content1

        Unknown2:
            title2: content2
        """
    )

    assert docstring.params[0].arg_name == "arg0"
    assert docstring.params[0].description == "desc0"
    assert docstring.params[1].arg_name == "arg1"
    assert docstring.params[1].description == "desc1"
