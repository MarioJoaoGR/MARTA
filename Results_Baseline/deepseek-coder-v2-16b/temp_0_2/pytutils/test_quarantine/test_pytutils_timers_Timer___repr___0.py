
import pytest
from pytutils.timers import Timer
import time

@pytest.fixture
def timer():
    return Timer('test_operation', verbose=True)

def test_timer_with_name_and_verbose(capsys):
    with Timer('test_operation', verbose=True) as t:
        time.sleep(1)  # Simulate a long operation taking approximately 1 second
    out, err = capsys.readouterr()
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

pytutils/Test4DT_tests/test_pytutils_timers_Timer___repr___0.py F        [100%]

=================================== FAILURES ===================================
_______________________ test_timer_with_name_and_verbose _______________________

capsys = <_pytest.capture.CaptureFixture object at 0x7f6ea436bad0>

    def test_timer_with_name_and_verbose(capsys):
        with Timer('test_operation', verbose=True) as t:
            time.sleep(1)  # Simulate a long operation taking approximately 1 second
        out, err = capsys.readouterr()
>       assert 'Elapsed time for \'test_operation\':' in out
E       assert "Elapsed time for 'test_operation':" in ''

pytutils/Test4DT_tests/test_pytutils_timers_Timer___repr___0.py:14: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_timers_Timer___repr___0.py::test_timer_with_name_and_verbose
============================== 1 failed in 1.06s ===============================
"""