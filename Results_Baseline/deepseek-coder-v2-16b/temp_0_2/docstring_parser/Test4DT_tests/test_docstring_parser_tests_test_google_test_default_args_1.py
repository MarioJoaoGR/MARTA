
# Module: docstring_parser.tests.test_google
from docstring_parser.tests.test_google import parse

def test_default_args():
    """Test parsing default arguments."""
    docstring = parse(
        """A sample function

A function the demonstrates docstrings

Args:
    arg1 (int): The firsty arg
    arg2 (str): The second arg
    arg3 (float, optional): The third arg. Defaults to 1.0.
    arg4 (Optional[Dict[str, Any]], optional): The last arg. Defaults to None.
    arg5 (str, optional): The fifth arg. Defaults to DEFAULT_ARG5.

Returns:
    Mapping[str, Any]: The args packed in a mapping
"""
    )
    
    # Test that the docstring is not None after parsing
    assert docstring is not None
    
    # Test that there are exactly 5 parameters
    assert len(docstring.params) == 5
    
    # Test individual parameter details for arg4
    arg4 = docstring.params[3]
    assert arg4.arg_name == "arg4"
    assert arg4.is_optional
    assert arg4.type_name == "Optional[Dict[str, Any]]"
    assert arg4.default == "None"
    assert arg4.description == "The last arg. Defaults to None."
    
    # Additional test cases for other parameters (arg1, arg2, arg3, arg5) can be added if needed
    # For example:
    arg1 = docstring.params[0]
    assert not arg1.is_optional
    assert arg1.type_name == "int"
    
    arg2 = docstring.params[1]
    assert not arg2.is_optional
    assert arg2.type_name == "str"
    
    arg3 = docstring.params[2]
    assert arg3.is_optional
    assert arg3.type_name == "float"
    assert arg3.default == "1.0"
    
    arg5 = docstring.params[4]
    assert arg5.is_optional
    assert arg5.type_name == "str"
    assert arg5.default == "DEFAULT_ARG5"
