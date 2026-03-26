
import pytest
from flutes.multiproc import ProgressBarManager

@pytest.fixture
def progress_bar_manager():
    return ProgressBarManager()

def test_progress_bar_manager_creation(progress_bar_manager):
    assert isinstance(progress_bar_manager, ProgressBarManager)

def test_proxy_methods(progress_bar_manager):
    proxy = progress_bar_manager.proxy
    assert callable(proxy.new)
    assert callable(proxy.update)
    assert callable(proxy.write)
    assert callable(proxy.close)
