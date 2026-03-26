
# Module: docstring_parser.common
# test_docstring_returns.py
import pytest
from typing import List, Optional

# Import the DocstringReturns class from its module
from docstring_parser.common import DocstringReturns

def test_init():
    """Test initialization of DocstringReturns."""
    # Test with all parameters provided
    docstring = DocstringReturns(args=["arg1"], description="The result of the operation", type_name="str", is_generator=False, return_name="result")
    assert docstring.args == ["arg1"]
    assert docstring.description == "The result of the operation"
    assert docstring.type_name == "str"
    assert docstring.is_generator == False
    assert docstring.return_name == "result"

def test_init_default():
    """Test initialization with default values."""
    # Test without optional parameters
    docstring = DocstringReturns(args=["arg1"], description="The result of the operation", type_name=None, is_generator=False, return_name=None)
    assert docstring.args == ["arg1"]
    assert docstring.description == "The result of the operation"
    assert docstring.type_name is None
    assert docstring.is_generator == False
    assert docstring.return_name is None

def test_init_no_args():
    """Test initialization without args."""
    # Test with missing required parameter 'args'
    with pytest.raises(TypeError):
        DocstringReturns()

def test_init_missing_description():
    """Test initialization without description."""
    # Test with missing required parameter 'description'
    with pytest.raises(TypeError):
        DocstringReturns(args=["arg1"], type_name="str", is_generator=False, return_name="result")

def test_init_missing_type_name():
    """Test initialization without type_name."""
    # Test with missing required parameter 'type_name'
    with pytest.raises(TypeError):
        DocstringReturns(args=["arg1"], description="The result of the operation", is_generator=False, return_name="result")

def test_init_missing_is_generator():
    """Test initialization without is_generator."""
    # Test with missing required parameter 'is_generator'
    with pytest.raises(TypeError):
        DocstringReturns(args=["arg1"], description="The result of the operation", type_name="str", return_name="result")

def test_init_missing_return_name():
    """Test initialization without return_name."""
    # Test with missing optional parameter 'return_name'
    docstring = DocstringReturns(args=["arg1"], description="The result of the operation", type_name="str", is_generator=False)
    assert docstring.args == ["arg1"]
    assert docstring.description == "The result of the operation"
    assert docstring.type_name == "str"
    assert docstring.is_generator == False
    assert docstring.return_name is None

def test_example():
    """Test example usage from the class documentation."""
    # Example usage as provided in the documentation
    class ExampleClass:
        def example_function(self, arg1: int) -> str:
            return "result"
    
    docstring = DocstringReturns(args=["arg1"], description="The result of the operation", type_name="str", is_generator=False, return_name="result")
    assert docstring.return_name == "result"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_common_DocstringReturns___init___0
docstring_parser/Test4DT_tests/test_docstring_parser_common_DocstringReturns___init___0.py:34:8: E1120: No value for argument 'args' in constructor call (no-value-for-parameter)
docstring_parser/Test4DT_tests/test_docstring_parser_common_DocstringReturns___init___0.py:34:8: E1120: No value for argument 'description' in constructor call (no-value-for-parameter)
docstring_parser/Test4DT_tests/test_docstring_parser_common_DocstringReturns___init___0.py:34:8: E1120: No value for argument 'type_name' in constructor call (no-value-for-parameter)
docstring_parser/Test4DT_tests/test_docstring_parser_common_DocstringReturns___init___0.py:34:8: E1120: No value for argument 'is_generator' in constructor call (no-value-for-parameter)
docstring_parser/Test4DT_tests/test_docstring_parser_common_DocstringReturns___init___0.py:40:8: E1120: No value for argument 'description' in constructor call (no-value-for-parameter)
docstring_parser/Test4DT_tests/test_docstring_parser_common_DocstringReturns___init___0.py:46:8: E1120: No value for argument 'type_name' in constructor call (no-value-for-parameter)
docstring_parser/Test4DT_tests/test_docstring_parser_common_DocstringReturns___init___0.py:52:8: E1120: No value for argument 'is_generator' in constructor call (no-value-for-parameter)

"""