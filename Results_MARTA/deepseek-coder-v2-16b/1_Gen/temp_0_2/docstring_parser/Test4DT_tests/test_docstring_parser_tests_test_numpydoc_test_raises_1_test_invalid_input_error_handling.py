
import pytest
from docstring_parser.tests.test_numpydoc import parse

def test_raises() -> None:
    """Test parsing raises."""
    # Test with no raises in the docstring
    docstring = parse(
        """
        Short description
        """
    )
    assert len(docstring.raises) == 0

    # Test with one raise in the docstring
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
