
import pytest
from flutes.multiproc import ProgressBarManager

@pytest.fixture
def progress_bar_manager():
    manager = ProgressBarManager()
    return manager

def test_valid_inputs(progress_bar_manager):
    # Test the new method with valid inputs
    iterable = list(range(100))
    bar = progress_bar_manager.new(iterable=iterable, total=len(iterable), desc="Test Progress Bar")
    assert isinstance(bar, type(iterable)), "Expected a tqdm instance or the iterable itself"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___enter___1_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

progress_bar_manager = <flutes.multiproc.ProgressBarManager object at 0x7f18d00b8210>

    def test_valid_inputs(progress_bar_manager):
        # Test the new method with valid inputs
        iterable = list(range(100))
>       bar = progress_bar_manager.new(iterable=iterable, total=len(iterable), desc="Test Progress Bar")
E       AttributeError: 'ProgressBarManager' object has no attribute 'new'

flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___enter___1_test_valid_inputs.py:13: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___enter___1_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.15s ===============================
"""