
import pytest
from flutes.multiproc import DummyPool  # Adjust the import to match the actual module path

def test_edge_cases():
    pool = DummyPool(processes=0)  # Create an instance of DummyPool with processes set to 0
    
    # Define a simple function for testing
    def multiply(a, b):
        return a * b
    
    # Prepare data for starmap test
    data = [(2, 3), (4, 5)]
    
    # Use the starmap method of DummyPool to apply the function across the iterable
    results = pool.starmap(multiply, data)
    
    # Assert that the results are as expected
    assert results == [6, 20]
