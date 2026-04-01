
import pytest
from flutes.multiproc import ProgressBarManager

@pytest.fixture(scope="module")
def progress_bar_manager():
    manager = ProgressBarManager()
    yield manager
    # Ensure all bars are closed after the test
    for bar in manager.progress_bars.values():
        bar.close()

def test_close_bar_1(progress_bar_manager):
    # Create a mock progress bar to simulate having a progress bar
    class MockProgressBar:
        def close(self):
            pass

    # Add the mock progress bar to the manager's progress bars dictionary
    worker_id = 1
    progress_bar_manager.progress_bars[worker_id] = MockProgressBar()

    # Call the _close_bar method with the worker ID
    progress_bar_manager._close_bar(worker_id)

    # Assert that the progress bar is closed and removed from the dictionary
    assert worker_id not in progress_bar_manager.progress_bars
