
import pytest
from flutes.multiproc import ProgressBarManager

@pytest.fixture(scope="module")
def progress_bar_manager():
    return ProgressBarManager()

def test_invalid_inputs(progress_bar_manager):
    with pytest.raises(TypeError):
        # Test that passing a non-iterable raises a TypeError
        progress_bar_manager._proxy.new(None)  # Passing None as iterable should raise TypeError

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

progress_bar_manager = <flutes.multiproc.ProgressBarManager object at 0x7f5c81c6e390>

    def test_invalid_inputs(progress_bar_manager):
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager_close_0_test_invalid_inputs.py:10: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager_close_0_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.14s ===============================


0it [00:00, ?it/s]
"""