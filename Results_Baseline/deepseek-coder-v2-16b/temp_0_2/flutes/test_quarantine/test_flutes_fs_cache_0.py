
import pytest
from unittest.mock import patch
import os
import pickle
import functools
from pathlib import Path

# Import the function from its module
from flutes.fs import cache

@pytest.fixture(params=[None, "my_cache.pkl", "my_other_cache.pkl"])
def cache_path(request):
    return request.param

@pytest.fixture(params=[True, False])
def verbose(request):
    return request.param

@pytest.fixture(params=[None, "custom_name", "another_cache"])
def name(request):
    return request.param

@pytest.fixture
def expensive_computation():
    @cache(path=None)
    def func(a, b):
        return a + b
    return func

@pytest.fixture
def another_expensive_computation():
    @cache(path="my_other_cache.pkl", name="another_cache")
    def func(x, y):
        return x * y
    return func

# Test cases for the cache decorator
def test_cache_with_no_path(cache_path, verbose, name):
    @cache(path=cache_path, verbose=verbose, name=name)
    def func():
        pass
    
    with pytest.raises(TypeError):
        func()

@patch('flutes.fs.os.path.exists', return_value=True)
def test_cache_with_existing_file(mock_exists, cache_path, verbose, name):
    @cache(path=cache_path, verbose=verbose, name=name)
    def func():
        return 42
    
    result = func()
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 36 items

flutes/Test4DT_tests/test_flutes_fs_cache_0.py FFFFFFFFFFFFFFFFFF....... [ 69%]
...........                                                              [100%]

=================================== FAILURES ===================================
___________________ test_cache_with_no_path[None-True-None] ____________________

cache_path = None, verbose = True, name = None

    def test_cache_with_no_path(cache_path, verbose, name):
        @cache(path=cache_path, verbose=verbose, name=name)
        def func():
            pass
    
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

flutes/Test4DT_tests/test_flutes_fs_cache_0.py:44: Failed
________________ test_cache_with_no_path[None-True-custom_name] ________________

cache_path = None, verbose = True, name = 'custom_name'

    def test_cache_with_no_path(cache_path, verbose, name):
        @cache(path=cache_path, verbose=verbose, name=name)
        def func():
            pass
    
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

flutes/Test4DT_tests/test_flutes_fs_cache_0.py:44: Failed
_______________ test_cache_with_no_path[None-True-another_cache] _______________

cache_path = None, verbose = True, name = 'another_cache'

    def test_cache_with_no_path(cache_path, verbose, name):
        @cache(path=cache_path, verbose=verbose, name=name)
        def func():
            pass
    
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

flutes/Test4DT_tests/test_flutes_fs_cache_0.py:44: Failed
___________________ test_cache_with_no_path[None-False-None] ___________________

cache_path = None, verbose = False, name = None

    def test_cache_with_no_path(cache_path, verbose, name):
        @cache(path=cache_path, verbose=verbose, name=name)
        def func():
            pass
    
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

flutes/Test4DT_tests/test_flutes_fs_cache_0.py:44: Failed
_______________ test_cache_with_no_path[None-False-custom_name] ________________

cache_path = None, verbose = False, name = 'custom_name'

    def test_cache_with_no_path(cache_path, verbose, name):
        @cache(path=cache_path, verbose=verbose, name=name)
        def func():
            pass
    
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

flutes/Test4DT_tests/test_flutes_fs_cache_0.py:44: Failed
______________ test_cache_with_no_path[None-False-another_cache] _______________

cache_path = None, verbose = False, name = 'another_cache'

    def test_cache_with_no_path(cache_path, verbose, name):
        @cache(path=cache_path, verbose=verbose, name=name)
        def func():
            pass
    
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

flutes/Test4DT_tests/test_flutes_fs_cache_0.py:44: Failed
_______________ test_cache_with_no_path[my_cache.pkl-True-None] ________________

cache_path = 'my_cache.pkl', verbose = True, name = None

    def test_cache_with_no_path(cache_path, verbose, name):
        @cache(path=cache_path, verbose=verbose, name=name)
        def func():
            pass
    
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

flutes/Test4DT_tests/test_flutes_fs_cache_0.py:44: Failed
----------------------------- Captured stdout call -----------------------------
[2026-03-25 07:03:23] Cache loaded from 'my_cache.pkl'
------------------------------ Captured log call -------------------------------
INFO     flutes.log:log.py:182 Cache loaded from 'my_cache.pkl'
____________ test_cache_with_no_path[my_cache.pkl-True-custom_name] ____________

cache_path = 'my_cache.pkl', verbose = True, name = 'custom_name'

    def test_cache_with_no_path(cache_path, verbose, name):
        @cache(path=cache_path, verbose=verbose, name=name)
        def func():
            pass
    
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

flutes/Test4DT_tests/test_flutes_fs_cache_0.py:44: Failed
----------------------------- Captured stdout call -----------------------------
[2026-03-25 07:03:23] Custom_name loaded from 'my_cache.pkl'
------------------------------ Captured log call -------------------------------
INFO     flutes.log:log.py:182 Custom_name loaded from 'my_cache.pkl'
___________ test_cache_with_no_path[my_cache.pkl-True-another_cache] ___________

cache_path = 'my_cache.pkl', verbose = True, name = 'another_cache'

    def test_cache_with_no_path(cache_path, verbose, name):
        @cache(path=cache_path, verbose=verbose, name=name)
        def func():
            pass
    
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

flutes/Test4DT_tests/test_flutes_fs_cache_0.py:44: Failed
----------------------------- Captured stdout call -----------------------------
[2026-03-25 07:03:23] Another_cache loaded from 'my_cache.pkl'
------------------------------ Captured log call -------------------------------
INFO     flutes.log:log.py:182 Another_cache loaded from 'my_cache.pkl'
_______________ test_cache_with_no_path[my_cache.pkl-False-None] _______________

cache_path = 'my_cache.pkl', verbose = False, name = None

    def test_cache_with_no_path(cache_path, verbose, name):
        @cache(path=cache_path, verbose=verbose, name=name)
        def func():
            pass
    
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

flutes/Test4DT_tests/test_flutes_fs_cache_0.py:44: Failed
___________ test_cache_with_no_path[my_cache.pkl-False-custom_name] ____________

cache_path = 'my_cache.pkl', verbose = False, name = 'custom_name'

    def test_cache_with_no_path(cache_path, verbose, name):
        @cache(path=cache_path, verbose=verbose, name=name)
        def func():
            pass
    
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

flutes/Test4DT_tests/test_flutes_fs_cache_0.py:44: Failed
__________ test_cache_with_no_path[my_cache.pkl-False-another_cache] ___________

cache_path = 'my_cache.pkl', verbose = False, name = 'another_cache'

    def test_cache_with_no_path(cache_path, verbose, name):
        @cache(path=cache_path, verbose=verbose, name=name)
        def func():
            pass
    
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

flutes/Test4DT_tests/test_flutes_fs_cache_0.py:44: Failed
____________ test_cache_with_no_path[my_other_cache.pkl-True-None] _____________

cache_path = 'my_other_cache.pkl', verbose = True, name = None

    def test_cache_with_no_path(cache_path, verbose, name):
        @cache(path=cache_path, verbose=verbose, name=name)
        def func():
            pass
    
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

flutes/Test4DT_tests/test_flutes_fs_cache_0.py:44: Failed
----------------------------- Captured stdout call -----------------------------
[2026-03-25 07:03:23] Cache loaded from 'my_other_cache.pkl'
------------------------------ Captured log call -------------------------------
INFO     flutes.log:log.py:182 Cache loaded from 'my_other_cache.pkl'
_________ test_cache_with_no_path[my_other_cache.pkl-True-custom_name] _________

cache_path = 'my_other_cache.pkl', verbose = True, name = 'custom_name'

    def test_cache_with_no_path(cache_path, verbose, name):
        @cache(path=cache_path, verbose=verbose, name=name)
        def func():
            pass
    
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

flutes/Test4DT_tests/test_flutes_fs_cache_0.py:44: Failed
----------------------------- Captured stdout call -----------------------------
[2026-03-25 07:03:23] Custom_name loaded from 'my_other_cache.pkl'
------------------------------ Captured log call -------------------------------
INFO     flutes.log:log.py:182 Custom_name loaded from 'my_other_cache.pkl'
________ test_cache_with_no_path[my_other_cache.pkl-True-another_cache] ________

cache_path = 'my_other_cache.pkl', verbose = True, name = 'another_cache'

    def test_cache_with_no_path(cache_path, verbose, name):
        @cache(path=cache_path, verbose=verbose, name=name)
        def func():
            pass
    
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

flutes/Test4DT_tests/test_flutes_fs_cache_0.py:44: Failed
----------------------------- Captured stdout call -----------------------------
[2026-03-25 07:03:23] Another_cache loaded from 'my_other_cache.pkl'
------------------------------ Captured log call -------------------------------
INFO     flutes.log:log.py:182 Another_cache loaded from 'my_other_cache.pkl'
____________ test_cache_with_no_path[my_other_cache.pkl-False-None] ____________

cache_path = 'my_other_cache.pkl', verbose = False, name = None

    def test_cache_with_no_path(cache_path, verbose, name):
        @cache(path=cache_path, verbose=verbose, name=name)
        def func():
            pass
    
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

flutes/Test4DT_tests/test_flutes_fs_cache_0.py:44: Failed
________ test_cache_with_no_path[my_other_cache.pkl-False-custom_name] _________

cache_path = 'my_other_cache.pkl', verbose = False, name = 'custom_name'

    def test_cache_with_no_path(cache_path, verbose, name):
        @cache(path=cache_path, verbose=verbose, name=name)
        def func():
            pass
    
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

flutes/Test4DT_tests/test_flutes_fs_cache_0.py:44: Failed
_______ test_cache_with_no_path[my_other_cache.pkl-False-another_cache] ________

cache_path = 'my_other_cache.pkl', verbose = False, name = 'another_cache'

    def test_cache_with_no_path(cache_path, verbose, name):
        @cache(path=cache_path, verbose=verbose, name=name)
        def func():
            pass
    
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

flutes/Test4DT_tests/test_flutes_fs_cache_0.py:44: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_fs_cache_0.py::test_cache_with_no_path[None-True-None]
FAILED flutes/Test4DT_tests/test_flutes_fs_cache_0.py::test_cache_with_no_path[None-True-custom_name]
FAILED flutes/Test4DT_tests/test_flutes_fs_cache_0.py::test_cache_with_no_path[None-True-another_cache]
FAILED flutes/Test4DT_tests/test_flutes_fs_cache_0.py::test_cache_with_no_path[None-False-None]
FAILED flutes/Test4DT_tests/test_flutes_fs_cache_0.py::test_cache_with_no_path[None-False-custom_name]
FAILED flutes/Test4DT_tests/test_flutes_fs_cache_0.py::test_cache_with_no_path[None-False-another_cache]
FAILED flutes/Test4DT_tests/test_flutes_fs_cache_0.py::test_cache_with_no_path[my_cache.pkl-True-None]
FAILED flutes/Test4DT_tests/test_flutes_fs_cache_0.py::test_cache_with_no_path[my_cache.pkl-True-custom_name]
FAILED flutes/Test4DT_tests/test_flutes_fs_cache_0.py::test_cache_with_no_path[my_cache.pkl-True-another_cache]
FAILED flutes/Test4DT_tests/test_flutes_fs_cache_0.py::test_cache_with_no_path[my_cache.pkl-False-None]
FAILED flutes/Test4DT_tests/test_flutes_fs_cache_0.py::test_cache_with_no_path[my_cache.pkl-False-custom_name]
FAILED flutes/Test4DT_tests/test_flutes_fs_cache_0.py::test_cache_with_no_path[my_cache.pkl-False-another_cache]
FAILED flutes/Test4DT_tests/test_flutes_fs_cache_0.py::test_cache_with_no_path[my_other_cache.pkl-True-None]
FAILED flutes/Test4DT_tests/test_flutes_fs_cache_0.py::test_cache_with_no_path[my_other_cache.pkl-True-custom_name]
FAILED flutes/Test4DT_tests/test_flutes_fs_cache_0.py::test_cache_with_no_path[my_other_cache.pkl-True-another_cache]
FAILED flutes/Test4DT_tests/test_flutes_fs_cache_0.py::test_cache_with_no_path[my_other_cache.pkl-False-None]
FAILED flutes/Test4DT_tests/test_flutes_fs_cache_0.py::test_cache_with_no_path[my_other_cache.pkl-False-custom_name]
FAILED flutes/Test4DT_tests/test_flutes_fs_cache_0.py::test_cache_with_no_path[my_other_cache.pkl-False-another_cache]
======================== 18 failed, 18 passed in 0.16s =========================
"""