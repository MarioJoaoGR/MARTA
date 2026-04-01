
import pytest
from multiprocessing import Pool
from flutes.multiproc import DummyPool

def test_invalid_inputs():
    with pytest.raises(TypeError):
        # Test initializing with invalid types for processes, initializer, and initargs
        DummyPool(processes="string", initializer=lambda: None, initargs=(1, 2))
