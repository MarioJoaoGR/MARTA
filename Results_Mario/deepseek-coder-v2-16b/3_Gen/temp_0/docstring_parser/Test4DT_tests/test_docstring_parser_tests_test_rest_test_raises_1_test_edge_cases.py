
import pytest
from docstring_parser.tests.test_rest import parse

def test_raises() -> None:
    """Test parsing raises."""
    # Test case for no exceptions
    docstring = parse(
        """
        Short description
        """
    )
    assert len(docstring.raises) == 0

    # Test case for single exception without type specified
    docstring = parse(
        """
        Short description
        :raises: description
        """
    )
    assert len(docstring.raises) == 1
    assert docstring.raises[0].type_name is None
    assert docstring.raises[0].description == "description"

    # Test case for single exception with type specified
    docstring = parse(
        """
        Short description
        :raises ValueError: description
        """
    )
    assert len(docstring.raises) == 1
    assert docstring.raises[0].type_name == "ValueError"
    assert docstring.raises[0].description == "description"
