# Module: docstring_parser.tests.test_epydoc
# test_epydoc.py
from docstring_parser import parse

def test_raises():
    """Test parsing raises."""
    
    # Test case 1: No raise statements in the docstring
    docstring = parse(
        """
        Short description
        """
    )
    assert len(docstring.raises) == 0, "Expected no raises to be parsed when there are none."

    # Test case 2: Raise statement without a type name
    docstring = parse(
        """
        Short description
        @raise: description
        """
    )
    assert len(docstring.raises) == 1, "Expected one raise to be parsed when only the description is provided."
    assert docstring.raises[0].type_name is None, "Expected type name to be None for a generic raise statement."
    assert docstring.raises[0].description == "description", "Expected the description to match 'description' exactly."

    # Test case 3: Raise statement with a specific type name (ValueError)
    docstring = parse(
        """
        Short description
        @raise ValueError: description
        """
    )
    assert len(docstring.raises) == 1, "Expected one raise to be parsed when specifying the exception type."
    assert docstring.raises[0].type_name == "ValueError", "Expected type name to be 'ValueError' exactly."
    assert docstring.raises[0].description == "description", "Expected the description to match 'description' exactly."
