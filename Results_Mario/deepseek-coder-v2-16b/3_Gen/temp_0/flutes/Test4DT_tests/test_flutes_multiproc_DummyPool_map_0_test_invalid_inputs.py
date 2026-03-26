
import pytest
from multiprocessing import Pool, TimeoutError
from flutes.multiproc import DummyPool

def test_invalid_inputs():
    with pytest.raises(TypeError):
        # Test invalid initializer type
        pool = DummyPool(processes=0, initializer="not a callable")
