
from pymonet.either import Either, Left, Right

def test_edge_cases():
    # Test with None value
    none_value = Either(Left(None))
    assert isinstance(none_value, Left)

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

pyMonet/Test4DT_tests/test_pymonet_either_Either_to_box_0_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        # Test with None value
        none_value = Either(Left(None))
>       assert isinstance(none_value, Left)
E       assert False
E        +  where False = isinstance(<pymonet.either.Either object at 0x7fd4b8024110>, Left)

pyMonet/Test4DT_tests/test_pymonet_either_Either_to_box_0_test_edge_cases.py:7: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_either_Either_to_box_0_test_edge_cases.py::test_edge_cases
============================== 1 failed in 0.07s ===============================
"""