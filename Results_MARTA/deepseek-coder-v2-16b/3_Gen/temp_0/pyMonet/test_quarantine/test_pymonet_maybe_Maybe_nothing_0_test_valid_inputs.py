
import pytest
from pymonet.maybe import Maybe

def test_valid_inputs():
    # Test creating a Maybe with a valid value and is_nothing set to False
    maybe = Maybe(value=42, is_nothing=False)
    assert not maybe.is_nothing
    assert maybe.value == 42
    
    # Test creating a Maybe with a valid value and is_nothing set to True
    another_maybe = Maybe(value="Hello", is_nothing=True)
    assert another_maybe.is_nothing
    assert another_maybe.value is None

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

pyMonet/Test4DT_tests/test_pymonet_maybe_Maybe_nothing_0_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        # Test creating a Maybe with a valid value and is_nothing set to False
        maybe = Maybe(value=42, is_nothing=False)
        assert not maybe.is_nothing
        assert maybe.value == 42
    
        # Test creating a Maybe with a valid value and is_nothing set to True
        another_maybe = Maybe(value="Hello", is_nothing=True)
        assert another_maybe.is_nothing
>       assert another_maybe.value is None
E       AttributeError: 'Maybe' object has no attribute 'value'

pyMonet/Test4DT_tests/test_pymonet_maybe_Maybe_nothing_0_test_valid_inputs.py:14: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_maybe_Maybe_nothing_0_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.07s ===============================
"""