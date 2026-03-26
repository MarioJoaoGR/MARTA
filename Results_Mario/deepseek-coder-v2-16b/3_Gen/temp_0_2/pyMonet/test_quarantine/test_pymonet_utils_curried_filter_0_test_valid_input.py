
import pytest
from pymonet.utils import curried_filter

def test_valid_input():
    def is_even(n):
        return n % 2 == 0
    
    assert curried_filter(is_even, [1, 2, 3, 4]) == [2, 4]
    assert curried_filter(lambda x: x > 5, [1, 7, 9, 10]) == [7, 9, 10]
    assert curried_filter(lambda x: isinstance(x, str) and len(x) > 3, ["apple", "banana", "cat"]) == ["banana"]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pyMonet
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

pyMonet/Test4DT_tests/test_pymonet_utils_curried_filter_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        def is_even(n):
            return n % 2 == 0
    
        assert curried_filter(is_even, [1, 2, 3, 4]) == [2, 4]
        assert curried_filter(lambda x: x > 5, [1, 7, 9, 10]) == [7, 9, 10]
>       assert curried_filter(lambda x: isinstance(x, str) and len(x) > 3, ["apple", "banana", "cat"]) == ["banana"]
E       AssertionError: assert ['apple', 'banana'] == ['banana']
E         
E         At index 0 diff: 'apple' != 'banana'
E         Left contains one more item: 'banana'
E         Use -v to get more diff

pyMonet/Test4DT_tests/test_pymonet_utils_curried_filter_0_test_valid_input.py:11: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_utils_curried_filter_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.08s ===============================
"""