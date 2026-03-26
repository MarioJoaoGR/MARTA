
import pytest
from multiprocessing import Pool as MPPool
from flutes.multiproc import DummyPool

# Test default initialization
def test_default_initialization():
    pool = DummyPool(processes=0)
    assert isinstance(pool, DummyPool)
    assert pool._process_state is None
    assert pool._state == MPPool()._state  # Assuming _state is a class attribute representing the state

# Test initialization with custom initializer function and arguments
def test_initializer_function():
    def initializer_func(arg):
        print(f"Initializing with arg: {arg}")
    
    pool = DummyPool(processes=0, initializer=initializer_func, initargs=(42,))
    assert isinstance(pool, DummyPool)