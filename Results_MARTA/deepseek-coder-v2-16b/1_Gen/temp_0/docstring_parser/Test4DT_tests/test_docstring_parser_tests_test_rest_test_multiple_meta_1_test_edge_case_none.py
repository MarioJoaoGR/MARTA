
import pytest
from docstring_parser.tests.test_rest import parse

def test_multiple_meta() -> None:
    """Test parsing multiple meta."""
    docstring = parse(
        """
        Short description

        :meta1: asd
            1
                2
            3
        :meta2: herp
        :meta3: derp
        """
    )
    assert docstring.short_description == "Short description"
    assert len(docstring.meta) == 3
    assert docstring.meta[0].args == ["meta1"]
    assert docstring.meta[0].description == "asd\n1\n    2\n3"
    assert docstring.meta[1].args == ["meta2"]
    assert docstring.meta[1].description == "herp"
    assert docstring.meta[2].args == ["meta3"]
    assert docstring.meta[2].description == "derp"
