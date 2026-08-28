
import pytest
from docstring_parser import parse
from docstring_parser.numpydoc import Docstring, NumpydocParser

# Test cases for the parse function
def test_basic_usage():
    text = """
    A short description.
    
    Long description with details.
    
    Parameters:
        param1 (type): Description of param1.
        param2 (type): Description of param2.
        
    Returns:
        type: Description of the return value.
    """
    docstring = parse(text)
    assert docstring.short_description == "A short description."
    assert docstring.long_description == "Long description with details."
    # Assuming meta contains metadata about parameters and return value