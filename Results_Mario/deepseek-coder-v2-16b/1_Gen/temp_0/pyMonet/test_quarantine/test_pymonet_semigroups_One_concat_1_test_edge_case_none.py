
from pymonet.semigroups import One

def test_edge_case_none():
    # Test when both values are None
    one1 = One(None)
    one2 = One(None)
    combined = one1.concat(one2)
    assert combined.value is False, "Expected value to be False when both inputs are None"

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

pyMonet/Test4DT_tests/test_pymonet_semigroups_One_concat_1_test_edge_case_none.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_edge_case_none ______________________________

    def test_edge_case_none():
        # Test when both values are None
        one1 = One(None)
        one2 = One(None)
        combined = one1.concat(one2)
>       assert combined.value is False, "Expected value to be False when both inputs are None"
E       AssertionError: Expected value to be False when both inputs are None
E       assert None is False
E        +  where None = <pymonet.semigroups.One object at 0x7f412fac0450>.value

pyMonet/Test4DT_tests/test_pymonet_semigroups_One_concat_1_test_edge_case_none.py:9: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_semigroups_One_concat_1_test_edge_case_none.py::test_edge_case_none
============================== 1 failed in 0.07s ===============================
"""