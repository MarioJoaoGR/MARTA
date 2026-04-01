
import pytest
from docstring_parser.common import DocstringReturns

def test_invalid_inputs():
    with pytest.raises(TypeError):
        # Missing 'args' parameter
        DocstringReturns(description="This function does something.", type_name="int", is_generator=False, return_name="result")
        
    with pytest.raises(TypeError):
        # Missing 'description' parameter
        DocstringReturns(args=["arg1", "arg2"], type_name="int", is_generator=False, return_name="result")
        
    with pytest.raises(TypeError):
        # Missing 'type_name' parameter
        DocstringReturns(args=["arg1", "arg2"], description="This function does something.", is_generator=False, return_name="result")
        
    with pytest.raises(TypeError):
        # Missing 'is_generator' parameter
        DocstringReturns(args=["arg1", "arg2"], description="This function does something.", type_name="int", return_name="result")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_common_DocstringReturns___init___2_test_invalid_inputs
docstring_parser/Test4DT_tests/test_docstring_parser_common_DocstringReturns___init___2_test_invalid_inputs.py:8:8: E1120: No value for argument 'args' in constructor call (no-value-for-parameter)
docstring_parser/Test4DT_tests/test_docstring_parser_common_DocstringReturns___init___2_test_invalid_inputs.py:12:8: E1120: No value for argument 'description' in constructor call (no-value-for-parameter)
docstring_parser/Test4DT_tests/test_docstring_parser_common_DocstringReturns___init___2_test_invalid_inputs.py:16:8: E1120: No value for argument 'type_name' in constructor call (no-value-for-parameter)
docstring_parser/Test4DT_tests/test_docstring_parser_common_DocstringReturns___init___2_test_invalid_inputs.py:20:8: E1120: No value for argument 'is_generator' in constructor call (no-value-for-parameter)


"""