
import pytest
from pymonet.lazy import Lazy

def test_edge_case_none():
    def square(x):
        return x * x
    
    lazy = Lazy(square)
    with pytest.raises(AttributeError):
        assert lazy.constructor_fn is None  # This will fail if the constructor_fn attribute is not properly set to None

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

pyMonet/Test4DT_tests/test_pymonet_lazy_Lazy___init___0_test_edge_case_none.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_edge_case_none ______________________________

    def test_edge_case_none():
        def square(x):
            return x * x
    
        lazy = Lazy(square)
        with pytest.raises(AttributeError):
>           assert lazy.constructor_fn is None  # This will fail if the constructor_fn attribute is not properly set to None
E           assert <function test_edge_case_none.<locals>.square at 0x7f7aa1efb9c0> is None
E            +  where <function test_edge_case_none.<locals>.square at 0x7f7aa1efb9c0> = <pymonet.lazy.Lazy object at 0x7f7aa1ebec10>.constructor_fn

pyMonet/Test4DT_tests/test_pymonet_lazy_Lazy___init___0_test_edge_case_none.py:11: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_lazy_Lazy___init___0_test_edge_case_none.py::test_edge_case_none
============================== 1 failed in 0.07s ===============================
"""