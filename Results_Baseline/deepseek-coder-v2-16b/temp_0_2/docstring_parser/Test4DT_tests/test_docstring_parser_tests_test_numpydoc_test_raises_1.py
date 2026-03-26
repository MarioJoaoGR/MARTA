
# Module: docstring_parser.tests.test_numpydoc
from docstring_parser import parse  # Importing from the correct module name

def test_raises():
    """Test parsing raises."""
    
    # Test case 1: No raises section in docstring
    docstring = parse(
        """
        Short description
        """
    )
    assert len(docstring.raises) == 0, "Expected no raises but found some."

    # Test case 2: With a single raise entry in the raises section
    docstring = parse(
        """
        Short description
        Raises
        ------
        ValueError
            description
        """
    )
    assert len(docstring.raises) == 1, "Expected one raise but found more."
    assert docstring.raises[0].type_name == "ValueError", f"Expected type 'ValueError' but got {docstring.raises[0].type_name}."
    assert docstring.raises[0].description == "description", f"Expected description 'description' but got '{docstring.raises[0].description}'."
    
    # Test case 3: No raises section with additional content in the docstring
    docstring = parse(
        """
        Short description
        Additional Content
        """
    )
    assert len(docstring.raises) == 0, "Expected no raises but found some."
    
    # Test case 4: With multiple raise entries in the raises section
    docstring = parse(
        """
        Short description
        Raises
        ------
        ValueError
            description for ValueError
        TypeError
            description for TypeError
        """
    )
    assert len(docstring.raises) == 2, "Expected two raises but found more."
    assert docstring.raises[0].type_name == "ValueError", f"Expected type 'ValueError' but got {docstring.raises[0].type_name}."
    assert docstring.raises[0].description == "description for ValueError", f"Expected description 'description for ValueError' but got '{docstring.raises[0].description}'."
    assert docstring.raises[1].type_name == "TypeError", f"Expected type 'TypeError' but got {docstring.raises[1].type_name}."
    assert docstring.raises[1].description == "description for TypeError", f"Expected description 'description for TypeError' but got '{docstring.raises[1].description}'."
    
    # Test case 5: Empty raises section in the docstring
    docstring = parse(
        """
        Short description
        Raises
        ------
        """
    )
    assert len(docstring.raises) == 0, "Expected no raises but found some."
    
    # Test case 6: No raises section with a different style of empty raises section in the docstring
    docstring = parse(
        """
        Short description
        Raises
        ------
    
        More content
        """
    )