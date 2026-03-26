
import pytest
from docstring_parser.common import DocstringRaises

def test_invalid_inputs():
    # Test when args is not provided
    with pytest.raises(TypeError):
        DocstringRaises(description="A function that does something.", type_name="ValueError")

    # Test when description is not provided
    with pytest.raises(TypeError):
        DocstringRaises(args=["arg1", "arg2"], type_name="ValueError")

    # Test when type_name is not provided
    with pytest.raises(TypeError):
        DocstringRaises(args=["arg1", "arg2"], description="A function that does something.")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_common_DocstringRaises___init___2_test_invalid_inputs
docstring_parser/Test4DT_tests/test_docstring_parser_common_DocstringRaises___init___2_test_invalid_inputs.py:8:8: E1120: No value for argument 'args' in constructor call (no-value-for-parameter)
docstring_parser/Test4DT_tests/test_docstring_parser_common_DocstringRaises___init___2_test_invalid_inputs.py:12:8: E1120: No value for argument 'description' in constructor call (no-value-for-parameter)
docstring_parser/Test4DT_tests/test_docstring_parser_common_DocstringRaises___init___2_test_invalid_inputs.py:16:8: E1120: No value for argument 'type_name' in constructor call (no-value-for-parameter)


"""