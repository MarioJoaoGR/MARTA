
import pytest
from flutes.multiproc import ProgressBarManager

@pytest.fixture
def progress_bar_manager():
    return ProgressBarManager(verbose=True)

def test_progress_bar_manager_creation(progress_bar_manager):
    assert isinstance(progress_bar_manager, ProgressBarManager)
    assert progress_bar_manager.verbose is True

def test_progress_bar_manager_proxy(progress_bar_manager):
    assert hasattr(progress_bar_manager, 'proxy')
    assert isinstance(progress_bar_manager.proxy, ProgressBarManager.Proxy)
