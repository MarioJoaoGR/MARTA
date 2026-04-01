
import pytest
from docstring_parser.tests.test_rest import parse

def test_meta_with_args() -> None:
    """Test parsing meta with additional arguments."""
    docstring = parse(
        """
        Short description

        :meta ene due rabe: asd
        """
    )
    assert docstring.short_description == "Short description"
    assert len(docstring.meta) == 1
    assert docstring.meta[0].args == ["meta", "ene", "due", "rabe"]
    assert docstring.meta[0].description == "asd"
