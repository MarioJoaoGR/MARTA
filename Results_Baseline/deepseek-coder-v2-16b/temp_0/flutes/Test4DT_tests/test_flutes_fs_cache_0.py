
# Module: flutes.fs
import os
import functools
import pickle
from pathlib import Path
from typing import Optional, Callable, NoReturn

# Assuming the following imports are available in flutes.fs module
# from flutes.fs import cache

def cache(path: Optional[Path], verbose: bool = True, name: Optional[str] = None):
    r"""A function decorator that caches the output of the function to disk. If the cache file exists, it is loaded from
    disk and the function will not be executed.

    :param path: Path to the cache file. If ``None``, no cache is loaded or saved.
    :param verbose: If ``True``, will print to log.
    :param name: Name of the object to load. Only used for logging purposes.
    """
    name = (name or 'cache').capitalize()

    def decorator(func):
        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            if path is not None and os.path.exists(str(path)):
                with open(path, "rb") as f:
                    ret = pickle.load(f)
                if verbose:
                    print(f"{name} loaded from '{path}'")
            else:
                ret = func(*args, **kwargs)
                if path is not None:
                    with open(path, "wb") as f:
                        pickle.dump(ret, f)
                    if verbose:
                        print(f"{name} saved to '{path}'")
            return ret

        return wrapped

    return decorator

# Test cases for the cache decorator

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
