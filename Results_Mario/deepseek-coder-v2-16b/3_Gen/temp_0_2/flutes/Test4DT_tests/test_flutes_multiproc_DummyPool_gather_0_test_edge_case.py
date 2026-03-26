
import pytest
from flutes.multiproc import DummyPool

def test_dummy_pool_single_threaded():
    # Mock the multiprocessing module to use a single-threaded execution
    with pytest.MonkeyPatch.context() as mp:
        mp.pool = type('mpool', (), {})  # Create a mock for the pool module
        mp.pool.RUN = 1  # Define a constant for the state
        
        def initializer_func():
            pass
        
        pool = DummyPool(processes=0, initializer=initializer_func)
        
        # Mock the task function to yield results from an iterable
        def task_fn(x):
            return [x]
        
        tasks = [1, 2, 3]
        results = list(pool.gather(task_fn, tasks))
        
        assert len(results) == len(tasks)
        for i in range(len(tasks)):
            assert results[i] == tasks[i]
