
import io
from unittest.mock import patch
from pytutils.pretty import pp  # Assuming the module is named 'pytutils.pretty'

def test_valid_input():
    # Prepare some data to be pretty-printed
    data = {'key': 'value'}
    
    # Capture the output using StringIO
    captured_output = io.StringIO()
    
    with patch('sys.stdout', new=captured_output):
        pp(data)
    
    # Get the content of the captured output
    printed_output = captured_output.getvalue().strip()
    
    # Assert that the output is as expected
    assert printed_output == "{'key': 'value'}"

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
        # Prepare some data to be pretty-printed
        data = {'key': 'value'}
    
        # Capture the output using StringIO
        captured_output = io.StringIO()
    
        with patch('sys.stdout', new=captured_output):
            pp(data)
    
        # Get the content of the captured output
        printed_output = captured_output.getvalue().strip()
    
        # Assert that the output is as expected
>       assert printed_output == "{'key': 'value'}"
E       assert '' == "{'key': 'value'}"
E         
E         - {'key': 'value'}

pytutils/Test4DT_tests/test_pytutils_pretty_pp_0_test_valid_input.py:20: AssertionError
----------------------------- Captured stdout call -----------------------------
[38;2;248;248;242m{[39m[38;2;230;219;116m'[39m[38;2;230;219;116mkey[39m[38;2;230;219;116m'[39m[38;2;248;248;242m:[39m[38;2;248;248;242m [39m[38;2;230;219;116m'[39m[38;2;230;219;116mvalue[39m[38;2;230;219;116m'[39m[38;2;248;248;242m}[39m
=============================== warnings summary ===============================
../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/nodeids: [Errno 13] Permission denied: '/dev/pytest-cache-files-4_6k72c2'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/lastfailed: [Errno 13] Permission denied: '/dev/pytest-cache-files-7kx1z0ux'
    config.cache.set("cache/lastfailed", self.lastfailed)

../../../usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51
  /usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/stepwise: [Errno 13] Permission denied: '/dev/pytest-cache-files-z3tiguqy'
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED ../../../dev/::test_valid_input - assert '' == "{'key': 'value'}"
======================== 1 failed, 3 warnings in 0.08s =========================
"""