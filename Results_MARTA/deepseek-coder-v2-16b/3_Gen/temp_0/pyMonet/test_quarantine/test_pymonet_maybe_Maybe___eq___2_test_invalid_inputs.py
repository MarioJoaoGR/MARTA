
import pytest
from pymonet.maybe import Maybe

def test_invalid_inputs():
    # Test comparing with non-Maybe object
    try_compare_with_non_maybe = Maybe(10, False)
    with pytest.raises(TypeError):  # Assuming the error is a TypeError if other is not Maybe
        assert try_compare_with_non_maybe == "not a Maybe object"

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

pyMonet/Test4DT_tests/test_pymonet_maybe_Maybe___eq___2_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        # Test comparing with non-Maybe object
        try_compare_with_non_maybe = Maybe(10, False)
        with pytest.raises(TypeError):  # Assuming the error is a TypeError if other is not Maybe
>           assert try_compare_with_non_maybe == "not a Maybe object"
E           AssertionError: assert <pymonet.maybe.Maybe object at 0x7f389cddef90> == 'not a Maybe object'

pyMonet/Test4DT_tests/test_pymonet_maybe_Maybe___eq___2_test_invalid_inputs.py:9: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_maybe_Maybe___eq___2_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.07s ===============================
"""