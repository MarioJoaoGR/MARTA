
# Module: docstring_parser.tests.test_rest
# Import the function from its module
from docstring_parser.tests.test_rest import test_meta_with_args

def test_parse():
    # Test parsing a ReST-style docstring with metadata
    from docstring_parser import parse  # Corrected the import and variable usage
    
    docstring = parse(
        """
        Short description

        :meta ene due rabe: asd
        """
    )
    
    # Assertions for the short description, number of meta entries, and details of each meta entry
    assert docstring.short_description == "Short description"
    assert len(docstring.meta) == 1
    assert docstring.meta[0].args == ["meta", "ene", "due", "rabe"]
    assert docstring.meta[0].description == "asd"

# Run the original function to ensure it still works as expected
test_meta_with_args()
