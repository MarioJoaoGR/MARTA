# Module: flutes.multiproc
import pytest
from multiprocessing import Pool

# Import the DummyPool class from its module
from flutes.multiproc import DummyPool

def test_dummy_pool_creation():
    pool = DummyPool(processes=0)
    assert isinstance(pool, DummyPool), "Expected a DummyPool instance"

def test_initializer_function():
    def initializer_func(arg):
        print(f"Initializing with arg: {arg}")
    
    pool = DummyPool(processes=0, initializer=initializer_func, initargs=(42,))
    assert hasattr(pool, '_process_state'), "Expected _process_state to be set by the initializer function"

def test_apply_function():
    def square(x):
        return x * x
    
    pool = DummyPool(processes=0)
    result = pool.apply(square, (2,))
    assert result == 4, "Expected the square of 2 to be 4"

def test_map_function():
    def square(x):
        return x * x
    
    pool = DummyPool(processes=0)
    results = pool.map(square, range(5))
    assert results == [0, 1, 4, 9, 16], "Expected the map function to apply square to each element"

def test_imap_function():
    def square(x):
        return x * x
    
    pool = DummyPool(processes=0)
    results = list(pool.imap(square, range(5)))
    assert all(isinstance(r, int) for r in results), "Expected the imap function to return integers"

def test_starmap_function():
    pool = DummyPool(processes=0)
    results = pool.starmap(lambda x, y: x * y, [(1, 2), (3, 4)])
    assert results == [2, 12], "Expected the starmap function to apply the lambda to each tuple"

def test_apply_async_function():
    def square(x):
        return x * x
    
    pool = DummyPool(processes=0)
    result = pool.apply_async(square, (3,), callback=lambda x: print(f"Callback result: {x}"))
    result.wait()  # Wait for the result to be ready
    assert True, "Expected apply_async to execute without errors"

def test_imap_unordered_function():
    def square(x):
        return x * x
    
    pool = DummyPool(processes=0)
    results = list(pool.imap_unordered(square, range(5)))
    assert len(results) == 5, "Expected the imap_unordered function to return a list of results"

if __name__ == "__main__":
    pytest.main()
