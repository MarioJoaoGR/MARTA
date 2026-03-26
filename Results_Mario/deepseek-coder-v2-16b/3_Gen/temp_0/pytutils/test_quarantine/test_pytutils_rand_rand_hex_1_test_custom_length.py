
import pytest
from unittest.mock import patch
import random
from pytutils.rand import rand_hex

@pytest.mark.parametrize("input_length, expected", [
    (8, True),
    (10, True),
    (5, True),
    (20, True),
])
def test_custom_length(input_length, expected):
    with patch('random.randrange') as mock_randrange:
        # Set the return value of randrange to always produce a valid hex character
        mock_randrange.return_value = 0x123456789abcdef

        result = rand_hex(input_length)
        assert len(result) == input_length

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /dev
configfile: null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 4 items

../../../dev FFF.                                                        [100%]

=================================== FAILURES ===================================
__________________________ test_custom_length[8-True] __________________________

input_length = 8, expected = True

    @pytest.mark.parametrize("input_length, expected", [
        (8, True),
        (10, True),
        (5, True),
        (20, True),
    ])
    def test_custom_length(input_length, expected):
        with patch('random.randrange') as mock_randrange:
            # Set the return value of randrange to always produce a valid hex character
            mock_randrange.return_value = 0x123456789abcdef
    
            result = rand_hex(input_length)
>           assert len(result) == input_length
E           AssertionError: assert 15 == 8
E            +  where 15 = len('123456789abcdef')

pytutils/Test4DT_tests/test_pytutils_rand_rand_hex_1_test_custom_length.py:19: AssertionError
_________________________ test_custom_length[10-True] __________________________

input_length = 10, expected = True

    @pytest.mark.parametrize("input_length, expected", [
        (8, True),
        (10, True),
        (5, True),
        (20, True),
    ])
    def test_custom_length(input_length, expected):
        with patch('random.randrange') as mock_randrange:
            # Set the return value of randrange to always produce a valid hex character
            mock_randrange.return_value = 0x123456789abcdef
    
            result = rand_hex(input_length)
>           assert len(result) == input_length
E           AssertionError: assert 15 == 10
E            +  where 15 = len('123456789abcdef')

pytutils/Test4DT_tests/test_pytutils_rand_rand_hex_1_test_custom_length.py:19: AssertionError
__________________________ test_custom_length[5-True] __________________________

input_length = 5, expected = True

    @pytest.mark.parametrize("input_length, expected", [
        (8, True),
        (10, True),
        (5, True),
        (20, True),
    ])
    def test_custom_length(input_length, expected):
        with patch('random.randrange') as mock_randrange:
            # Set the return value of randrange to always produce a valid hex character
            mock_randrange.return_value = 0x123456789abcdef
    
            result = rand_hex(input_length)
>           assert len(result) == input_length
E           AssertionError: assert 15 == 5
E            +  where 15 = len('123456789abcdef')

pytutils/Test4DT_tests/test_pytutils_rand_rand_hex_1_test_custom_length.py:19: AssertionError
=============================== warnings summary ===============================
../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/nodeids: [Errno 13] Permission denied: '/dev/pytest-cache-files-ar_pt8nw'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/lastfailed: [Errno 13] Permission denied: '/dev/pytest-cache-files-daqnohsu'
    config.cache.set("cache/lastfailed", self.lastfailed)

../../../usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51
  /usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/stepwise: [Errno 13] Permission denied: '/dev/pytest-cache-files-ty_facn9'
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED ../../../dev/::test_custom_length[8-True] - AssertionError: assert 15 ...
FAILED ../../../dev/::test_custom_length[10-True] - AssertionError: assert 15...
FAILED ../../../dev/::test_custom_length[5-True] - AssertionError: assert 15 ...
=================== 3 failed, 1 passed, 3 warnings in 0.07s ====================
"""