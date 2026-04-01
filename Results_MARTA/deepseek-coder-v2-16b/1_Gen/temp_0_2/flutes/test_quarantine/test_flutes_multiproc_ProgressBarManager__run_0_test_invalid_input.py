
import pytest
from flutes.multiproc import ProgressBarManager

def test_invalid_input():
    manager = ProgressBarManager(verbose=False)
    
    # Test with invalid update frequency (not a float or int)
    with pytest.raises(ValueError):
        manager._proxy.new(iterable=[1, 2, 3], update_frequency="invalid")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager__run_0_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        manager = ProgressBarManager(verbose=False)
    
        # Test with invalid update frequency (not a float or int)
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager__run_0_test_invalid_input.py:9: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager__run_0_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.10s ===============================
"""