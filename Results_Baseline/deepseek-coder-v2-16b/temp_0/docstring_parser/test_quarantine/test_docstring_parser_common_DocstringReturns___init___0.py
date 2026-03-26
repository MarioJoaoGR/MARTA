
# Module: docstring_parser.common
# test_docstring_parser.py
from docstring_parser.common import DocstringReturns
import pytest
import typing as T

def test_init():
    """Test the initialization of DocstringReturns."""
    args = ["arg1", "arg2"]
    description = "This function does something."
    type_name = "int"
    is_generator = False
    return_name = "result"
    
    docstring_meta = DocstringReturns(args=args, description=description, type_name=type_name, is_generator=is_generator, return_name=return_name)
    
    assert docstring_meta.args == args
    assert docstring_meta.description == description
    assert docstring_meta.type_name == type_name
    assert docstring_meta.is_generator == is_generator
    assert docstring_meta.return_name == return_name

def test_init_no_return_name():
    """Test the initialization of DocstringReturns without a return name."""
    args = ["arg1", "arg2"]
    description = "This function does something."
    type_name = "int"
    is_generator = False
    
    docstring_meta = DocstringReturns(args=args, description=description, type_name=type_name, is_generator=is_generator)
    
    assert docstring_meta.args == args
    assert docstring_meta.description == description
    assert docstring_meta.type_name == type_name
    assert docstring_meta.is_generator == is_generator
    assert docstring_meta.return_name is None

def test_init_with_only_args():
    """Test the initialization of DocstringReturns with only args."""
    args = ["arg1", "arg2"]
    
    docstring_meta = DocstringReturns(args=args)
    
    assert docstring_meta.args == args
    assert docstring_meta.description is None
    assert docstring_meta.type_name is None
    assert not docstring_meta.is_generator
    assert docstring_meta.return_name is None

def test_init_with_all_parameters():
    """Test the initialization of DocstringReturns with all parameters."""
    args = ["arg1", "arg2"]
    description = "This function does something."
    type_name = "int"
    is_generator = True
    return_name = "result"
    
    docstring_meta = DocstringReturns(args=args, description=description, type_name=type_name, is_generator=is_generator, return_name=return_name)
    
    assert docstring_meta.args == args
    assert docstring_meta.description == description
    assert docstring_meta.type_name == type_name
    assert docstring_meta.is_generator == is_generator
    assert docstring_meta.return_name == return_name

def test_init_with_invalid_parameters():
    """Test the initialization of DocstringReturns with invalid parameters."""
    args = "not a list"  # Invalid type for args
    
    with pytest.raises(TypeError):
        docstring_meta = DocstringReturns(args=args)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_common_DocstringReturns___init___0
docstring_parser/Test4DT_tests/test_docstring_parser_common_DocstringReturns___init___0.py:43:21: E1120: No value for argument 'description' in constructor call (no-value-for-parameter)
docstring_parser/Test4DT_tests/test_docstring_parser_common_DocstringReturns___init___0.py:43:21: E1120: No value for argument 'type_name' in constructor call (no-value-for-parameter)
docstring_parser/Test4DT_tests/test_docstring_parser_common_DocstringReturns___init___0.py:43:21: E1120: No value for argument 'is_generator' in constructor call (no-value-for-parameter)
docstring_parser/Test4DT_tests/test_docstring_parser_common_DocstringReturns___init___0.py:72:25: E1120: No value for argument 'description' in constructor call (no-value-for-parameter)
docstring_parser/Test4DT_tests/test_docstring_parser_common_DocstringReturns___init___0.py:72:25: E1120: No value for argument 'type_name' in constructor call (no-value-for-parameter)
docstring_parser/Test4DT_tests/test_docstring_parser_common_DocstringReturns___init___0.py:72:25: E1120: No value for argument 'is_generator' in constructor call (no-value-for-parameter)

"""