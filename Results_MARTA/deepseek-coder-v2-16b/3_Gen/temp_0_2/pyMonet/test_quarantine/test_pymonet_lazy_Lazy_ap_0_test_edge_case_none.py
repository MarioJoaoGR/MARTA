
import pytest
from pymonet.lazy import Lazy

def test_ap():
    def expensive_computation(x):
        return x * x  # Example function to be called lazily
    
    lazy_value = Lazy(expensive_computation)
    assert not lazy_value.is_evaluated
    
    another_lazy_value = Lazy(lambda x: x + 1)
    
    result_lazy = lazy_value.ap(another_lazy_value)
    assert result_lazy.is_evaluated
    assert result_lazy.value == (lambda x: x + 1)(expensive_computation(1))

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

pyMonet/Test4DT_tests/test_pymonet_lazy_Lazy_ap_0_test_edge_case_none.py F [100%]

=================================== FAILURES ===================================
___________________________________ test_ap ____________________________________

    def test_ap():
        def expensive_computation(x):
            return x * x  # Example function to be called lazily
    
        lazy_value = Lazy(expensive_computation)
        assert not lazy_value.is_evaluated
    
        another_lazy_value = Lazy(lambda x: x + 1)
    
        result_lazy = lazy_value.ap(another_lazy_value)
>       assert result_lazy.is_evaluated
E       assert False
E        +  where False = <pymonet.lazy.Lazy object at 0x7f1a56f449d0>.is_evaluated

pyMonet/Test4DT_tests/test_pymonet_lazy_Lazy_ap_0_test_edge_case_none.py:15: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_lazy_Lazy_ap_0_test_edge_case_none.py::test_ap
============================== 1 failed in 0.10s ===============================
"""