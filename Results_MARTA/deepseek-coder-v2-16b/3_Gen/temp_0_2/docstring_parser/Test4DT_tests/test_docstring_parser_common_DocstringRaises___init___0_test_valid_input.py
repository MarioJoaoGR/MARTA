
import pytest
from typing import List, Optional
from docstring_parser.common import DocstringRaises

def test_valid_input():
    # Test initialization with valid input
    args = ["arg1", "arg2"]
    description = "This function performs a critical operation."
    type_name = "ValueError"
    
    docstring_instance = DocstringRaises(args=args, description=description, type_name=type_name)
    
    assert docstring_instance.args == args
    assert docstring_instance.description == description
    assert docstring_instance.type_name == type_name
