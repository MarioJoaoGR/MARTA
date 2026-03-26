
import pytest
from pathlib import Path
import os
import pickle
import functools
from typing import Optional, Callable
from flutes.fs import cache

# Mocking necessary modules or functions if required for testing
class MockPath:
    def __init__(self, exists=True):
        self.exists = exists

os.path.exists = lambda path: getattr(MockPath(), 'exists', False)

@pytest.fixture
def mock_cache():
    @cache("my_cache.pkl", verbose=True)
    def expensive_function(x):
        return x * 2
    return expensive_function, "my_cache.pkl"

def test_valid_inputs(mock_cache):
    func, path = mock_cache
    # First call should execute the function and cache the result
    assert func(5) == 10
    
    # Second call should load from cache without executing the function
    assert func(5) == 10
