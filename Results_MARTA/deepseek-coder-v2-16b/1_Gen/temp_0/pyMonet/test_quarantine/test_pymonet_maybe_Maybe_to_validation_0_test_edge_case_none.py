
import pytest
from pymonet.maybe import Maybe
from pymonet.validation import Validation

def test_edge_case_none():
    maybe = Maybe(value=None, is_nothing=False)
    validation_result = maybe.to_validation()
    assert isinstance(validation_result, Validation)
    assert validation_result.success() is None

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

pyMonet/Test4DT_tests/test_pymonet_maybe_Maybe_to_validation_0_test_edge_case_none.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_edge_case_none ______________________________

    def test_edge_case_none():
        maybe = Maybe(value=None, is_nothing=False)
        validation_result = maybe.to_validation()
        assert isinstance(validation_result, Validation)
>       assert validation_result.success() is None
E       assert <pymonet.validation.Validation object at 0x7fb918f38f50> is None
E        +  where <pymonet.validation.Validation object at 0x7fb918f38f50> = success()
E        +    where success = <pymonet.validation.Validation object at 0x7fb9190a17d0>.success

pyMonet/Test4DT_tests/test_pymonet_maybe_Maybe_to_validation_0_test_edge_case_none.py:10: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_maybe_Maybe_to_validation_0_test_edge_case_none.py::test_edge_case_none
============================== 1 failed in 0.07s ===============================
"""