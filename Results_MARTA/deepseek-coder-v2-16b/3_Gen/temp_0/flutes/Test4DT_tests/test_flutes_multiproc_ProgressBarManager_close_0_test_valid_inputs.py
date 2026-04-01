
import pytest
from flutes.multiproc import ProgressBarManager

@pytest.fixture(scope="module")
def progress_bar_manager():
    manager = ProgressBarManager()
    yield manager
    manager.close()

def test_progress_bar_creation(progress_bar_manager):
    assert isinstance(progress_bar_manager._proxy, ProgressBarManager.Proxy)

def test_update_progress_bar(progress_bar_manager):
    xs = list(range(100))
    bar = progress_bar_manager._proxy.new(total=len(xs), desc="Test Bar")
    assert isinstance(bar, ProgressBarManager.Proxy)
    
    # Update the progress bar manually to ensure it updates correctly
    for i in range(len(xs)):
        if i % 10 == 0:  # Update every 10 iterations
            bar.update(i + 1)
    
    assert len(progress_bar_manager.progress_bars) > 0
