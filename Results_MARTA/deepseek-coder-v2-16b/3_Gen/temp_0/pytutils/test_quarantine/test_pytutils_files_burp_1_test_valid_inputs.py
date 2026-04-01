
import pytest
from unittest.mock import patch
from pytutils.files import burp

@pytest.mark.parametrize("filename, contents, expected", [
    ('example.txt', 'Hello, world!', None),
    ('-', 'Hello, world!', None),
])
def test_valid_inputs(filename, contents, expected):
    with patch('sys.stdout', new=[]) as mock_stdout:
        burp(filename, contents)
    assert mock_stdout.getvalue().strip() == ('Hello, world!' if filename == '-' else '')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /dev
configfile: null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

../../../dev FF                                                          [100%]

=================================== FAILURES ===================================
______________ test_valid_inputs[example.txt-Hello, world!-None] _______________

filename = 'example.txt', contents = 'Hello, world!', expected = None

    @pytest.mark.parametrize("filename, contents, expected", [
        ('example.txt', 'Hello, world!', None),
        ('-', 'Hello, world!', None),
    ])
    def test_valid_inputs(filename, contents, expected):
        with patch('sys.stdout', new=[]) as mock_stdout:
            burp(filename, contents)
>       assert mock_stdout.getvalue().strip() == ('Hello, world!' if filename == '-' else '')
E       AttributeError: 'list' object has no attribute 'getvalue'

pytutils/Test4DT_tests/test_pytutils_files_burp_1_test_valid_inputs.py:13: AttributeError
___________________ test_valid_inputs[--Hello, world!-None] ____________________

filename = '-', contents = 'Hello, world!', expected = None

    @pytest.mark.parametrize("filename, contents, expected", [
        ('example.txt', 'Hello, world!', None),
        ('-', 'Hello, world!', None),
    ])
    def test_valid_inputs(filename, contents, expected):
        with patch('sys.stdout', new=[]) as mock_stdout:
>           burp(filename, contents)

pytutils/Test4DT_tests/test_pytutils_files_burp_1_test_valid_inputs.py:12: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

filename = '-', contents = 'Hello, world!', mode = 'w', allow_stdout = True
expanduser = True, expandvars = True

    def burp(filename, contents, mode='w', allow_stdout=True, expanduser=True, expandvars=True):
        """
        Write `contents` to `filename`.
        """
        if filename == '-' and allow_stdout:
>           sys.stdout.write(contents)
E           AttributeError: 'list' object has no attribute 'write'

pytutils/pytutils/files.py:60: AttributeError
=============================== warnings summary ===============================
../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/nodeids: [Errno 13] Permission denied: '/dev/pytest-cache-files-w7jn2jii'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/lastfailed: [Errno 13] Permission denied: '/dev/pytest-cache-files-r1ceqohl'
    config.cache.set("cache/lastfailed", self.lastfailed)

../../../usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51
  /usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/stepwise: [Errno 13] Permission denied: '/dev/pytest-cache-files-2z40ub78'
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED ../../../dev/::test_valid_inputs[example.txt-Hello, world!-None] - Att...
FAILED ../../../dev/::test_valid_inputs[--Hello, world!-None] - AttributeErro...
======================== 2 failed, 3 warnings in 0.08s =========================
"""