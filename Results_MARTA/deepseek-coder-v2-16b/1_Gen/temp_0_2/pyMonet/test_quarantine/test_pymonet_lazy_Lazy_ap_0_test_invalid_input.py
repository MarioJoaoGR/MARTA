
from pymonet.lazy import Lazy
import pytest

def test_invalid_input():
    # Test initialization with a non-callable object
    with pytest.raises(TypeError):
        lazy = Lazy("not_a_function")  # This should raise a TypeError

    # Test ap method with an invalid applicative
    def square(x):
        return x * x
    
    lazy1 = Lazy(lambda: 2)
    lazy2 = Lazy(lambda: "not_a_callable")  # This is not callable, should raise a TypeError when calling ap
    
    with pytest.raises(TypeError):
        combined_lazy = lazy1.ap(lazy2)  # This should raise a TypeError

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

pyMonet/Test4DT_tests/test_pymonet_lazy_Lazy_ap_0_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        # Test initialization with a non-callable object
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

pyMonet/Test4DT_tests/test_pymonet_lazy_Lazy_ap_0_test_invalid_input.py:7: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_lazy_Lazy_ap_0_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.07s ===============================
"""