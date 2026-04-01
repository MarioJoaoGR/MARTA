
import pytest
from docstring_parser.tests.test_epydoc import parse

def test_raises() -> None:
    """Test parsing raises."""
    # Test case for no raise statements
    docstring = parse(
        """
        Short description
        """
    )
    assert len(docstring.raises) == 0

    # Test case for single raise statement without a specific type
    docstring = parse(
        """
        Short description
        @raise: description
        """
    )
    assert len(docstring.raises) == 1
    assert docstring.raises[0].type_name is None
    assert docstring.raises[0].description == "description"

    # Test case for single raise statement with a specific type (ValueError)
    docstring = parse(
        """
        Short description
        @raise ValueError: description
        """
    )
    assert len(docstring.raises) == 1
    assert docstring.raises[0].type_name == "ValueError"
    assert docstring.raises[0].description == "description"
