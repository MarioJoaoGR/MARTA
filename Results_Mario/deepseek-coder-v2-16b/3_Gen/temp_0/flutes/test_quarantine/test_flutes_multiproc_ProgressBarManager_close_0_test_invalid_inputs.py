
import pytest
from flutes.multiproc import ProgressBarManager

@pytest.fixture
def progress_bar_manager():
    manager = ProgressBarManager(verbose=True)
    yield manager
    # Ensure the progress bar is closed after the test
    manager.close()

def test_update_progress_bar(progress_bar_manager):
    xs = list(range(100))
    bar = progress_bar_manager._proxy.new(total=len(xs), desc="Test Bar")
    assert isinstance(bar, ProgressBarManager.Proxy)

    # Update the progress bar manually to ensure it updates correctly
    for i in range(len(xs)):
        if (i + 1) % 10 == 0:  # Update every 10 iterations
            bar.update(1, postfix={"sum": sum(xs[:i+1])})

    assert len(progress_bar_manager.progress_bars) > 0

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager_close_0_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
___________________________ test_update_progress_bar ___________________________

progress_bar_manager = <flutes.multiproc.ProgressBarManager object at 0x7f39c8eed710>

    def test_update_progress_bar(progress_bar_manager):
        xs = list(range(100))
        bar = progress_bar_manager._proxy.new(total=len(xs), desc="Test Bar")
        assert isinstance(bar, ProgressBarManager.Proxy)
    
        # Update the progress bar manually to ensure it updates correctly
        for i in range(len(xs)):
            if (i + 1) % 10 == 0:  # Update every 10 iterations
                bar.update(1, postfix={"sum": sum(xs[:i+1])})
    
>       assert len(progress_bar_manager.progress_bars) > 0
E       assert 0 > 0
E        +  where 0 = len({})
E        +    where {} = <flutes.multiproc.ProgressBarManager object at 0x7f39c8eed710>.progress_bars

flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager_close_0_test_invalid_inputs.py:22: AssertionError
--------------------------- Captured stderr teardown ---------------------------

                                                 
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager_close_0_test_invalid_inputs.py::test_update_progress_bar
============================== 1 failed in 0.14s ===============================


Test Bar:   0%|          | 0/100 [00:00<?, ?it/s]
"""