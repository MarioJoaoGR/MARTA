
# Module: docstring_parser.tests.test_google
# test_google.py
from docstring_parser import parse  # Corrected import statement

def test_raises():
    """Test parsing raises."""
    # Test case 1: No Raises section in the docstring
    docstring = parse(
        """
        Short description
        """
    )
    assert len(docstring.raises) == 0, "Expected no raised exceptions but found some."

    # Test case 2: With Raises section in the docstring
    docstring = parse(
        """
        Short description
        Raises:
            ValueError: description
        """
    )
    assert len(docstring.raises) == 1, "Expected one raised exception but found more."
    assert docstring.raises[0].type_name == "ValueError", f"Expected type 'ValueError' but got '{docstring.raises[0].type_name}'."
    assert docstring.raises[0].description == "description", f"Expected description 'description' but got '{docstring.raises[0].description}'."
