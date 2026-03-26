
# Module: docstring_parser.tests.test_numpydoc
from docstring_parser import parse  # Importing from the correct module name

def test_raises():
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
