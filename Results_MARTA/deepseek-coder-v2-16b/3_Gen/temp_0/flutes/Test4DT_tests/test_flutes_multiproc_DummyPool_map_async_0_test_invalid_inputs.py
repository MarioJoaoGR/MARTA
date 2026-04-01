
import pytest
from multiprocessing import Pool
from flutes.multiproc import DummyPool

def test_invalid_inputs():
    with pytest.raises(TypeError):
        # This should raise a TypeError because the initializer function is not callable
        pool = DummyPool(processes=0, initializer="not_a_callable", initargs=())
