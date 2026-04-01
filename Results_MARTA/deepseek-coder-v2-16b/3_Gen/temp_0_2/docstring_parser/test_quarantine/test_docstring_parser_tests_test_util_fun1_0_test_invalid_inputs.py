
import pytest
from docstring_parser.tests.test_util import fun1

def test_invalid_inputs():
    """
    Test that fun1 raises an AssertionError when any of the arguments are None.
    """
    with pytest.raises(AssertionError):
        fun1(None, True, "string", [1, 2, 3])

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_util_fun1_0_test_invalid_inputs
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_util_fun1_0_test_invalid_inputs.py:3:0: E0611: No name 'fun1' in module 'docstring_parser.tests.test_util' (no-name-in-module)


"""