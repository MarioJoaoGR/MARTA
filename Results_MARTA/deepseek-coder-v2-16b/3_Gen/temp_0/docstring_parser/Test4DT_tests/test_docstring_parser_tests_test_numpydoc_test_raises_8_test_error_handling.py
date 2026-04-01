
import pytest
from docstring_parser.tests.test_numpydoc import parse

def test_raises() -> None:
    """Test parsing raises."""
    # Test with no raise statements
    docstring = parse(
        """
        Short description
        """
    )
    assert len(docstring.raises) == 0, "Expected 0 raises but found some."

    # Test with one raise statement
    docstring = parse(
        """
        Short description
        Raises
        ------
        ValueError
            description
        """
    )
    assert len(docstring.raises) == 1, "Expected 1 raises but found more."
    assert docstring.raises[0].type_name == "ValueError", "Raised exception type does not match expected ValueError."
    assert docstring.raises[0].description == "description", "Description of raised exception does not match expected 'description'."
