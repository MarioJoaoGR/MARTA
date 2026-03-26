
import pytest
from flutes.multiproc import ProgressBarManager

def test_invalid_inputs():
    manager = ProgressBarManager()
    
    # Test invalid update frequency for new method
    with pytest.raises(ValueError):
        manager.proxy.new([1, 2, 3], update_frequency=-5)
