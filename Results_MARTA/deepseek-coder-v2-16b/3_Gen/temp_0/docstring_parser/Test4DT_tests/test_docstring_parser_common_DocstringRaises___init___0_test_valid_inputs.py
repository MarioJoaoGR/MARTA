
import pytest
from docstring_parser.common import DocstringRaises

def test_valid_inputs():
    # Test valid inputs for the DocstringRaises class
    args = ['arg1', 'arg2']
    description = 'This function performs some operation.'
    type_name = 'ValueError'
    
    docstring_meta = DocstringRaises(args=args, description=description, type_name=type_name)
    
    assert docstring_meta.args == args
    assert docstring_meta.description == description
    assert docstring_meta.type_name == type_name
