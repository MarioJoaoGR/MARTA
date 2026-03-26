
# Module: docstring_parser.tests.test_numpydoc
# Import the function using its provided module name
from docstring_parser import parse
import typing as T

def test_meta_newlines():
    # Test case with a typical numpy-style docstring containing newlines around descriptions
    source = """
        A short description.
        
        Long description that spans multiple lines.
        
        Parameters:
            param1 (type): Description of param1.
            param2 (type): Description of param2.
        
        Returns:
            type: Description of the return value.
    """
    
    # Expected values after parsing the docstring
    expected_short_desc = "A short description."
    expected_long_desc = "Long description that spans multiple lines."
    expected_blank_short_desc = True
    expected_blank_long_desc = False
    
    # Call the function with the test case data
    docstring = parse(source)
    
    # Assertions to verify the parsed results match the expected values
    assert docstring.short_description == expected_short_desc, f"Expected short description: {expected_short_desc}, but got: {docstring.short_description}"
    assert docstring.long_description == expected_long_desc, f"Expected long description: {expected_long_desc}, but got: {docstring.long_description}"
    assert docstring.blank_after_short_description == expected_blank_short_desc, f"Expected blank after short description: {expected_blank_short_desc}, but got: {docstring.blank_after_short_description}"