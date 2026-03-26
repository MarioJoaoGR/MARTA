
import pytest
from pytutils.debug import interact
import inspect
import sys

@pytest.mark.parametrize("invalid_input", [None, 123, [], {}])
def test_invalid_inputs(invalid_input):
    with pytest.raises(TypeError):
        interact(banner=invalid_input)

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

../../../dev FFFF                                                        [100%]

=================================== FAILURES ===================================
__________________________ test_invalid_inputs[None] ___________________________

invalid_input = None

    @pytest.mark.parametrize("invalid_input", [None, 123, [], {}])
    def test_invalid_inputs(invalid_input):
        with pytest.raises(TypeError):
>           interact(banner=invalid_input)

pytutils/Test4DT_tests/test_pytutils_debug_interact_4_test_invalid_inputs.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
pytutils/pytutils/debug.py:18: in interact
    code.interact(local=calling_vars, banner=banner)
/usr/local/lib/python3.11/code.py:301: in interact
    console.interact(banner, exitmsg)
/usr/local/lib/python3.11/code.py:227: in interact
    line = self.raw_input(prompt)
/usr/local/lib/python3.11/code.py:274: in raw_input
    return input(prompt)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <_pytest.capture.DontReadFromInput object at 0x7f4f51e30990>, size = -1

    def read(self, size: int = -1) -> str:
>       raise OSError(
            "pytest: reading from stdin while output is captured!  Consider using `-s`."
        )
E       OSError: pytest: reading from stdin while output is captured!  Consider using `-s`.

/usr/local/lib/python3.11/site-packages/_pytest/capture.py:208: OSError
----------------------------- Captured stdout call -----------------------------
>>> 
----------------------------- Captured stderr call -----------------------------
Python 3.11.15 (main, Mar 16 2026, 23:07:56) [GCC 14.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
___________________________ test_invalid_inputs[123] ___________________________

invalid_input = 123

    @pytest.mark.parametrize("invalid_input", [None, 123, [], {}])
    def test_invalid_inputs(invalid_input):
        with pytest.raises(TypeError):
>           interact(banner=invalid_input)

pytutils/Test4DT_tests/test_pytutils_debug_interact_4_test_invalid_inputs.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
pytutils/pytutils/debug.py:18: in interact
    code.interact(local=calling_vars, banner=banner)
/usr/local/lib/python3.11/code.py:301: in interact
    console.interact(banner, exitmsg)
/usr/local/lib/python3.11/code.py:227: in interact
    line = self.raw_input(prompt)
/usr/local/lib/python3.11/code.py:274: in raw_input
    return input(prompt)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <_pytest.capture.DontReadFromInput object at 0x7f4f51e30990>, size = -1

    def read(self, size: int = -1) -> str:
>       raise OSError(
            "pytest: reading from stdin while output is captured!  Consider using `-s`."
        )
E       OSError: pytest: reading from stdin while output is captured!  Consider using `-s`.

/usr/local/lib/python3.11/site-packages/_pytest/capture.py:208: OSError
----------------------------- Captured stdout call -----------------------------
>>> 
----------------------------- Captured stderr call -----------------------------
123
_____________________ test_invalid_inputs[invalid_input2] ______________________

invalid_input = []

    @pytest.mark.parametrize("invalid_input", [None, 123, [], {}])
    def test_invalid_inputs(invalid_input):
        with pytest.raises(TypeError):
>           interact(banner=invalid_input)

pytutils/Test4DT_tests/test_pytutils_debug_interact_4_test_invalid_inputs.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
pytutils/pytutils/debug.py:18: in interact
    code.interact(local=calling_vars, banner=banner)
/usr/local/lib/python3.11/code.py:301: in interact
    console.interact(banner, exitmsg)
/usr/local/lib/python3.11/code.py:227: in interact
    line = self.raw_input(prompt)
/usr/local/lib/python3.11/code.py:274: in raw_input
    return input(prompt)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <_pytest.capture.DontReadFromInput object at 0x7f4f51e30990>, size = -1

    def read(self, size: int = -1) -> str:
>       raise OSError(
            "pytest: reading from stdin while output is captured!  Consider using `-s`."
        )
E       OSError: pytest: reading from stdin while output is captured!  Consider using `-s`.

/usr/local/lib/python3.11/site-packages/_pytest/capture.py:208: OSError
----------------------------- Captured stdout call -----------------------------
>>> 
_____________________ test_invalid_inputs[invalid_input3] ______________________

invalid_input = {}

    @pytest.mark.parametrize("invalid_input", [None, 123, [], {}])
    def test_invalid_inputs(invalid_input):
        with pytest.raises(TypeError):
>           interact(banner=invalid_input)

pytutils/Test4DT_tests/test_pytutils_debug_interact_4_test_invalid_inputs.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
pytutils/pytutils/debug.py:18: in interact
    code.interact(local=calling_vars, banner=banner)
/usr/local/lib/python3.11/code.py:301: in interact
    console.interact(banner, exitmsg)
/usr/local/lib/python3.11/code.py:227: in interact
    line = self.raw_input(prompt)
/usr/local/lib/python3.11/code.py:274: in raw_input
    return input(prompt)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <_pytest.capture.DontReadFromInput object at 0x7f4f51e30990>, size = -1

    def read(self, size: int = -1) -> str:
>       raise OSError(
            "pytest: reading from stdin while output is captured!  Consider using `-s`."
        )
E       OSError: pytest: reading from stdin while output is captured!  Consider using `-s`.

/usr/local/lib/python3.11/site-packages/_pytest/capture.py:208: OSError
----------------------------- Captured stdout call -----------------------------
>>> 
=============================== warnings summary ===============================
../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/nodeids: [Errno 13] Permission denied: '/dev/pytest-cache-files-y7rz5hwa'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/lastfailed: [Errno 13] Permission denied: '/dev/pytest-cache-files-ugs9ey7v'
    config.cache.set("cache/lastfailed", self.lastfailed)

../../../usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51
  /usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/stepwise: [Errno 13] Permission denied: '/dev/pytest-cache-files-zdsqe1po'
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED ../../../dev/::test_invalid_inputs[None] - OSError: pytest: reading fr...
FAILED ../../../dev/::test_invalid_inputs[123] - OSError: pytest: reading fro...
FAILED ../../../dev/::test_invalid_inputs[invalid_input2] - OSError: pytest: ...
FAILED ../../../dev/::test_invalid_inputs[invalid_input3] - OSError: pytest: ...
======================== 4 failed, 3 warnings in 0.15s =========================
"""