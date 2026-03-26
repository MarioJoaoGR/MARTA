
import pytest
from docstring_parser.tests.test_numpydoc import parse

def test_raises() -> None:
    """Test parsing raises."""
    # Test with invalid docstring format (no raise statements)
    docstring = parse(
        """
        Short description
        """
    )
    assert len(docstring.raises) == 0, "Expected 0 raises but found more"

    # Test with valid docstring containing a single raise statement
    docstring = parse(
        """
        Short description
        Raises
        ------
        ValueError
            description
        """
    )
    assert len(docstring.raises) == 1, "Expected 1 raise but found more"
    assert docstring.raises[0].type_name == "ValueError", "Raised exception type does not match expected ValueError"
    assert docstring.raises[0].description == "description", "Description of raised exception does not match expected 'description'"
