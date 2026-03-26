
import pytest
from flutes.multiproc import ProgressBarManager

@pytest.fixture(scope="module")
def progress_bar_manager():
    return ProgressBarManager()

def test_valid_case(progress_bar_manager):
    assert isinstance(progress_bar_manager, ProgressBarManager)
