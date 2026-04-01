
from pymonet.maybe import Maybe

def test_valid_input():
    maybe1 = Maybe(value=42, is_nothing=False)
    maybe2 = Maybe(value='hello', is_nothing=True)
    
    assert not maybe1.is_nothing
    assert maybe1.value == 42
    assert maybe2.is_nothing
    assert maybe2.value is None

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

pyMonet/Test4DT_tests/test_pymonet_maybe_Maybe___eq___0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        maybe1 = Maybe(value=42, is_nothing=False)
        maybe2 = Maybe(value='hello', is_nothing=True)
    
        assert not maybe1.is_nothing
        assert maybe1.value == 42
        assert maybe2.is_nothing
>       assert maybe2.value is None
E       AttributeError: 'Maybe' object has no attribute 'value'

pyMonet/Test4DT_tests/test_pymonet_maybe_Maybe___eq___0_test_valid_input.py:11: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_maybe_Maybe___eq___0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.07s ===============================
"""