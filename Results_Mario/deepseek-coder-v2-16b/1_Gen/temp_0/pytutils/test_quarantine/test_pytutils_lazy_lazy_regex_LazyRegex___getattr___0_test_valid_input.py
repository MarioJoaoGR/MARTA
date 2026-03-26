
import re
from pytutils.lazy import LazyRegex

def test_valid_input():
    lazy_regex = LazyRegex(r'\d+', ignorecase=True)
    assert hasattr(lazy_regex, 'findall')
    assert hasattr(lazy_regex, 'search')
    matches = lazy_regex.findall("123abc")
    assert matches == ['123']

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_lazy_lazy_regex_LazyRegex___getattr___0_test_valid_input
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_LazyRegex___getattr___0_test_valid_input.py:3:0: E0611: No name 'LazyRegex' in module 'pytutils.lazy' (no-name-in-module)


"""