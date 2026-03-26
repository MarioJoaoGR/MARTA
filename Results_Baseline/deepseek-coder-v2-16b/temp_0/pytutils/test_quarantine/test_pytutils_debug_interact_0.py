
import pytest
import inspect
import code
from pytutils.debug import interact

def test_default_usage():
    """Test the default usage of the interact function."""
    try:
        interact()
    except Exception as e:
        pytest.fail(f"Unexpected error occurred: {e}")

def test_custom_banner():
    """Test the custom banner usage of the interact function."""
    try:
        interact(banner='Welcome to the Debug Shell')
    except Exception as e:
        pytest.fail(f"Unexpected error occurred: {e}")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

pytutils/Test4DT_tests/test_pytutils_debug_interact_0.py FF              [100%]

=================================== FAILURES ===================================
______________________________ test_default_usage ______________________________

    def test_default_usage():
        """Test the default usage of the interact function."""
        try:
>           interact()

pytutils/Test4DT_tests/test_pytutils_debug_interact_0.py:10: 
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

self = <_pytest.capture.DontReadFromInput object at 0x7f9a5a127a90>, size = -1

    def read(self, size: int = -1) -> str:
>       raise OSError(
            "pytest: reading from stdin while output is captured!  Consider using `-s`."
        )
E       OSError: pytest: reading from stdin while output is captured!  Consider using `-s`.

/usr/local/lib/python3.11/site-packages/_pytest/capture.py:208: OSError

During handling of the above exception, another exception occurred:

    def test_default_usage():
        """Test the default usage of the interact function."""
        try:
            interact()
        except Exception as e:
>           pytest.fail(f"Unexpected error occurred: {e}")
E           Failed: Unexpected error occurred: pytest: reading from stdin while output is captured!  Consider using `-s`.

pytutils/Test4DT_tests/test_pytutils_debug_interact_0.py:12: Failed
----------------------------- Captured stdout call -----------------------------
>>> 
----------------------------- Captured stderr call -----------------------------
(debug shell)
______________________________ test_custom_banner ______________________________

    def test_custom_banner():
        """Test the custom banner usage of the interact function."""
        try:
>           interact(banner='Welcome to the Debug Shell')

pytutils/Test4DT_tests/test_pytutils_debug_interact_0.py:17: 
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

self = <_pytest.capture.DontReadFromInput object at 0x7f9a5a127a90>, size = -1

    def read(self, size: int = -1) -> str:
>       raise OSError(
            "pytest: reading from stdin while output is captured!  Consider using `-s`."
        )
E       OSError: pytest: reading from stdin while output is captured!  Consider using `-s`.

/usr/local/lib/python3.11/site-packages/_pytest/capture.py:208: OSError

During handling of the above exception, another exception occurred:

    def test_custom_banner():
        """Test the custom banner usage of the interact function."""
        try:
            interact(banner='Welcome to the Debug Shell')
        except Exception as e:
>           pytest.fail(f"Unexpected error occurred: {e}")
E           Failed: Unexpected error occurred: pytest: reading from stdin while output is captured!  Consider using `-s`.

pytutils/Test4DT_tests/test_pytutils_debug_interact_0.py:19: Failed
----------------------------- Captured stdout call -----------------------------
>>> 
----------------------------- Captured stderr call -----------------------------
Welcome to the Debug Shell
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_debug_interact_0.py::test_default_usage
FAILED pytutils/Test4DT_tests/test_pytutils_debug_interact_0.py::test_custom_banner
============================== 2 failed in 0.09s ===============================
"""