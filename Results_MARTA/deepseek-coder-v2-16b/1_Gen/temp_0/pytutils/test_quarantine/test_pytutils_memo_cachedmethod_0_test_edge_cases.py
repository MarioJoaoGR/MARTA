
import pytest
from unittest.mock import Mock, patch
from pytutils.memo import cachedmethod

# Define a mock for CachedException if it doesn't exist in the module
try:
    from pytutils.exceptions import CachedException
except ImportError:
    class CachedException(Exception):
        pass

def test_cachedmethod():
    # Mock cachetools and its dependencies
    with patch('pytutils.memo.cachetools') as mock_cachetools:
        # Create a mock for typedkey
        mock_typedkey = Mock()
        mock_cachetools.typedkey = mock_typedkey
        
        # Define a method to be cached
        def expensive_function(self, arg):
            return f"Result of {arg}"

        # Apply the decorator
        @cachedmethod(cache=Mock(), key=lambda *args: args[1], lock=Mock(), typed=False)
        def cached_expensive_function(self, arg):
            return expensive_function(self, arg)

        # Create a mock instance to test the caching mechanism
        instance = Mock()
        instance.cache = {}  # Ensure there's an empty cache for the instance

        # First call should not hit the cache and compute the result
        assert cached_expensive_function(instance, "arg1") == "Result of arg1"
        
        # Second call with the same argument should hit the cache
        assert cached_expensive_function(instance, "arg1") == "Result of arg1"

        # Third call with a different argument should not hit the cache and compute again
        assert cached_expensive_function(instance, "arg2") == "Result of arg2"

if __name__ == "__main__":
    pytest.main()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

pytutils/Test4DT_tests/test_pytutils_memo_cachedmethod_0_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
______________________________ test_cachedmethod _______________________________

    def test_cachedmethod():
        # Mock cachetools and its dependencies
        with patch('pytutils.memo.cachetools') as mock_cachetools:
            # Create a mock for typedkey
            mock_typedkey = Mock()
            mock_cachetools.typedkey = mock_typedkey
    
            # Define a method to be cached
            def expensive_function(self, arg):
                return f"Result of {arg}"
    
            # Apply the decorator
>           @cachedmethod(cache=Mock(), key=lambda *args: args[1], lock=Mock(), typed=False)

pytutils/Test4DT_tests/test_pytutils_memo_cachedmethod_0_test_edge_cases.py:25: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

cache = <Mock id='139948436346000'>
key = <function test_cachedmethod.<locals>.<lambda> at 0x7f48474baf20>
lock = <Mock id='139948410675088'>, typed = False, cached_exception = None

    def cachedmethod(cache, key=_default, lock=None, typed=_default, cached_exception=None):
        """Decorator to wrap a class or instance method with a memoizing
        callable that saves results in a cache.
    
        You can also specify a cached exception to cache and re-throw as well.
    
        Originally from cachetools, but modified to support caching certain exceptions.
        """
        if key is not _default and not callable(key):
            key, typed = _default, key
        if typed is not _default:
>           warnings.warn(
                "Passing 'typed' to cachedmethod() is deprecated, "
                "use 'key=typedkey' instead", DeprecationWarning, 2
            )
E           NameError: name 'warnings' is not defined

pytutils/pytutils/memo.py:31: NameError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_memo_cachedmethod_0_test_edge_cases.py::test_cachedmethod
============================== 1 failed in 0.06s ===============================
"""