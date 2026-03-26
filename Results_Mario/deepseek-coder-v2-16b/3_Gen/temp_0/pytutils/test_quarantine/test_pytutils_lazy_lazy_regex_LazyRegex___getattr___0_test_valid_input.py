
import re
from pytutils.lazy.lazy_regex import LazyRegex

def test_valid_input():
    lazy_regex = LazyRegex(r'\d+', ignorecase=True)
    assert isinstance(lazy_regex._real_regex, re.Pattern)
    assert 'ignorecase' in str(lazy_regex._real_regex)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_lazy_lazy_regex_LazyRegex___getattr___0_test_valid_input
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_LazyRegex___getattr___0_test_valid_input.py:6:17: E1123: Unexpected keyword argument 'ignorecase' in constructor call (unexpected-keyword-arg)


"""