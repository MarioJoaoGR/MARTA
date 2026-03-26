
import os
import pickle
from pathlib import Path
import functools
from typing import Optional, Callable, Any
from flutes.fs import log

def cache(path: Optional[PathType], verbose: bool = True, name: Optional[str] = None):
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
                with open(str(path), "rb") as f:
                    ret = pickle.load(f)
                if verbose:
                    log(f"{name} loaded from '{path}'")
            else:
                ret = func(*args, **kwargs)
                if path is not None:
                    with open(str(path), "wb") as f:
                        pickle.dump(ret, f)
                    if verbose:
                        log(f"{name} saved to '{path}'")
            return ret

        return wrapped

    return decorator

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_fs_cache_0_test_valid_input
flutes/Test4DT_tests/test_flutes_fs_cache_0_test_valid_input.py:9:25: E0602: Undefined variable 'PathType' (undefined-variable)

"""