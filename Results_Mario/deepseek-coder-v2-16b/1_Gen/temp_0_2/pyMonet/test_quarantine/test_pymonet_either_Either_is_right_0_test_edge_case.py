
from pymonet.either import Either, Right, Left

def test_edge_case():
    # Setup
    either_none = Either(None)
    
    # Test
    assert either_none.is_right() == False

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

pyMonet/Test4DT_tests/test_pymonet_either_Either_is_right_0_test_edge_case.py F [100%]

=================================== FAILURES ===================================
________________________________ test_edge_case ________________________________

    def test_edge_case():
        # Setup
        either_none = Either(None)
    
        # Test
>       assert either_none.is_right() == False
E       assert None == False
E        +  where None = is_right()
E        +    where is_right = <pymonet.either.Either object at 0x7fdefc1c46d0>.is_right

pyMonet/Test4DT_tests/test_pymonet_either_Either_is_right_0_test_edge_case.py:9: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_either_Either_is_right_0_test_edge_case.py::test_edge_case
============================== 1 failed in 0.06s ===============================
"""