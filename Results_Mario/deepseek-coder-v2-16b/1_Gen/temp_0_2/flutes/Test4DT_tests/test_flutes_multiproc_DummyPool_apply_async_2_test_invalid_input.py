
import pytest
from multiprocessing import Pool
from flutes.multiproc import DummyPool

def test_invalid_input():
    with pytest.raises(TypeError):
        # Passing a non-callable initializer should raise a TypeError
        pool = DummyPool(processes=0, initializer="not_a_callable", initargs=())
