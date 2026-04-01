
import pytest
from pymonet.maybe import Maybe

def test_invalid_input():
    # Test invalid input where is_nothing is not a boolean
    with pytest.raises(TypeError):
        Maybe(value=42, is_nothing="not a bool")

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

pyMonet/Test4DT_tests/test_pymonet_maybe_Maybe_to_try_2_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        # Test invalid input where is_nothing is not a boolean
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

pyMonet/Test4DT_tests/test_pymonet_maybe_Maybe_to_try_2_test_invalid_input.py:7: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_maybe_Maybe_to_try_2_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.07s ===============================
"""