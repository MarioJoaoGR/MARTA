
import os
import functools
import pickle
from pathlib import Path
from typing import Optional, Callable, NoReturn
import pytest

# Assuming the following imports are available in flutes.fs module
from flutes.fs import cache

def test_cache_with_verbose():
    @cache("my_cache.pkl", verbose=True)
    def expensive_function(x):
        return x * 2
    
    # First call should execute and cache the function
    result = expensive_function(5)
    assert result == 10, f"Expected 10 but got {result}"
    
    # Second call should load from cache
    result = expensive_function(5)
    assert result == 10, f"Expected 10 but got {result}"

def test_cache_without_verbose():
    @cache("my_cache.pkl", verbose=False)
    def log_example(x):
        return x * 2
    
    # First call should execute and cache the function, no logs expected
    result = log_example(5)
    assert result == 10, f"Expected 10 but got {result}"
    
    # Second call should load from cache, no logs expected
    result = log_example(5)
    assert result == 10, f"Expected 10 but got {result}"

def test_cache_with_custom_name():
    @cache("my_cache.pkl", verbose=True, name="custom_log")
    def custom_function(x):
        return x * 2
    
    # First call should execute and cache the function
    result = custom_function(5)
    assert result == 10, f"Expected 10 but got {result}"
    
    # Second call should load from cache
    result = custom_function(5)
    assert result == 10, f"Expected 10 but got {result}"

def test_cache_with_none_path():
    @cache(None, verbose=True)
    def no_cache_function(x):
        return x * 2
    
    # First call should execute and not cache the function
    result = no_cache_function(5)
    assert result == 10, f"Expected 10 but got {result}"
    
    # Second call should re-execute the function as there's no cache path specified
    result = no_cache_function(5)
    assert result == 10, f"Expected 10 but got {result}"

# Additional test cases to cover uncovered lines

def test_capitalize_name():
    @cache("my_cache.pkl", verbose=True, name="custom_log")
    def custom_function(x):
        return x * 2
    
    # Ensure the name is capitalized correctly