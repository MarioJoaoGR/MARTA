
import pytest
from flutes.multiproc import ProgressBarManager

@pytest.fixture
def progress_bar_manager():
    return ProgressBarManager(verbose=True)

def test_edge_case(progress_bar_manager):
    manager = progress_bar_manager
    assert isinstance(manager._proxy, ProgressBarManager.Proxy)
