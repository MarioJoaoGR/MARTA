
import os
import pickle
from unittest.mock import patch
import pytest
from flutes.fs import cache, PathType

@cache("test_cache.pkl", verbose=True)
def cached_function():
    return "Hello, World!"

def test_valid_input():
    with patch('flutes.fs.os.path.exists', return_value=False):
        result = cached_function()
        assert result == "Hello, World!"

        # Check if the cache file was created after the function execution
        with open("test_cache.pkl", "rb") as f:
            loaded_result = pickle.load(f)
        assert loaded_result == "Hello, World!"
