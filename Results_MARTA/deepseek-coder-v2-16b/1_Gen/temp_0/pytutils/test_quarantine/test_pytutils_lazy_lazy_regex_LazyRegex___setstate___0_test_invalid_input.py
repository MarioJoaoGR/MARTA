
import pytest
from pytutils.lazy.lazy_regex import LazyRegex

def test_invalid_input():
    with pytest.raises(TypeError):
        LazyRegex(invalid_arg="value")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_lazy_lazy_regex_LazyRegex___setstate___0_test_invalid_input
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_LazyRegex___setstate___0_test_invalid_input.py:7:8: E1123: Unexpected keyword argument 'invalid_arg' in constructor call (unexpected-keyword-arg)


"""