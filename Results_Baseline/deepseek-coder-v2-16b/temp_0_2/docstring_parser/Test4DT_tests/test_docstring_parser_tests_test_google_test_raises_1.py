
# Module: docstring_parser.tests.test_google
from docstring_parser import parse  # Corrected import statement
import pytest

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

    # New test case 3: No raises specified, should return empty list
    docstring = parse(
        """
        Short description
        """
    )
    assert len(docstring.raises) == 0, "Expected no raised exceptions but found some."

    # New test case 4: Multiple raises specified
    docstring = parse(
        """
        Short description
        Raises:
            ValueError: First exception
            TypeError: Second exception
        """
    )
    assert len(docstring.raises) == 2, "Expected two raised exceptions but found more."
    assert docstring.raises[0].type_name == "ValueError", f"Expected type 'ValueError' but got '{docstring.raises[0].type_name}'."
    assert docstring.raises[0].description == "First exception", f"Expected description 'First exception' but got '{docstring.raises[0].description}'."
    assert docstring.raises[1].type_name == "TypeError", f"Expected type 'TypeError' but got '{docstring.raises[1].type_name}'."
    assert docstring.raises[1].description == "Second exception", f"Expected description 'Second exception' but got '{docstring.raises[1].description}'."

    # New test case 5: No raises specified, should return empty list (edge case)
    docstring = parse(
        """
        Short description with no raises
        """
    )
    assert len(docstring.raises) == 0, "Expected no raised exceptions but found some."

    # New test case 6: Empty Raises section, should return empty list
    docstring = parse(
        """
        Short description
        Raises:
        """
    )
    assert len(docstring.raises) == 0, "Expected no raised exceptions but found some."

    # New test case 7: No raises specified, should return empty list (edge case with extra spaces)
    docstring = parse(
        """
        Short description  
        """
    )
    assert len(docstring.raises) == 0, "Expected no raised exceptions but found some."
