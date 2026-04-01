
import io
import sys
import pytest
from pytutils.debug import interact
import inspect

def test_edge_case_none():
    def example_function():
        x = 10
        y = 20
        interact(banner=None)

    # Capture the output of the function call to ensure no banner is displayed
    captured_stdout = io.StringIO()
    captured_stderr = io.StringIO()
    sys.stdout, sys.stderr = captured_stdout, captured_stderr

    with pytest.raises(RuntimeError):
        example_function()

    # Check if the banner is not displayed by checking the output
    assert "banner" not in captured_stdout.getvalue().lower(), f"Expected no banner but got: {captured_stdout.getvalue()}"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

pytutils/Test4DT_tests/test_pytutils_debug_interact_0_test_edge_case_none.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_edge_case_none ______________________________

    def test_edge_case_none():
        def example_function():
            x = 10
            y = 20
            interact(banner=None)
    
        # Capture the output of the function call to ensure no banner is displayed
        captured_stdout = io.StringIO()
        captured_stderr = io.StringIO()
        sys.stdout, sys.stderr = captured_stdout, captured_stderr
    
        with pytest.raises(RuntimeError):
>           example_function()

pytutils/Test4DT_tests/test_pytutils_debug_interact_0_test_edge_case_none.py:20: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
pytutils/Test4DT_tests/test_pytutils_debug_interact_0_test_edge_case_none.py:12: in example_function
    interact(banner=None)
pytutils/pytutils/debug.py:18: in interact
    code.interact(local=calling_vars, banner=banner)
/usr/local/lib/python3.11/code.py:301: in interact
    console.interact(banner, exitmsg)
/usr/local/lib/python3.11/code.py:227: in interact
    line = self.raw_input(prompt)
/usr/local/lib/python3.11/code.py:274: in raw_input
    return input(prompt)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <_pytest.capture.DontReadFromInput object at 0x7f662b911510>, size = -1

    def read(self, size: int = -1) -> str:
>       raise OSError(
            "pytest: reading from stdin while output is captured!  Consider using `-s`."
        )
E       OSError: pytest: reading from stdin while output is captured!  Consider using `-s`.

/usr/local/lib/python3.11/site-packages/_pytest/capture.py:208: OSError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_debug_interact_0_test_edge_case_none.py::test_edge_case_none
============================== 1 failed in 0.07s ===============================
"""