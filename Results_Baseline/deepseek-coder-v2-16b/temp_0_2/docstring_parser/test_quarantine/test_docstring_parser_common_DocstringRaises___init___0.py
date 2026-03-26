
# Module: docstring_parser.common
# test_docstring_parser.py
import pytest
from docstring_parser.common import DocstringRaises

def test_initialization():
    # Test initialization with all parameters provided
    metadata = DocstringRaises(args=["arg1", "arg2"], description="This function does something useful.", type_name="SomeType")
    assert metadata.type_name == "SomeType"
    assert metadata.description == "This function does something useful."
    
    # Test initialization with missing optional parameters
    metadata_no_type = DocstringRaises(args=["arg1", "arg2"], description="This function does something useful.")
    assert metadata_no_type.type_name is None
    assert metadata_no_type.description == "This function does something useful."
    
    # Test initialization with missing both optional parameters
    metadata_none = DocstringRaises(args=["arg1", "arg2"])
    assert metadata_none.type_name is None
    assert metadata_none.description is None

def test_inheritance():
    # Ensure that the class inherits from super().__init__ correctly
    metadata = DocstringRaises(args=["arg1", "arg2"], description="This function does something useful.", type_name="SomeType")
    assert hasattr(metadata, '_DocstringMeta__args') and hasattr(metadata, '_DocstringMeta__description')
    
def test_str_representation():
    # Test the string representation of the class
    metadata = DocstringRaises(args=["arg1", "arg2"], description="This function does something useful.", type_name="SomeType")
    assert str(metadata) == "DocstringRaises(args=['arg1', 'arg2'], description='This function does something useful.', type_name='SomeType')"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_common_DocstringRaises___init___0
docstring_parser/Test4DT_tests/test_docstring_parser_common_DocstringRaises___init___0.py:14:23: E1120: No value for argument 'type_name' in constructor call (no-value-for-parameter)
docstring_parser/Test4DT_tests/test_docstring_parser_common_DocstringRaises___init___0.py:19:20: E1120: No value for argument 'description' in constructor call (no-value-for-parameter)
docstring_parser/Test4DT_tests/test_docstring_parser_common_DocstringRaises___init___0.py:19:20: E1120: No value for argument 'type_name' in constructor call (no-value-for-parameter)

"""