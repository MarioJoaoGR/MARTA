
import pytest
from flutes.fs import cache
import os
import pickle
import functools
from pathlib import Path
from typing import Optional, Callable

# Assuming 'log' is a predefined function or you can mock it appropriately
def log(message):
    print(message)

@pytest.fixture
def example_function():
    @cache("my_cache.pkl", verbose=True)
    def expensive_function(x):
        return x * 2
    return expensive_function

def test_example_function(tmpdir, example_function):
    # Create a temporary directory for the cache file
    tmpdir = str(tmpdir)
    path = os.path.join(tmpdir, "my_cache.pkl")
    
    # First call should execute the function and save the result to cache
    result1 = example_function(5)
    assert result1 == 10
    with open(path, "rb") as f:
        cached_result = pickle.load(f)
    assert cached_result == 10
    
    # Second call should load the result from cache without executing the function
    result2 = example_function(5)
    assert result2 == 10

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_fs_cache_0_test_edge_cases.py F         [100%]

=================================== FAILURES ===================================
____________________________ test_example_function _____________________________

tmpdir = '/tmp/pytest-of-joaovitorino/pytest-2/test_example_function0'
example_function = <function example_function.<locals>.expensive_function at 0x7fab107511c0>

    def test_example_function(tmpdir, example_function):
        # Create a temporary directory for the cache file
        tmpdir = str(tmpdir)
        path = os.path.join(tmpdir, "my_cache.pkl")
    
        # First call should execute the function and save the result to cache
        result1 = example_function(5)
>       assert result1 == 10
E       assert 20 == 10

flutes/Test4DT_tests/test_flutes_fs_cache_0_test_edge_cases.py:28: AssertionError
----------------------------- Captured stdout call -----------------------------
[2026-03-24 16:26:19] Cache loaded from 'my_cache.pkl'
------------------------------ Captured log call -------------------------------
INFO     flutes.log:log.py:182 Cache loaded from 'my_cache.pkl'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_fs_cache_0_test_edge_cases.py::test_example_function
============================== 1 failed in 0.09s ===============================
"""