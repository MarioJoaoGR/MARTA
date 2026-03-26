
import pytest
from flutes.multiproc import ProgressBarManager

@pytest.fixture
def progress_bar_manager():
    return ProgressBarManager()

def test_progress_bar_manager(progress_bar_manager):
    assert isinstance(progress_bar_manager, ProgressBarManager)
