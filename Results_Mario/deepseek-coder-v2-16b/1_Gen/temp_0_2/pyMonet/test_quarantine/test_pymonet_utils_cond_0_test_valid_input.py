
import pytest
from pymonet.utils import cond

def is_even(n): return n % 2 == 0
def double(n): return n * 2
def triple(n): return n * 3
c = cond([(is_even, double), (lambda x: x > 5, triple)])

def test_valid_input():
    assert c(4) == 8  # is_even returns True for 4, so it should use the double function
    assert c(7) == 21  # lambda x: x > 5 returns True for 7, so it should use the triple function
    assert c(3) == 3  # Neither condition is met for 3, so it should return the default value or raise an error if not handled

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

pyMonet/Test4DT_tests/test_pymonet_utils_cond_0_test_valid_input.py F    [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        assert c(4) == 8  # is_even returns True for 4, so it should use the double function
        assert c(7) == 21  # lambda x: x > 5 returns True for 7, so it should use the triple function
>       assert c(3) == 3  # Neither condition is met for 3, so it should return the default value or raise an error if not handled
E       assert None == 3
E        +  where None = c(3)

pyMonet/Test4DT_tests/test_pymonet_utils_cond_0_test_valid_input.py:13: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_utils_cond_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.06s ===============================
"""