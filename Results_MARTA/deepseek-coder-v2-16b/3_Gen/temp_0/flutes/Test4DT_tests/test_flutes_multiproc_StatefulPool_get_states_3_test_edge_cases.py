
import pytest
from multiprocessing import Pool
from flutes.multiproc import StatefulPool, State

def test_edge_cases():
    with pytest.raises(TypeError):
        # Test initializing with None inputs
        StatefulPool(None, None, (None,), (), {})
