
from docstring_parser.tests.test_numpydoc import parse

def test_raises() -> None:
    """Test parsing raises."""
    # Test case for no exceptions in the docstring
    docstring = parse(
        """
        Short description
        """
    )
    assert len(docstring.raises) == 0

    # Test case for one exception in the docstring
    docstring = parse(
        """
        Short description
        Raises
        ------
        ValueError
            description
        """
    )
    assert len(docstring.raises) == 1
    assert docstring.raises[0].type_name == "ValueError"
    assert docstring.raises[0].description == "description"
