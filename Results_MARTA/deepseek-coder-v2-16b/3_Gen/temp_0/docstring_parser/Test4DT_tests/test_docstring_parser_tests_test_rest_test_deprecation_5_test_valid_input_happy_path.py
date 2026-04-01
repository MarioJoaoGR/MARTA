
from docstring_parser.tests.test_rest import parse

def test_deprecation() -> None:
    """Test parsing deprecation notes."""
    docstring = parse(":deprecation: 1.1.0 this function will be removed")
    assert docstring.deprecation is not None
    assert docstring.deprecation.version == "1.1.0"
    assert docstring.deprecation.description == "this function will be removed"

    docstring = parse(":deprecation: this function will be removed")
    assert docstring.deprecation is not None
    assert docstring.deprecation.version is None
    assert docstring.deprecation.description == "this function will be removed"
