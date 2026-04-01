
import pytest
from flutes.multiproc import ProgressBarManager

def test_invalid_inputs():
    with pytest.raises(ValueError):
        # Test invalid update frequency for new method
        manager = ProgressBarManager()
        with pytest.raises(ValueError):
            manager.proxy.new([1, 2, 3], update_frequency=0)

        # Test invalid total in kwargs for new method
        with pytest.raises(ValueError):
            manager.proxy.new([1, 2, 3], total=0)

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

flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager_close_0_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        with pytest.raises(ValueError):
            # Test invalid update frequency for new method
            manager = ProgressBarManager()
            with pytest.raises(ValueError):
                manager.proxy.new([1, 2, 3], update_frequency=0)
    
            # Test invalid total in kwargs for new method
>           with pytest.raises(ValueError):
E           Failed: DID NOT RAISE <class 'ValueError'>

flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager_close_0_test_invalid_inputs.py:13: Failed
=============================== warnings summary ===============================
Test4DT_tests/test_flutes_multiproc_ProgressBarManager_close_0_test_invalid_inputs.py::test_invalid_inputs
  /projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py:910: UserWarning: Iterable has length 3 but total=0 is specified
    warnings.warn(f"Iterable has length {iter_len} but total={length} is specified")

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager_close_0_test_invalid_inputs.py::test_invalid_inputs
========================= 1 failed, 1 warning in 0.13s =========================


0it [00:00, ?it/s]
"""