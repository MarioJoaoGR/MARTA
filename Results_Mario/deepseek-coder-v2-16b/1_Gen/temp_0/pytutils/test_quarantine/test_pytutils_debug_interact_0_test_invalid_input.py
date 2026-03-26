
import io
import sys
import pytest
import inspect
from pytutils.debug import interact

def test_invalid_input():
    # Create a mock buffer to capture stdout and stderr
    captured_output = io.StringIO()
    sys.stdout = captured_output
    sys.stderr = captured_output
    
    with pytest.raises(TypeError):
        interact(banner=123)
    
    # Check that the error message is as expected
    assert "TypeError" in captured_output.getvalue()

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

pytutils/Test4DT_tests/test_pytutils_debug_interact_0_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        # Create a mock buffer to capture stdout and stderr
        captured_output = io.StringIO()
        sys.stdout = captured_output
        sys.stderr = captured_output
    
        with pytest.raises(TypeError):
>           interact(banner=123)

pytutils/Test4DT_tests/test_pytutils_debug_interact_0_test_invalid_input.py:15: 
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

self = <_pytest.capture.DontReadFromInput object at 0x7f012a725fd0>, size = -1

    def read(self, size: int = -1) -> str:
>       raise OSError(
            "pytest: reading from stdin while output is captured!  Consider using `-s`."
        )
E       OSError: pytest: reading from stdin while output is captured!  Consider using `-s`.

/usr/local/lib/python3.11/site-packages/_pytest/capture.py:208: OSError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_debug_interact_0_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.07s ===============================
"""