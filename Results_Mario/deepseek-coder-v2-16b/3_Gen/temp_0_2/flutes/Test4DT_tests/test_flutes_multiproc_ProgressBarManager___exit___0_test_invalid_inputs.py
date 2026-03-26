
import pytest
from flutes.multiproc import ProgressBarManager

def test_invalid_inputs():
    with pytest.raises(ValueError):
        # Test case 1: Invalid update frequency (should raise ValueError)
        manager = ProgressBarManager(verbose=True)
        manager.proxy.new(iterable=[1, 2, 3], update_frequency=-1)
        
        # Test case 2: Iterable without length and no total specified (should raise ValueError)
        manager = ProgressBarManager(verbose=True)
        manager.proxy.new(iterable=[1, 2, 3])
        
        # Test case 3: Invalid update frequency type (should raise TypeError)
        manager = ProgressBarManager(verbose=True)
        with pytest.raises(TypeError):
            manager.proxy.new(iterable=[1, 2, 3], update_frequency="invalid")
        
        # Test case 4: Invalid total specified without iterable (should raise ValueError)
        manager = ProgressBarManager(verbose=True)
        with pytest.raises(ValueError):
            manager.proxy.new(total=100)
