
import pytest
from multiprocessing import Pool
import flutes.multiproc

# Test creating a DummyPool instance with zero processes and no initializer function
def test_dummy_pool_creation():
    pool = flutes.multiproc.DummyPool(processes=0)
    assert isinstance(pool, flutes.multiproc.DummyPool)

# Test applying a function using the pool
def my_function(x):
    return x * 2

@pytest.fixture
def setup():
    return flutes.multiproc.DummyPool(processes=0)

def test_apply(setup):
    pool = setup
    result = pool.apply(my_function, args=(5,))
    assert result == 10

# Test applying a function asynchronously
def test_apply_async(setup):
    pool = setup
    result = pool.apply_async(lambda x: x * 2, args=(5,))
    assert result.get() == 10

# Test using the pool with an initializer function
def initializer_func():
    print("Initializing worker")

def test_initializer_function():
    pool = flutes.multiproc.DummyPool(processes=0, initializer=initializer_func)

# New test case to cover line 103 in the apply method
def test_apply_with_process_state(setup):
    pool = setup
    pool._process_state = "some_state"
    result = pool.apply(my_function, args=(5,))
    assert result == 10
    # Also check that the local variable __state__ is set correctly