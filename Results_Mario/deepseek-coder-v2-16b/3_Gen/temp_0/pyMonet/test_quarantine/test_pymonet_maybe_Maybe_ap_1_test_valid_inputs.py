
import pytest
from pymonet.maybe import Maybe

def test_valid_inputs():
    # Test case 1: Applying a function to a non-empty Maybe
    maybe_some = Maybe(value=lambda x: x + 1, is_nothing=False)
    result = maybe_some.ap(Maybe(value=5, is_nothing=False))
    assert not result.is_nothing
    assert result.value == 6
    
    # Test case 2: Applying a function to an empty Maybe
    maybe_empty = Maybe(value=lambda x: x + 1, is_nothing=True)
    result = maybe_empty.ap(Maybe(value=5, is_nothing=False))
    assert result.is_nothing
    
    # Test case 3: Applying a function to another Maybe with an empty Maybe
    maybe_some = Maybe(value=lambda x: x + 1, is_nothing=False)
    result = maybe_some.ap(Maybe(value=None, is_nothing=True))
    assert not result.is_nothing

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

pyMonet/Test4DT_tests/test_pymonet_maybe_Maybe_ap_1_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        # Test case 1: Applying a function to a non-empty Maybe
        maybe_some = Maybe(value=lambda x: x + 1, is_nothing=False)
        result = maybe_some.ap(Maybe(value=5, is_nothing=False))
        assert not result.is_nothing
        assert result.value == 6
    
        # Test case 2: Applying a function to an empty Maybe
        maybe_empty = Maybe(value=lambda x: x + 1, is_nothing=True)
        result = maybe_empty.ap(Maybe(value=5, is_nothing=False))
        assert result.is_nothing
    
        # Test case 3: Applying a function to another Maybe with an empty Maybe
        maybe_some = Maybe(value=lambda x: x + 1, is_nothing=False)
        result = maybe_some.ap(Maybe(value=None, is_nothing=True))
>       assert not result.is_nothing
E       assert not True
E        +  where True = <pymonet.maybe.Maybe object at 0x7fe8420bfb90>.is_nothing

pyMonet/Test4DT_tests/test_pymonet_maybe_Maybe_ap_1_test_valid_inputs.py:20: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_maybe_Maybe_ap_1_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.08s ===============================
"""