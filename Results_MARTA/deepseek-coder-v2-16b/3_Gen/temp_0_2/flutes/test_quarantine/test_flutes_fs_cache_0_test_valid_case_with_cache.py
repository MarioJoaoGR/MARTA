
import pytest
from pathlib import Path
import os
import pickle
import functools
from unittest.mock import patch
from flutes.fs import cache

# Define a sample function to be cached
@cache("my_function_output.pkl", verbose=False)
def my_function():
    return "Hello, World!"

# Test the caching functionality
def test_valid_case_with_cache():
    # Ensure the cache file does not exist initially
    assert not os.path.exists("my_function_output.pkl")
    
    # Call the function to trigger caching
    result = my_function()
    
    # Check if the cache file now exists and contains the expected data
    with open("my_function_output.pkl", "rb") as f:
        cached_result = pickle.load(f)
    assert os.path.exists("my_function_output.pkl")
    assert cached_result == "Hello, World!"
    
    # Ensure the function is not executed again when called a second time
    with patch('builtins.print') as mock_print:
        result = my_function()
        mock_print.assert_called_with("cache loaded from 'my_function_output.pkl'")

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

flutes/Test4DT_tests/test_flutes_fs_cache_0_test_valid_case_with_cache.py F [100%]

=================================== FAILURES ===================================
__________________________ test_valid_case_with_cache __________________________

    def test_valid_case_with_cache():
        # Ensure the cache file does not exist initially
        assert not os.path.exists("my_function_output.pkl")
    
        # Call the function to trigger caching
        result = my_function()
    
        # Check if the cache file now exists and contains the expected data
        with open("my_function_output.pkl", "rb") as f:
            cached_result = pickle.load(f)
        assert os.path.exists("my_function_output.pkl")
        assert cached_result == "Hello, World!"
    
        # Ensure the function is not executed again when called a second time
        with patch('builtins.print') as mock_print:
            result = my_function()
>           mock_print.assert_called_with("cache loaded from 'my_function_output.pkl'")

flutes/Test4DT_tests/test_flutes_fs_cache_0_test_valid_case_with_cache.py:32: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <MagicMock name='print' id='140606838523344'>
args = ("cache loaded from 'my_function_output.pkl'",), kwargs = {}
expected = 'print("cache loaded from \'my_function_output.pkl\'")'
actual = 'not called.'
error_message = 'expected call not found.\nExpected: print("cache loaded from \'my_function_output.pkl\'")\n  Actual: not called.'

    def assert_called_with(self, /, *args, **kwargs):
        """assert that the last call was made with the specified arguments.
    
        Raises an AssertionError if the args and keyword args passed in are
        different to the last call to the mock."""
        if self.call_args is None:
            expected = self._format_mock_call_signature(args, kwargs)
            actual = 'not called.'
            error_message = ('expected call not found.\nExpected: %s\n  Actual: %s'
                    % (expected, actual))
>           raise AssertionError(error_message)
E           AssertionError: expected call not found.
E           Expected: print("cache loaded from 'my_function_output.pkl'")
E             Actual: not called.

/usr/local/lib/python3.11/unittest/mock.py:930: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_fs_cache_0_test_valid_case_with_cache.py::test_valid_case_with_cache
============================== 1 failed in 0.12s ===============================
"""