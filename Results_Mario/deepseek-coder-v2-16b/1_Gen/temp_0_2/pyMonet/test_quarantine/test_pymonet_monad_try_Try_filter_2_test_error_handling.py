
from pymonet.monad_try import Try

def test_error_handling():
    none_try = Try(None, True)
    
    def is_even(n):
        return n % 2 == 0
    
    # Test when the value is even and should be successful
    filtered_success = none_try.filter(is_even)
    assert filtered_success.is_success, "Expected success but got failure"
    assert filtered_success.value is None, "Expected value to be None"

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

pyMonet/Test4DT_tests/test_pymonet_monad_try_Try_filter_2_test_error_handling.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_error_handling ______________________________

    def test_error_handling():
        none_try = Try(None, True)
    
        def is_even(n):
            return n % 2 == 0
    
        # Test when the value is even and should be successful
>       filtered_success = none_try.filter(is_even)

pyMonet/Test4DT_tests/test_pymonet_monad_try_Try_filter_2_test_error_handling.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
pyMonet/pymonet/monad_try.py:103: in filter
    if self.is_success and filterer(self.value):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

n = None

    def is_even(n):
>       return n % 2 == 0
E       TypeError: unsupported operand type(s) for %: 'NoneType' and 'int'

pyMonet/Test4DT_tests/test_pymonet_monad_try_Try_filter_2_test_error_handling.py:8: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_monad_try_Try_filter_2_test_error_handling.py::test_error_handling
============================== 1 failed in 0.07s ===============================
"""