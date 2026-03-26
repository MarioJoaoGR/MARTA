
import pytest
from flutes.multiproc import ProgressBarManager

@pytest.fixture
def progress_bar_manager():
    manager = ProgressBarManager()
    yield manager
    # Ensure the progress bar is closed after the test
    for worker_id in list(manager.progress_bars.keys()):
        manager._close_bar(worker_id)

def test_close_bar(progress_bar_manager):
    worker_id = 1
    # Create a mock progress bar for testing
    progress_bar_manager._proxy.new = lambda iterable, update_frequency=1, **kwargs: None
    progress_bar_manager._proxy.update = lambda n=0, **kwargs: None
    
    # Add a mock progress bar to the manager
    progress_bar_manager.progress_bars[worker_id] = "mock_tqdm"
    
    # Call the method under test
    progress_bar_manager._close_bar(worker_id)
    
    # Assert that the progress bar is closed and removed from the manager
    assert worker_id not in progress_bar_manager.progress_bars

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

flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager__close_bar_0_test_edge_cases.py FE [100%]

==================================== ERRORS ====================================
_____________________ ERROR at teardown of test_close_bar ______________________

    @pytest.fixture
    def progress_bar_manager():
        manager = ProgressBarManager()
        yield manager
        # Ensure the progress bar is closed after the test
        for worker_id in list(manager.progress_bars.keys()):
>           manager._close_bar(worker_id)

flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager__close_bar_0_test_edge_cases.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <flutes.multiproc.ProgressBarManager object at 0x7f4be2082190>
worker_id = 1

    def _close_bar(self, worker_id: Optional[int]) -> None:
        if worker_id in self.progress_bars:
>           self.progress_bars[worker_id].close()
E           AttributeError: 'str' object has no attribute 'close'

flutes/flutes/multiproc.py:1029: AttributeError
=================================== FAILURES ===================================
________________________________ test_close_bar ________________________________

progress_bar_manager = <flutes.multiproc.ProgressBarManager object at 0x7f4be2082190>

    def test_close_bar(progress_bar_manager):
        worker_id = 1
        # Create a mock progress bar for testing
        progress_bar_manager._proxy.new = lambda iterable, update_frequency=1, **kwargs: None
        progress_bar_manager._proxy.update = lambda n=0, **kwargs: None
    
        # Add a mock progress bar to the manager
        progress_bar_manager.progress_bars[worker_id] = "mock_tqdm"
    
        # Call the method under test
>       progress_bar_manager._close_bar(worker_id)

flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager__close_bar_0_test_edge_cases.py:23: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <flutes.multiproc.ProgressBarManager object at 0x7f4be2082190>
worker_id = 1

    def _close_bar(self, worker_id: Optional[int]) -> None:
        if worker_id in self.progress_bars:
>           self.progress_bars[worker_id].close()
E           AttributeError: 'str' object has no attribute 'close'

flutes/flutes/multiproc.py:1029: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager__close_bar_0_test_edge_cases.py::test_close_bar
ERROR flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager__close_bar_0_test_edge_cases.py::test_close_bar
========================== 1 failed, 1 error in 0.15s ==========================
"""