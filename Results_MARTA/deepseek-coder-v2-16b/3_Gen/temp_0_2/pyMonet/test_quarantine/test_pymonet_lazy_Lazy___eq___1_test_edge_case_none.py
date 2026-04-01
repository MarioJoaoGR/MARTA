
import pytest
from pymonet.lazy import Lazy

def test_edge_case_none():
    lazy_instance = Lazy(lambda x: x)
    assert lazy_instance == Lazy(lambda x: x)

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

pyMonet/Test4DT_tests/test_pymonet_lazy_Lazy___eq___1_test_edge_case_none.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_edge_case_none ______________________________

    def test_edge_case_none():
        lazy_instance = Lazy(lambda x: x)
>       assert lazy_instance == Lazy(lambda x: x)
E       assert <pymonet.lazy.Lazy object at 0x7f166cbca290> == <pymonet.lazy.Lazy object at 0x7f166cc04150>
E        +  where <pymonet.lazy.Lazy object at 0x7f166cc04150> = Lazy(<function test_edge_case_none.<locals>.<lambda> at 0x7f166cbb27a0>)

pyMonet/Test4DT_tests/test_pymonet_lazy_Lazy___eq___1_test_edge_case_none.py:7: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_lazy_Lazy___eq___1_test_edge_case_none.py::test_edge_case_none
============================== 1 failed in 0.08s ===============================
"""