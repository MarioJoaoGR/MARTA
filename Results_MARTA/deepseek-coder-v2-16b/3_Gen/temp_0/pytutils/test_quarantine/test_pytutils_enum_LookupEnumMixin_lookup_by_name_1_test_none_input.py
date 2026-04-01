
import pytest
from pytutils.enum import LookupEnumMixin

def test_lookup_by_name_none_input():
    # Define an empty enum class to simulate no members
    class EmptyEnum(LookupEnumMixin, metaclass=type):
        pass
    
    # Call the method with None input
    result = LookupEnumMixin.lookup_by_name(EmptyEnum)
    
    # Assert that the result is an empty dictionary since there are no members
    assert result == {}

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
________________________ test_lookup_by_name_none_input ________________________

    def test_lookup_by_name_none_input():
        # Define an empty enum class to simulate no members
        class EmptyEnum(LookupEnumMixin, metaclass=type):
            pass
    
        # Call the method with None input
>       result = LookupEnumMixin.lookup_by_name(EmptyEnum)

pytutils/Test4DT_tests/test_pytutils_enum_LookupEnumMixin_lookup_by_name_1_test_none_input.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
pytutils/pytutils/props.py:10: in __get__
    return self.f(owner)
pytutils/pytutils/props.py:49: in _lazyclassprop
    setattr(cls, attr_name, fn(cls))
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

cls = <class 'pytutils.enum.LookupEnumMixin'>

    @lazyclassproperty
    def lookup_by_name(cls):
>       return cls.__members__
E       AttributeError: type object 'LookupEnumMixin' has no attribute '__members__'

pytutils/pytutils/enum.py:7: AttributeError
=============================== warnings summary ===============================
../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/nodeids: [Errno 13] Permission denied: '/dev/pytest-cache-files-g7zyfeeq'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/lastfailed: [Errno 13] Permission denied: '/dev/pytest-cache-files-xkczoxv9'
    config.cache.set("cache/lastfailed", self.lastfailed)

../../../usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51
  /usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/stepwise: [Errno 13] Permission denied: '/dev/pytest-cache-files-4_x300d4'
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED ../../../dev/::test_lookup_by_name_none_input - AttributeError: type o...
======================== 1 failed, 3 warnings in 0.08s =========================
"""