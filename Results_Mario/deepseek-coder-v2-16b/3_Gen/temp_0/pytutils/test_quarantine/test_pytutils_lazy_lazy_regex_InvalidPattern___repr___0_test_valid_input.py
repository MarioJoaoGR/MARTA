
import pytest
from pytutils.lazy.lazy_regex import InvalidPattern

def test_valid_input():
    msg = "The provided pattern does not match any known format."
    try:
        raise InvalidPattern(msg)
    except InvalidPattern as e:
        assert str(e) == f"InvalidPattern('{msg}')"

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
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        msg = "The provided pattern does not match any known format."
        try:
>           raise InvalidPattern(msg)
E           pytutils.lazy.lazy_regex.InvalidPattern: <exception str() failed>

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_InvalidPattern___repr___0_test_valid_input.py:8: InvalidPattern

During handling of the above exception, another exception occurred:

    def test_valid_input():
        msg = "The provided pattern does not match any known format."
        try:
            raise InvalidPattern(msg)
        except InvalidPattern as e:
>           assert str(e) == f"InvalidPattern('{msg}')"

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_InvalidPattern___repr___0_test_valid_input.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
pytutils/pytutils/lazy/lazy_regex.py:74: in __str__
    s = self._format()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <[UnboundLocalError("cannot access local variable 'e' where it is not associated with a value") raised in repr()] InvalidPattern object at 0x7feea1695de0>

    def _format(self):
        s = getattr(self, '_preformatted_string', None)
        if s is not None:
            # contains a preformatted message
            return s
        try:
            fmt = self._get_format_string()
            if fmt:
                d = dict(self.__dict__)
                s = fmt % d
                # __str__() should always return a 'str' object
                # never a 'unicode' object.
                return s
        except Exception as e:
            pass # just bind to 'e' for formatting below
        else:
            e = None
        return 'Unprintable exception %s: dict=%r, fmt=%r, error=%r' \
            % (self.__class__.__name__,
               self.__dict__,
               getattr(self, '_fmt', None),
>              e)
E       UnboundLocalError: cannot access local variable 'e' where it is not associated with a value

pytutils/pytutils/lazy/lazy_regex.py:60: UnboundLocalError
=============================== warnings summary ===============================
../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/nodeids: [Errno 13] Permission denied: '/dev/pytest-cache-files-lwq44q74'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/lastfailed: [Errno 13] Permission denied: '/dev/pytest-cache-files-k9vmkjrm'
    config.cache.set("cache/lastfailed", self.lastfailed)

../../../usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51
  /usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/stepwise: [Errno 13] Permission denied: '/dev/pytest-cache-files-vyxex3ap'
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED ../../../dev/::test_valid_input - UnboundLocalError: cannot access loc...
======================== 1 failed, 3 warnings in 0.08s =========================
"""