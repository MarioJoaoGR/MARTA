
import pytest
import sys
import os
from pytutils.files import burp

@pytest.mark.parametrize("filename, contents, mode, allow_stdout, expanduser, expandvars, expected_output", [
    (None, "Hello, world!", 'w', True, True, True, None),  # Invalid filename type
    ("-", None, 'w', True, True, True, None),              # Invalid contents type
    ("-", "Hello, world!", None, True, True, True, None),  # Invalid mode type
    ("-", "Hello, world!", 'w', False, True, True, None),   # Invalid allow_stdout type
    ("-", "Hello, world!", 'w', True, False, True, None),   # Invalid expanduser type
    ("-", "Hello, world!", 'w', True, True, False, None)    # Invalid expandvars type
])
def test_invalid_input(filename, contents, mode, allow_stdout, expanduser, expandvars, expected_output):
    with pytest.raises(TypeError):  # Expecting a TypeError due to invalid input types
        burp(filename, contents, mode=mode, allow_stdout=allow_stdout, expanduser=expanduser, expandvars=expandvars)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /dev
configfile: null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 6 items

../../../dev ..FFFF                                                      [100%]

=================================== FAILURES ===================================
_________ test_invalid_input[--Hello, world!-None-True-True-True-None] _________

filename = '-', contents = 'Hello, world!', mode = None, allow_stdout = True
expanduser = True, expandvars = True, expected_output = None

    @pytest.mark.parametrize("filename, contents, mode, allow_stdout, expanduser, expandvars, expected_output", [
        (None, "Hello, world!", 'w', True, True, True, None),  # Invalid filename type
        ("-", None, 'w', True, True, True, None),              # Invalid contents type
        ("-", "Hello, world!", None, True, True, True, None),  # Invalid mode type
        ("-", "Hello, world!", 'w', False, True, True, None),   # Invalid allow_stdout type
        ("-", "Hello, world!", 'w', True, False, True, None),   # Invalid expanduser type
        ("-", "Hello, world!", 'w', True, True, False, None)    # Invalid expandvars type
    ])
    def test_invalid_input(filename, contents, mode, allow_stdout, expanduser, expandvars, expected_output):
>       with pytest.raises(TypeError):  # Expecting a TypeError due to invalid input types
E       Failed: DID NOT RAISE <class 'TypeError'>

pytutils/Test4DT_tests/test_pytutils_files_burp_0_test_invalid_input.py:16: Failed
----------------------------- Captured stdout call -----------------------------
Hello, world!
__________ test_invalid_input[--Hello, world!-w-False-True-True-None] __________

filename = '-', contents = 'Hello, world!', mode = 'w', allow_stdout = False
expanduser = True, expandvars = True, expected_output = None

    @pytest.mark.parametrize("filename, contents, mode, allow_stdout, expanduser, expandvars, expected_output", [
        (None, "Hello, world!", 'w', True, True, True, None),  # Invalid filename type
        ("-", None, 'w', True, True, True, None),              # Invalid contents type
        ("-", "Hello, world!", None, True, True, True, None),  # Invalid mode type
        ("-", "Hello, world!", 'w', False, True, True, None),   # Invalid allow_stdout type
        ("-", "Hello, world!", 'w', True, False, True, None),   # Invalid expanduser type
        ("-", "Hello, world!", 'w', True, True, False, None)    # Invalid expandvars type
    ])
    def test_invalid_input(filename, contents, mode, allow_stdout, expanduser, expandvars, expected_output):
>       with pytest.raises(TypeError):  # Expecting a TypeError due to invalid input types
E       Failed: DID NOT RAISE <class 'TypeError'>

pytutils/Test4DT_tests/test_pytutils_files_burp_0_test_invalid_input.py:16: Failed
__________ test_invalid_input[--Hello, world!-w-True-False-True-None] __________

filename = '-', contents = 'Hello, world!', mode = 'w', allow_stdout = True
expanduser = False, expandvars = True, expected_output = None

    @pytest.mark.parametrize("filename, contents, mode, allow_stdout, expanduser, expandvars, expected_output", [
        (None, "Hello, world!", 'w', True, True, True, None),  # Invalid filename type
        ("-", None, 'w', True, True, True, None),              # Invalid contents type
        ("-", "Hello, world!", None, True, True, True, None),  # Invalid mode type
        ("-", "Hello, world!", 'w', False, True, True, None),   # Invalid allow_stdout type
        ("-", "Hello, world!", 'w', True, False, True, None),   # Invalid expanduser type
        ("-", "Hello, world!", 'w', True, True, False, None)    # Invalid expandvars type
    ])
    def test_invalid_input(filename, contents, mode, allow_stdout, expanduser, expandvars, expected_output):
>       with pytest.raises(TypeError):  # Expecting a TypeError due to invalid input types
E       Failed: DID NOT RAISE <class 'TypeError'>

pytutils/Test4DT_tests/test_pytutils_files_burp_0_test_invalid_input.py:16: Failed
----------------------------- Captured stdout call -----------------------------
Hello, world!
__________ test_invalid_input[--Hello, world!-w-True-True-False-None] __________

filename = '-', contents = 'Hello, world!', mode = 'w', allow_stdout = True
expanduser = True, expandvars = False, expected_output = None

    @pytest.mark.parametrize("filename, contents, mode, allow_stdout, expanduser, expandvars, expected_output", [
        (None, "Hello, world!", 'w', True, True, True, None),  # Invalid filename type
        ("-", None, 'w', True, True, True, None),              # Invalid contents type
        ("-", "Hello, world!", None, True, True, True, None),  # Invalid mode type
        ("-", "Hello, world!", 'w', False, True, True, None),   # Invalid allow_stdout type
        ("-", "Hello, world!", 'w', True, False, True, None),   # Invalid expanduser type
        ("-", "Hello, world!", 'w', True, True, False, None)    # Invalid expandvars type
    ])
    def test_invalid_input(filename, contents, mode, allow_stdout, expanduser, expandvars, expected_output):
>       with pytest.raises(TypeError):  # Expecting a TypeError due to invalid input types
E       Failed: DID NOT RAISE <class 'TypeError'>

pytutils/Test4DT_tests/test_pytutils_files_burp_0_test_invalid_input.py:16: Failed
----------------------------- Captured stdout call -----------------------------
Hello, world!
=============================== warnings summary ===============================
../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/nodeids: [Errno 13] Permission denied: '/dev/pytest-cache-files-7kudq3hx'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/lastfailed: [Errno 13] Permission denied: '/dev/pytest-cache-files-rk20vn4s'
    config.cache.set("cache/lastfailed", self.lastfailed)

../../../usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51
  /usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/stepwise: [Errno 13] Permission denied: '/dev/pytest-cache-files-c9sbuimq'
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED ../../../dev/::test_invalid_input[--Hello, world!-None-True-True-True-None]
FAILED ../../../dev/::test_invalid_input[--Hello, world!-w-False-True-True-None]
FAILED ../../../dev/::test_invalid_input[--Hello, world!-w-True-False-True-None]
FAILED ../../../dev/::test_invalid_input[--Hello, world!-w-True-True-False-None]
=================== 4 failed, 2 passed, 3 warnings in 0.07s ====================
"""