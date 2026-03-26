
import pytest
from docstring_parser import parse

# Test case for parsing a function with both short and long descriptions
def test_long_description_1():
    source = """
    A brief description of what this function does.
    
    Extended documentation or explanation follows here.
    
    Parameters:
        param1 (type): Description of param1.
        param2 (type): Description of param2.
        
    Returns:
        type: Description of the return value.
    """
    expected_short_desc = "A brief description of what this function does."
    expected_long_desc = "Extended documentation or explanation follows here."
    docstring = parse(source)
    assert docstring.short_description == expected_short_desc
    assert docstring.long_description == expected_long_desc

# Test case for a function without any long description
def test_long_description_2():
    source = "A brief description without any long explanation."
    expected_short_desc = "A brief description without any long explanation."
    docstring = parse(source)
    assert docstring.short_description == expected_short_desc
    assert docstring.long_description is None or docstring.long_description == ""

# Test case for a function with only metadata (no short or long description)
def test_long_description_3():
    source = """
    Parameters:
        param1 (type): Description of param1.
        param2 (type): Description of param2.
        
    Returns:
        type: Description of the return value.
    """
    expected_short_desc = ""
    expected_long_desc = ""
    docstring = parse(source)