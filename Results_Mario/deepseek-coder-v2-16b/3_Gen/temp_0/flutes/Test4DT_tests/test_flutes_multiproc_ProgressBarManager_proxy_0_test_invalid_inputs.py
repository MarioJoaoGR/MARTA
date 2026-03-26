
import pytest
from flutes.multiproc import ProgressBarManager

@pytest.fixture(scope="module")
def progress_bar_manager():
    return ProgressBarManager()

def test_invalid_inputs(progress_bar_manager):
    with pytest.raises(TypeError):
        # Test invalid input: passing a non-iterable object to new method
        progress_bar_manager.proxy().new("not an iterable")
