
import pytest
from pytutils.props import setterproperty

# Test fixture to create a mock setter property
@pytest.fixture
def create_mock_setterproperty():
    def _create_mock_setterproperty(func):
        return setterproperty(func)
    return _create_mock_setterproperty

# Test case for invalid input when setting the value
def test_invalid_input(create_mock_setterproperty):
    class MyClass:
        pass
    
    mock_setter = create_mock_setterproperty(lambda obj, new_value: None)
    instance = MyClass()
    
    with pytest.raises(TypeError):
        # Attempt to set a value that is not compatible with the setter function
        instance.mock_setter = "invalid input"

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
______________________________ test_invalid_input ______________________________

create_mock_setterproperty = <function create_mock_setterproperty.<locals>._create_mock_setterproperty at 0x7f423f5ec900>

    def test_invalid_input(create_mock_setterproperty):
        class MyClass:
            pass
    
        mock_setter = create_mock_setterproperty(lambda obj, new_value: None)
        instance = MyClass()
    
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

pytutils/Test4DT_tests/test_pytutils_props_setterproperty___set___0_test_invalid_input.py:20: Failed
=============================== warnings summary ===============================
../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/nodeids: [Errno 13] Permission denied: '/dev/pytest-cache-files-7crafuhy'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/lastfailed: [Errno 13] Permission denied: '/dev/pytest-cache-files-kspurkly'
    config.cache.set("cache/lastfailed", self.lastfailed)

../../../usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51
  /usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/stepwise: [Errno 13] Permission denied: '/dev/pytest-cache-files-quh4j8ai'
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED ../../../dev/::test_invalid_input - Failed: DID NOT RAISE <class 'Type...
======================== 1 failed, 3 warnings in 0.05s =========================
"""