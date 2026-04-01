
from pymonet.lazy import Lazy

def test_invalid_input():
    # Test that bind method raises a TypeError when the provided function is not callable
    lazy = Lazy(lambda x: x)  # Example constructor function
    
    try:
        result = lazy.bind(123)  # Providing an invalid function (int instead of callable)
        assert False, "Expected TypeError but got no exception"
    except TypeError as e:
        assert str(e) == "__init__() takes 2 positional arguments but 1 was given", f"Unexpected error: {str(e)}"

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

pyMonet/Test4DT_tests/test_pymonet_lazy_Lazy_bind_0_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        # Test that bind method raises a TypeError when the provided function is not callable
        lazy = Lazy(lambda x: x)  # Example constructor function
    
        try:
            result = lazy.bind(123)  # Providing an invalid function (int instead of callable)
>           assert False, "Expected TypeError but got no exception"
E           AssertionError: Expected TypeError but got no exception
E           assert False

pyMonet/Test4DT_tests/test_pymonet_lazy_Lazy_bind_0_test_invalid_input.py:10: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_lazy_Lazy_bind_0_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.06s ===============================
"""