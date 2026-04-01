
import pytest
from pytutils.timers import Timer

def test_invalid_inputs():
    with pytest.raises(TypeError):
        Timer()  # This should raise a TypeError because __init__ does not accept positional arguments without default values

    with pytest.raises(TypeError):
        Timer(name=123)  # This should raise a TypeError because name expects a string and is passed an integer

    with pytest.raises(TypeError):
        Timer(verbose="true")  # This should raise a TypeError because verbose expects a boolean and is passed a string

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

pytutils/Test4DT_tests/test_pytutils_timers_Timer___repr___1_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

pytutils/Test4DT_tests/test_pytutils_timers_Timer___repr___1_test_invalid_inputs.py:6: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_timers_Timer___repr___1_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.05s ===============================
"""