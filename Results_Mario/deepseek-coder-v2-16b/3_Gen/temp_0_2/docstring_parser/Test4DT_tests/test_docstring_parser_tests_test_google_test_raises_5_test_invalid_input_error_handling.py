
import pytest
from docstring_parser.tests.test_google import parse

def test_raises() -> None:
    """Test parsing raises."""
    # Test case for no raises section in the docstring
    docstring = parse(
        """
        Short description
        """
    )
    assert len(docstring.raises) == 0

    # Test case for a single raise statement with ValueError and its description
    docstring = parse(
        """
        Short description
        Raises:
            ValueError: description
        """
    )
    assert len(docstring.raises) == 1
    assert docstring.raises[0].type_name == "ValueError"
    assert docstring.raises[0].description == "description"
