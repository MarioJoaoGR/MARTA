
import pytest
from unittest.mock import MagicMock
from pytutils.props import setterproperty

def test_setterproperty():
    # Create a mock function to be used as the property's getter/setter
    mock_func = MagicMock()
    
    # Initialize the setterproperty with the mock function
    sp = setterproperty(mock_func)
    
    # Create an instance of a class that uses the setterproperty
    class MyClass:
        def __init__(self, value):
            self._value = value
        
        @sp
        def value(self):
            return self._value
        
        @value.setter
        def value(self, new_value):
            self._value = new_value
    
    # Create an instance of MyClass
    obj = MyClass(10)
    
    # Test the getter and setter
    assert obj.value == 10
    obj.value = 20
    assert obj.value == 20
    mock_func.assert_called_with(obj, 20)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /dev
configfile: null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

../../../dev F                                                           [100%]

=================================== FAILURES ===================================
_____________________________ test_setterproperty ______________________________

    def test_setterproperty():
        # Create a mock function to be used as the property's getter/setter
        mock_func = MagicMock()
    
        # Initialize the setterproperty with the mock function
        sp = setterproperty(mock_func)
    
        # Create an instance of a class that uses the setterproperty
>       class MyClass:

pytutils/Test4DT_tests/test_pytutils_props_setterproperty___set___0_test_edge_case.py:14: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

    class MyClass:
        def __init__(self, value):
            self._value = value
    
>       @sp
E       TypeError: 'setterproperty' object is not callable

pytutils/Test4DT_tests/test_pytutils_props_setterproperty___set___0_test_edge_case.py:18: TypeError
=============================== warnings summary ===============================
../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/nodeids: [Errno 13] Permission denied: '/dev/pytest-cache-files-0zq0m0yw'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/lastfailed: [Errno 13] Permission denied: '/dev/pytest-cache-files-8dahx63q'
    config.cache.set("cache/lastfailed", self.lastfailed)

../../../usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51
  /usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/stepwise: [Errno 13] Permission denied: '/dev/pytest-cache-files-hlphy5pl'
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED ../../../dev/::test_setterproperty - TypeError: 'setterproperty' objec...
======================== 1 failed, 3 warnings in 0.05s =========================
"""