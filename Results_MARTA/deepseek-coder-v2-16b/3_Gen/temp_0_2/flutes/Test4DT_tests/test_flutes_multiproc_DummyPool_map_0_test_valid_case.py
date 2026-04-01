
import pytest
from multiprocessing import Pool, TimeoutError
from flutes.multiproc import DummyPool

def test_valid_case():
    # Create a DummyPool instance with 4 worker processes, no initializer, no initargs, maxtasksperchild set to 5, and context set to {'key': 'value'}
    pool = DummyPool(processes=4, initializer=lambda x: None, initargs=(1,), maxtasksperchild=5, context={'key': 'value'})
    
    # Define a function to be mapped over an iterable
    def square(x):
        return x * x
    
    # Create an iterable of numbers to map the function over
    numbers = [1, 2, 3, 4]
    
    # Map the square function over the numbers using the pool
    results = list(pool.map(square, numbers))
    
    # Assert that the results are as expected
    assert results == [1, 4, 9, 16]
