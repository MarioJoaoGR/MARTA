
import pytest
from typing import List, Optional
from docstring_parser.common import DocstringRaises

def test_docstring_raises_initialization_with_all_parameters():
    args = ["specific condition"]
    description = "If the input is negative"
    type_name = "ValueError"
    
    raises_info = DocstringRaises(args=args, description=description, type_name=type_name)
    
    assert raises_info.args == args
    assert raises_info.description == description
    assert raises_info.type_name == type_name

def test_docstring_raises_initialization_with_minimal_information():
    args = []
    description = None
    type_name = "TypeError"
    
    raises_info = DocstringRaises(args=args, description=description, type_name=type_name)
    
    assert raises_info.args == args
    assert raises_info.description == description
    assert raises_info.type_name == type_name

def test_docstring_raises_initialization_with_no_additional_arguments_and_detailed_description():
    args = []
    description = "This exception is raised when the input does not meet the required format."
    type_name = "FormatError"
    
    raises_info = DocstringRaises(args=args, description=description, type_name=type_name)
    
    assert raises_info.args == args
    assert raises_info.description == description
    assert raises_info.type_name == type_name

def test_docstring_raises_initialization_with_empty_description():
    args = ["when x < 0"]
    description = ""
    type_name = "ValueError"
    
    raises_info = DocstringRaises(args=args, description=description, type_name=type_name)
    
    assert raises_info.args == args
    assert raises_info.description == description
    assert raises_info.type_name == type_name

def test_docstring_raises_initialization_with_no_type_name():
    args = []
    description = "An unexpected error occurred."
    type_name = None
    
    raises_info = DocstringRaises(args=args, description=description, type_name=type_name)
    
    assert raises_info.args == args
    assert raises_info.description == description
    assert raises_info.type_name == type_name

def test_docstring_raises_initialization_with_empty_args():
    args: List[str] = []
    description = "An unexpected error occurred."
    type_name = "RuntimeError"
    
    raises_info = DocstringRaises(args=args, description=description, type_name=type_name)
    
    assert raises_info.args == args
    assert raises_info.description == description