
import pytest
from docstring_parser.common import DocstringRaises

def test_init_with_all_parameters():
    args = ["arg1", "arg2"]
    description = "This function performs some operation."
    type_name = "ValueError"
    
    docstring_meta = DocstringRaises(args=args, description=description, type_name=type_name)
    
    assert docstring_meta.args == args
    assert docstring_meta.description == description
    assert docstring_meta.type_name == type_name

def test_init_without_optional_parameters():
    args = ["arg1", "arg2"]
    
    docstring_meta = DocstringRaises(args=args)
    
    assert docstring_meta.args == args
    assert docstring_meta.description is None
    assert docstring_meta.type_name is None

def test_init_with_only_required_parameters():
    args = ["arg1", "arg2"]
    
    docstring_meta = DocstringRaises(args=args, description="")
    
    assert docstring_meta.args == args
    assert docstring_meta.description == ""
    assert docstring_meta.type_name is None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_common_DocstringRaises___init___1_test_edge_cases
docstring_parser/Test4DT_tests/test_docstring_parser_common_DocstringRaises___init___1_test_edge_cases.py:19:21: E1120: No value for argument 'description' in constructor call (no-value-for-parameter)
docstring_parser/Test4DT_tests/test_docstring_parser_common_DocstringRaises___init___1_test_edge_cases.py:19:21: E1120: No value for argument 'type_name' in constructor call (no-value-for-parameter)
docstring_parser/Test4DT_tests/test_docstring_parser_common_DocstringRaises___init___1_test_edge_cases.py:28:21: E1120: No value for argument 'type_name' in constructor call (no-value-for-parameter)


"""