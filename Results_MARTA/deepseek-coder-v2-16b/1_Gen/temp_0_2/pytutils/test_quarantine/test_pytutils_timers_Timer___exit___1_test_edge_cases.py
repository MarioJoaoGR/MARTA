
import pytest
from pytutils.timers import Timer
import time

@pytest.mark.parametrize("verbose", [None, False])
def test_edge_cases(verbose):
    with pytest.raises(AttributeError):
        # Since `start` is not defined in the initial implementation, accessing it will raise an AttributeError
        with Timer(name='test', verbose=verbose) as t:
            pass  # This should trigger the __exit__ method without defining a start time

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

pytutils/Test4DT_tests/test_pytutils_timers_Timer___exit___1_test_edge_cases.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
____________________________ test_edge_cases[None] _____________________________

verbose = None

    @pytest.mark.parametrize("verbose", [None, False])
    def test_edge_cases(verbose):
>       with pytest.raises(AttributeError):
E       Failed: DID NOT RAISE <class 'AttributeError'>

pytutils/Test4DT_tests/test_pytutils_timers_Timer___exit___1_test_edge_cases.py:8: Failed
____________________________ test_edge_cases[False] ____________________________

verbose = False

    @pytest.mark.parametrize("verbose", [None, False])
    def test_edge_cases(verbose):
>       with pytest.raises(AttributeError):
E       Failed: DID NOT RAISE <class 'AttributeError'>

pytutils/Test4DT_tests/test_pytutils_timers_Timer___exit___1_test_edge_cases.py:8: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_timers_Timer___exit___1_test_edge_cases.py::test_edge_cases[None]
FAILED pytutils/Test4DT_tests/test_pytutils_timers_Timer___exit___1_test_edge_cases.py::test_edge_cases[False]
============================== 2 failed in 0.05s ===============================
"""