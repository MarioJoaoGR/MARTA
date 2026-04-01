
import os
import sys
from io import StringIO
from unittest.mock import patch
from pytutils.files import burp

def test_edge_cases():
    # Test writing to a file
    with patch('sys.stdout', new=StringIO()) as mock_stdout:
        burp('example.txt', 'Hello, world!')
        assert open('example.txt').read() == 'Hello, world!'
    
    # Test writing to stdout
    captured_output = StringIO()
    sys.stdout = captured_output
    burp('-', 'Hello, world!', allow_stdout=True)
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue().strip() == 'Hello, world!'
    
    # Test expanding user home directory and environment variables in the filename
    with patch('os.path.expanduser', return_value='~/expanded_example.txt') as mock_expanduser:
        with patch('os.path.expandvars', return_value='~/expanded_example.txt') as mock_expandvars:
            burp('~/example.txt', 'Hello, world!', expanduser=True, expandvars=True)
            assert open('~/expanded_example.txt').read() == 'Hello, world!'

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
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        # Test writing to a file
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            burp('example.txt', 'Hello, world!')
            assert open('example.txt').read() == 'Hello, world!'
    
        # Test writing to stdout
        captured_output = StringIO()
        sys.stdout = captured_output
        burp('-', 'Hello, world!', allow_stdout=True)
        sys.stdout = sys.__stdout__
        assert captured_output.getvalue().strip() == 'Hello, world!'
    
        # Test expanding user home directory and environment variables in the filename
        with patch('os.path.expanduser', return_value='~/expanded_example.txt') as mock_expanduser:
            with patch('os.path.expandvars', return_value='~/expanded_example.txt') as mock_expandvars:
>               burp('~/example.txt', 'Hello, world!', expanduser=True, expandvars=True)

pytutils/Test4DT_tests/test_pytutils_files_burp_1_test_edge_cases.py:24: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

filename = '~/expanded_example.txt', contents = 'Hello, world!', mode = 'w'
allow_stdout = True, expanduser = True, expandvars = True

    def burp(filename, contents, mode='w', allow_stdout=True, expanduser=True, expandvars=True):
        """
        Write `contents` to `filename`.
        """
        if filename == '-' and allow_stdout:
            sys.stdout.write(contents)
        else:
            if expanduser:
                filename = os.path.expanduser(filename)
            if expandvars:
                filename = os.path.expandvars(filename)
    
>           with open(filename, mode) as fh:
E           FileNotFoundError: [Errno 2] No such file or directory: '~/expanded_example.txt'

pytutils/pytutils/files.py:67: FileNotFoundError
=============================== warnings summary ===============================
../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/nodeids: [Errno 13] Permission denied: '/dev/pytest-cache-files-irrrbvby'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/lastfailed: [Errno 13] Permission denied: '/dev/pytest-cache-files-6f8pi3ce'
    config.cache.set("cache/lastfailed", self.lastfailed)

../../../usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51
  /usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/stepwise: [Errno 13] Permission denied: '/dev/pytest-cache-files-0cix5ju4'
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED ../../../dev/::test_edge_cases - FileNotFoundError: [Errno 2] No such ...
======================== 1 failed, 3 warnings in 0.08s =========================
"""