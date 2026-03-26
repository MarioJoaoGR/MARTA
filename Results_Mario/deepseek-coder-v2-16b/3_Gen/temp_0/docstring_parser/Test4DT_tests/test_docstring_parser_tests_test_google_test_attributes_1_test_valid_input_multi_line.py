
from docstring_parser.tests.test_google import parse

def test_attributes() -> None:
    """Test parsing attributes from a Google-style docstring."""
    # Test case for empty docstring
    docstring = parse("Short description")
    assert len(docstring.params) == 0

    # Test case for multi-line attribute descriptions
    docstring = parse(
        """
        Short description

        Attributes:
            name: description 1
                with multi-line text
            priority (int): description 2
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
    assert docstring.params[1].description == "description 2"
