
import pytest
from docstring_parser.tests.test_numpydoc import parse

def test_invalid_inputs():
    with pytest.raises(ValueError):
        parse("Short description", invalid_arg="invalid_value")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_numpydoc_test_attributes_2_test_invalid_inputs
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_attributes_2_test_invalid_inputs.py:7:8: E1123: Unexpected keyword argument 'invalid_arg' in function call (unexpected-keyword-arg)


"""