
import pytest
from flutes.multiproc import ProgressBarManager

@pytest.fixture(scope="module")
def progress_bar_manager():
    manager = ProgressBarManager()
    yield manager
    # Ensure the progress bar is closed when the test is done
    manager.__exit__(None, None, None)

def test_valid_case(progress_bar_manager):
    assert isinstance(progress_bar_manager._proxy, ProgressBarManager.Proxy)
