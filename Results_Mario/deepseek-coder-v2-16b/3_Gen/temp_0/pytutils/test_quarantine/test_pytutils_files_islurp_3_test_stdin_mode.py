
import pytest
import io
import sys
import os
import functools
from pytutils.files import islurp

@pytest.mark.parametrize("filename, allow_stdin", [("-", True)])
def test_stdin_mode(monkeypatch, filename, allow_stdin):
    # Mock stdin input
    mock_input = "Mocked standard input data"
    monkeypatch.setattr('sys.stdin', io.StringIO(mock_input))

    # Call the function
    gen = islurp(filename, allow_stdin=allow_stdin)

    # Collect output from generator
    collected_output = []
    for line in gen:
        collected_output.append(line)

    # Check if the collected output matches the mocked input
    assert ''.join(collected_output) == mock_input

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
___________________________ test_stdin_mode[--True] ____________________________

monkeypatch = <_pytest.monkeypatch.MonkeyPatch object at 0x7fdce9ae8390>
filename = '-', allow_stdin = True

    @pytest.mark.parametrize("filename, allow_stdin", [("-", True)])
    def test_stdin_mode(monkeypatch, filename, allow_stdin):
        # Mock stdin input
        mock_input = "Mocked standard input data"
        monkeypatch.setattr('sys.stdin', io.StringIO(mock_input))
    
        # Call the function
        gen = islurp(filename, allow_stdin=allow_stdin)
    
        # Collect output from generator
        collected_output = []
>       for line in gen:

pytutils/Test4DT_tests/test_pytutils_files_islurp_3_test_stdin_mode.py:20: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

filename = '-', mode = 'r', iter_by = 0, allow_stdin = True, expanduser = True
expandvars = True

    def islurp(filename, mode='r', iter_by=LINEMODE, allow_stdin=True, expanduser=True, expandvars=True):
        """
        Read [expanded] `filename` and yield each (line | chunk).
    
        :param str filename: File path
        :param str mode: Use this mode to open `filename`, ala `r` for text (default), `rb` for binary, etc.
        :param int iter_by: Iterate by this many bytes at a time. Default is by line.
        :param bool allow_stdin: If Truthy and filename is `-`, read from `sys.stdin`.
        :param bool expanduser: If Truthy, expand `~` in `filename`
        :param bool expandvars: If Truthy, expand env vars in `filename`
        """
        if iter_by == 'LINEMODE':
            iter_by = LINEMODE
    
        fh = None
        try:
            if filename == '-' and allow_stdin:
                fh = sys.stdin
            else:
                if expanduser:
                    filename = os.path.expanduser(filename)
                if expandvars:
                    filename = os.path.expandvars(filename)
    
                fh = open(filename, mode)
                fh_next = fh.readline if iter_by == LINEMODE else functools.partial(fh.read, iter_by)
    
            while True:
>               buf = fh_next()
E               UnboundLocalError: cannot access local variable 'fh_next' where it is not associated with a value

pytutils/pytutils/files.py:40: UnboundLocalError
=============================== warnings summary ===============================
../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/nodeids: [Errno 13] Permission denied: '/dev/pytest-cache-files-f53ywzgd'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/lastfailed: [Errno 13] Permission denied: '/dev/pytest-cache-files-fqi7z8fa'
    config.cache.set("cache/lastfailed", self.lastfailed)

../../../usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51
  /usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/stepwise: [Errno 13] Permission denied: '/dev/pytest-cache-files-6e57xe2j'
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED ../../../dev/::test_stdin_mode[--True] - UnboundLocalError: cannot acc...
======================== 1 failed, 3 warnings in 0.09s =========================
"""