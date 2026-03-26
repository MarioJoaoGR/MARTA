
import pytest
from flutes.multiproc import ProgressBarManager

def test_invalid_inputs():
    manager = ProgressBarManager(verbose=True)
    
    # Test invalid iterable type
    with pytest.raises(ValueError):
        manager._proxy.new("not an iterable")  # This should raise a ValueError

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

flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager_proxy_0_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        manager = ProgressBarManager(verbose=True)
    
        # Test invalid iterable type
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager_proxy_0_test_invalid_inputs.py:9: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager_proxy_0_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.13s ===============================


  0%|          | 0/15 [00:00<?, ?it/s]
"""