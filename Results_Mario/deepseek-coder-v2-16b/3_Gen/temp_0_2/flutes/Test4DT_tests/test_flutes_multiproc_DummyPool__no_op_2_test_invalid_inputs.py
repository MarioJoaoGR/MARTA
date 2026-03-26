
import pytest
from multiprocessing import Pool
from flutes.multiproc import DummyPool

def test_invalid_inputs():
    with pytest.raises(TypeError):
        # Test invalid initializer type (should raise TypeError)
        pool = DummyPool(processes=0, initializer="not a callable", initargs=(1, "arg2"))
