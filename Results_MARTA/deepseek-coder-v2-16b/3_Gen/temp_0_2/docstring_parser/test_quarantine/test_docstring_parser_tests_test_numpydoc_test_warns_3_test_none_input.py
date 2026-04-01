
import pytest
from docstring_parser.tests.test_numpydoc import parse

def test_none_input():
    with pytest.raises(TypeError):
        parse()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_numpydoc_test_warns_3_test_none_input
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_warns_3_test_none_input.py:7:8: E1120: No value for argument 'text' in function call (no-value-for-parameter)


"""