
import os
import pickle
from pathlib import Path
from unittest.mock import patch, Mock
from flutes.fs import cache

def test_function():
    return 'Hello, World!'

@cache(Path('test_cache.pkl'), verbose=True, name='my_cache')
def cached_function():
    return test_function()

def test_valid_input():
    with patch('flutes.fs.os.path.exists', return_value=False):
        result = cached_function()
        assert result == 'Hello, World!'
        
        # Check if the cache file was created after the function execution
        assert os.path.exists('test_cache.pkl')
        
        # Load the cache file and check if it contains the expected data
        with open('test_cache.pkl', 'rb') as f:
            cached_result = pickle.load(f)
        assert cached_result == 'Hello, World!'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

flutes/Test4DT_tests/test_flutes_fs_cache_0_test_valid_input.py .F       [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        with patch('flutes.fs.os.path.exists', return_value=False):
            result = cached_function()
            assert result == 'Hello, World!'
    
            # Check if the cache file was created after the function execution
>           assert os.path.exists('test_cache.pkl')
E           AssertionError: assert False
E            +  where False = <MagicMock name='exists' id='140426016373264'>('test_cache.pkl')
E            +    where <MagicMock name='exists' id='140426016373264'> = <module 'posixpath' (frozen)>.exists
E            +      where <module 'posixpath' (frozen)> = os.path

flutes/Test4DT_tests/test_flutes_fs_cache_0_test_valid_input.py:21: AssertionError
----------------------------- Captured stdout call -----------------------------
[2026-03-24 17:52:58] My_cache saved to 'test_cache.pkl'
------------------------------ Captured log call -------------------------------
INFO     flutes.log:log.py:182 My_cache saved to 'test_cache.pkl'
=============================== warnings summary ===============================
Test4DT_tests/test_flutes_fs_cache_0_test_valid_input.py::test_function
  /usr/local/lib/python3.11/site-packages/_pytest/python.py:163: PytestReturnNotNoneWarning: Expected None, but Test4DT_tests/test_flutes_fs_cache_0_test_valid_input.py::test_function returned 'Hello, World!', which will be an error in a future version of pytest.  Did you mean to use `assert` instead of `return`?
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_fs_cache_0_test_valid_input.py::test_valid_input
==================== 1 failed, 1 passed, 1 warning in 0.09s ====================
"""