
import pytest
from pytutils.debug import interact
import inspect
import code

def test_valid_input():
    def test():
        x = 10
        y = 20
        interact()
    
    # Capture the output of the function to ensure it runs without errors
    captured_output = []
    def capture_output(func):
        def wrapper(*args, **kwargs):
            import sys
            from io import StringIO
            old_stdout = sys.stdout
            new_stdout = StringIO()
            sys.stdout = new_stdout
            func(*args, **kwargs)
            captured_output.append(new_stdout.getvalue())
            sys.stdout = old_stdout
        return wrapper
    
    @capture_output
    def run_test():
        test()
    
    run_test()
    
    # Check that the output contains the expected banner and prompt
    assert "(debug shell)" in captured_output[0]

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
        def test():
            x = 10
            y = 20
            interact()
    
        # Capture the output of the function to ensure it runs without errors
        captured_output = []
        def capture_output(func):
            def wrapper(*args, **kwargs):
                import sys
                from io import StringIO
                old_stdout = sys.stdout
                new_stdout = StringIO()
                sys.stdout = new_stdout
                func(*args, **kwargs)
                captured_output.append(new_stdout.getvalue())
                sys.stdout = old_stdout
            return wrapper
    
        @capture_output
        def run_test():
            test()
    
>       run_test()

pytutils/Test4DT_tests/test_pytutils_debug_interact_0_test_valid_input.py:31: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
pytutils/Test4DT_tests/test_pytutils_debug_interact_0_test_valid_input.py:22: in wrapper
    func(*args, **kwargs)
pytutils/Test4DT_tests/test_pytutils_debug_interact_0_test_valid_input.py:29: in run_test
    test()
pytutils/Test4DT_tests/test_pytutils_debug_interact_0_test_valid_input.py:11: in test
    interact()
pytutils/pytutils/debug.py:18: in interact
    code.interact(local=calling_vars, banner=banner)
/usr/local/lib/python3.11/code.py:301: in interact
    console.interact(banner, exitmsg)
/usr/local/lib/python3.11/code.py:227: in interact
    line = self.raw_input(prompt)
/usr/local/lib/python3.11/code.py:274: in raw_input
    return input(prompt)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <_pytest.capture.DontReadFromInput object at 0x7fbfd63080d0>, size = -1

    def read(self, size: int = -1) -> str:
>       raise OSError(
            "pytest: reading from stdin while output is captured!  Consider using `-s`."
        )
E       OSError: pytest: reading from stdin while output is captured!  Consider using `-s`.

/usr/local/lib/python3.11/site-packages/_pytest/capture.py:208: OSError
----------------------------- Captured stderr call -----------------------------
(debug shell)
=============================== warnings summary ===============================
../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/nodeids: [Errno 13] Permission denied: '/dev/pytest-cache-files-uir9nb_3'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/lastfailed: [Errno 13] Permission denied: '/dev/pytest-cache-files-o2vekx_r'
    config.cache.set("cache/lastfailed", self.lastfailed)

../../../usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51
  /usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/stepwise: [Errno 13] Permission denied: '/dev/pytest-cache-files-k1mqp_h7'
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED ../../../dev/::test_valid_input - OSError: pytest: reading from stdin ...
======================== 1 failed, 3 warnings in 0.11s =========================
"""