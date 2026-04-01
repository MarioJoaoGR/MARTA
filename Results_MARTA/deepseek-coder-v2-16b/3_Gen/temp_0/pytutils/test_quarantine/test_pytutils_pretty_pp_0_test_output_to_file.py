
import pytest
from pytutils.pretty import pp
import sys
import io

# Mocking Pygments and its components since they might not be available in the test environment
class MockPygments:
    @staticmethod
    def highlight(arg, lexer, formatter, outfile):
        outfile.write(str(arg))

sys.modules['pygments'] = MockPygments

# Mocking six since it might not be available in the test environment
import sys
import six
if not hasattr(sys, 'six'):
    sys.six = six
else:
    sys.six = sys.modules['six']

def test_output_to_file():
    # Capture stdout to verify the output
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    # Test with a dictionary and an outfile specified
    pp({'key': 'value'}, outfile='test_output.txt')
    
    # Reset stdout to its original value
    sys.stdout = sys.__stdout__
    
    # Verify the output file content
    with open('test_output.txt', 'r') as f:
        assert f.read() == "{'key': 'value'}\n"

# Run the test case
if __name__ == "__main__":
    pytest.main([__file__, "-v", "--capture=sys"])

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
_____________________________ test_output_to_file ______________________________

    def test_output_to_file():
        # Capture stdout to verify the output
        captured_output = io.StringIO()
        sys.stdout = captured_output
    
        # Test with a dictionary and an outfile specified
        pp({'key': 'value'}, outfile='test_output.txt')
    
        # Reset stdout to its original value
        sys.stdout = sys.__stdout__
    
        # Verify the output file content
        with open('test_output.txt', 'r') as f:
>           assert f.read() == "{'key': 'value'}\n"
E           assert '\x1b[38;2;24...2m}\x1b[39m\n' == "{'key': 'value'}\n"
E             
E             - {'key': 'value'}
E             + [38;2;248;248;242m{[39m[38;2;230;219;116m'[39m[38;2;230;219;116mkey[39m[38;2;230;219;116m'[39m[38;2;248;248;242m:[39m[38;2;248;248;242m [39m[38;2;230;219;116m'[39m[38;2;230;219;116mvalue[39m[38;2;230;219;116m'[39m[38;2;248;248;242m}[39m

pytutils/Test4DT_tests/test_pytutils_pretty_pp_0_test_output_to_file.py:36: AssertionError
=============================== warnings summary ===============================
../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/nodeids: [Errno 13] Permission denied: '/dev/pytest-cache-files-mf1bx1c3'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/lastfailed: [Errno 13] Permission denied: '/dev/pytest-cache-files-bw0p_6og'
    config.cache.set("cache/lastfailed", self.lastfailed)

../../../usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51
  /usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/stepwise: [Errno 13] Permission denied: '/dev/pytest-cache-files-gk5rmpog'
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED ../../../dev/::test_output_to_file - assert '\x1b[38;2;24...2m}\x1b[39...
======================== 1 failed, 3 warnings in 0.09s =========================
"""