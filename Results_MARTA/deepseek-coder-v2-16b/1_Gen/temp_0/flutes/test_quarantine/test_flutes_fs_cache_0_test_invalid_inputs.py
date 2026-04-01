
import pytest
from unittest.mock import patch
import os
import pickle
from flutes.fs import PathType
from flutes.log import log

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
            if path is not None and os.path.exists(path):
                with open(path, "rb") as f:
                    ret = pickle.load(f)
                if verbose:
                    log(f"{name} loaded from '{path}'")
            else:
                ret = func(*args, **kwargs)
                if path is not None:
                    with open(path, "wb") as f:
                        pickle.dump(ret, f)
                    if verbose:
                        log(f"{name} saved to '{path}'")
            return ret

        return wrapped

    return decorator

@pytest.mark.parametrize("input_value", [5])
def test_invalid_inputs(function_to_be_cached, input_value):
    with patch('flutes.fs.os.path.exists', return_value=False):
        result = function_to_be_cached(input_value)
        assert result == input_value * 2

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_fs_cache_0_test_invalid_inputs
flutes/Test4DT_tests/test_flutes_fs_cache_0_test_invalid_inputs.py:9:16: E0602: Undefined variable 'Optional' (undefined-variable)
flutes/Test4DT_tests/test_flutes_fs_cache_0_test_invalid_inputs.py:9:64: E0602: Undefined variable 'Optional' (undefined-variable)
flutes/Test4DT_tests/test_flutes_fs_cache_0_test_invalid_inputs.py:20:9: E0602: Undefined variable 'functools' (undefined-variable)


"""