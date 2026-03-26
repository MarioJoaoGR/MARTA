
import pytest
from docstring_parser.tests.test_rest import parse

def test_meta_with_multiline_description() -> None:
    """Test parsing multiline meta documentation."""
    docstring = parse(
        """
        Short description

        :meta: asd
            1
                2
            3
        """
    )
    assert docstring.short_description == "Short description"
    assert len(docstring.meta) == 1
    assert docstring.meta[0].args == ["meta"]
    assert docstring.meta[0].description == "asd\n1\n    2\n3"
