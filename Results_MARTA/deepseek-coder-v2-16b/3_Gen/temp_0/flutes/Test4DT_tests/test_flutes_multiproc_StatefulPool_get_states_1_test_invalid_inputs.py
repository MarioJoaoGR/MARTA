
import pytest
from multiprocessing import Pool
from flutes.multiproc import StatefulPool, State

def test_invalid_inputs():
    with pytest.raises(TypeError):
        # Invalid pool class provided (should be a subclass of multiprocessing.pool.Pool)
        StatefulPool(int, State, (), (), {})
