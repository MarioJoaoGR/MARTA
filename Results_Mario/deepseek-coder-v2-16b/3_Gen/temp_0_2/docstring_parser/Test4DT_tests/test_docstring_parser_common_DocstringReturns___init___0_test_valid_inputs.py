
import pytest
from docstring_parser.common import DocstringReturns

def test_valid_inputs():
    # Test with valid inputs
    args = ["arg1", "arg2"]
    description = "This function does something."
    type_name = "int"
    is_generator = False
    return_name = "result"
    
    docstring = DocstringReturns(args=args, description=description, type_name=type_name, is_generator=is_generator, return_name=return_name)
    
    assert docstring.args == args
    assert docstring.description == description
    assert docstring.type_name == type_name
    assert docstring.is_generator == is_generator
    assert docstring.return_name == return_name
