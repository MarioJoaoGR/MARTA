
import pytest
from flutes.multiproc import ProgressBarManager

@pytest.mark.parametrize("verbose", [True, False])
def test_ProgressBarManager_init(verbose):
    manager = ProgressBarManager(verbose=verbose)
    
    if verbose:
        assert isinstance(manager._proxy, ProgressBarManager.Proxy)
    else:
        assert isinstance(manager._proxy, ProgressBarManager._DummyProxy)
