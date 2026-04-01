
import pytest
from flutes.multiproc import ProgressBarManager

@pytest.fixture
def progress_bar_manager():
    return ProgressBarManager()

def test_close_bar(progress_bar_manager):
    # Create a new bar for a worker
    progress_bar_manager._proxy.new([1, 2, 3], total=3)
    
    # Close the bar associated with a worker
    progress_bar_manager.close_bar(None)

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

flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager__close_bar_0_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
________________________________ test_close_bar ________________________________

progress_bar_manager = <flutes.multiproc.ProgressBarManager object at 0x7efe94125450>

    def test_close_bar(progress_bar_manager):
        # Create a new bar for a worker
        progress_bar_manager._proxy.new([1, 2, 3], total=3)
    
        # Close the bar associated with a worker
>       progress_bar_manager.close_bar(None)
E       AttributeError: 'ProgressBarManager' object has no attribute 'close_bar'

flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager__close_bar_0_test_edge_cases.py:14: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager__close_bar_0_test_edge_cases.py::test_close_bar
============================== 1 failed in 0.13s ===============================


  0%|          | 0/3 [00:00<?, ?it/s]
"""