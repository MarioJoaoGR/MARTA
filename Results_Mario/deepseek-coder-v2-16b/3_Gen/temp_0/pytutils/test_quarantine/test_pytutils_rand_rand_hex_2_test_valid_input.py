
import pytest
from unittest.mock import patch
import random
from pytutils.rand import rand_hex

@pytest.mark.parametrize("length", [3, 5, 8, 10])
def test_valid_input(length):
    with patch('random.randrange') as mock_randrange:
        # Mock the return value of random.randrange to control the output
        mock_randrange.return_value = 0xabcdef  # Example hex value

        result = rand_hex(length)

        # Check if the length of the generated hex string matches the expected length
        assert len(result) == length

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

../../../dev FF..                                                        [100%]

=================================== FAILURES ===================================
_____________________________ test_valid_input[3] ______________________________

length = 3

    @pytest.mark.parametrize("length", [3, 5, 8, 10])
    def test_valid_input(length):
        with patch('random.randrange') as mock_randrange:
            # Mock the return value of random.randrange to control the output
            mock_randrange.return_value = 0xabcdef  # Example hex value
    
            result = rand_hex(length)
    
            # Check if the length of the generated hex string matches the expected length
>           assert len(result) == length
E           AssertionError: assert 6 == 3
E            +  where 6 = len('abcdef')

pytutils/Test4DT_tests/test_pytutils_rand_rand_hex_2_test_valid_input.py:16: AssertionError
_____________________________ test_valid_input[5] ______________________________

length = 5

    @pytest.mark.parametrize("length", [3, 5, 8, 10])
    def test_valid_input(length):
        with patch('random.randrange') as mock_randrange:
            # Mock the return value of random.randrange to control the output
            mock_randrange.return_value = 0xabcdef  # Example hex value
    
            result = rand_hex(length)
    
            # Check if the length of the generated hex string matches the expected length
>           assert len(result) == length
E           AssertionError: assert 6 == 5
E            +  where 6 = len('abcdef')

pytutils/Test4DT_tests/test_pytutils_rand_rand_hex_2_test_valid_input.py:16: AssertionError
=============================== warnings summary ===============================
../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/nodeids: [Errno 13] Permission denied: '/dev/pytest-cache-files-jy88rdpn'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/lastfailed: [Errno 13] Permission denied: '/dev/pytest-cache-files-sv8ru9vf'
    config.cache.set("cache/lastfailed", self.lastfailed)

../../../usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51
  /usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/stepwise: [Errno 13] Permission denied: '/dev/pytest-cache-files-ufjxkans'
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED ../../../dev/::test_valid_input[3] - AssertionError: assert 6 == 3
FAILED ../../../dev/::test_valid_input[5] - AssertionError: assert 6 == 5
=================== 2 failed, 2 passed, 3 warnings in 0.08s ====================
"""