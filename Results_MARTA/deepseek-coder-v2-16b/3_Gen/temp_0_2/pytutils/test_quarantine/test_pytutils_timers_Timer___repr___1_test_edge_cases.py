
from pytutils.timers import Timer
import pytest

def test_edge_cases():
    # Test with None for name and False for verbose
    timer = Timer(None, False)
    
    assert repr(timer) == 'Timer(None)'
    
    # Ensure that the context manager does not raise an error when used correctly
    with pytest.raises(TypeError):  # Since __init__ expects a str or None for name and a bool for verbose
        pass

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

pytutils/Test4DT_tests/test_pytutils_timers_Timer___repr___1_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        # Test with None for name and False for verbose
        timer = Timer(None, False)
    
        assert repr(timer) == 'Timer(None)'
    
        # Ensure that the context manager does not raise an error when used correctly
>       with pytest.raises(TypeError):  # Since __init__ expects a str or None for name and a bool for verbose
E       Failed: DID NOT RAISE <class 'TypeError'>

pytutils/Test4DT_tests/test_pytutils_timers_Timer___repr___1_test_edge_cases.py:12: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_timers_Timer___repr___1_test_edge_cases.py::test_edge_cases
============================== 1 failed in 0.05s ===============================
"""