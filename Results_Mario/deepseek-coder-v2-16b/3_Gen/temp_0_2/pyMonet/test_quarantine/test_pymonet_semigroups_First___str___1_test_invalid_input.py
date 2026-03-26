
import pytest
from pymonet.semigroups import First

def test_invalid_input():
    # Test that an exception is raised when trying to create a First instance with an invalid type
    with pytest.raises(TypeError):
        First("invalid")  # This should raise a TypeError because "invalid" is not a valid type for the value attribute

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

pyMonet/Test4DT_tests/test_pymonet_semigroups_First___str___1_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        # Test that an exception is raised when trying to create a First instance with an invalid type
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

pyMonet/Test4DT_tests/test_pymonet_semigroups_First___str___1_test_invalid_input.py:7: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_semigroups_First___str___1_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.08s ===============================
"""