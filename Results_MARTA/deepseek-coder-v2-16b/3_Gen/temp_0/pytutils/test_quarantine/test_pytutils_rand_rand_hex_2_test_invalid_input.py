
import pytest
from pytutils.rand import rand_hex
import random

@pytest.mark.parametrize("invalid_input", ["string", 3.14, None])
def test_invalid_input(invalid_input):
    with pytest.raises(TypeError):
        rand_hex(invalid_input)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /dev
configfile: null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

../../../dev .F.                                                         [100%]

=================================== FAILURES ===================================
___________________________ test_invalid_input[3.14] ___________________________

self = <random.Random object at 0x55ade215b4d0>, start = 6038.606714024353
stop = None, step = 1

    def randrange(self, start, stop=None, step=_ONE):
        """Choose a random item from range(stop) or range(start, stop[, step]).
    
        Roughly equivalent to ``choice(range(start, stop, step))`` but
        supports arbitrarily large ranges and is optimized for common cases.
    
        """
    
        # This code is a bit messy to make it fast for the
        # common case while still doing adequate error checking.
        try:
>           istart = _index(start)
E           TypeError: 'float' object cannot be interpreted as an integer

/usr/local/lib/python3.11/random.py:295: TypeError

During handling of the above exception, another exception occurred:

invalid_input = 3.14

    @pytest.mark.parametrize("invalid_input", ["string", 3.14, None])
    def test_invalid_input(invalid_input):
        with pytest.raises(TypeError):
>           rand_hex(invalid_input)

pytutils/Test4DT_tests/test_pytutils_rand_rand_hex_2_test_invalid_input.py:9: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
pytutils/pytutils/rand.py:11: in rand_hex
    return '%0{}x'.format(length) % random.randrange(16**length)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <random.Random object at 0x55ade215b4d0>, start = 6038.606714024353
stop = None, step = 1

    def randrange(self, start, stop=None, step=_ONE):
        """Choose a random item from range(stop) or range(start, stop[, step]).
    
        Roughly equivalent to ``choice(range(start, stop, step))`` but
        supports arbitrarily large ranges and is optimized for common cases.
    
        """
    
        # This code is a bit messy to make it fast for the
        # common case while still doing adequate error checking.
        try:
            istart = _index(start)
        except TypeError:
            istart = int(start)
            if istart != start:
                _warn('randrange() will raise TypeError in the future',
                      DeprecationWarning, 2)
>               raise ValueError("non-integer arg 1 for randrange()")
E               ValueError: non-integer arg 1 for randrange()

/usr/local/lib/python3.11/random.py:301: ValueError
=============================== warnings summary ===============================
::test_invalid_input[3.14]
  /projects/F202407648IACDCF2/mario/pytutils/pytutils/rand.py:11: DeprecationWarning: randrange() will raise TypeError in the future
    return '%0{}x'.format(length) % random.randrange(16**length)

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/nodeids: [Errno 13] Permission denied: '/dev/pytest-cache-files-vi67a8vg'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/lastfailed: [Errno 13] Permission denied: '/dev/pytest-cache-files-ik6yvuun'
    config.cache.set("cache/lastfailed", self.lastfailed)

../../../usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51
  /usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/stepwise: [Errno 13] Permission denied: '/dev/pytest-cache-files-q8n9a4zh'
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED ../../../dev/::test_invalid_input[3.14] - ValueError: non-integer arg ...
=================== 1 failed, 2 passed, 4 warnings in 0.09s ====================
"""