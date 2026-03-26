
import pytest
import sys
import io
from pytutils.debug import interact
import inspect

def test_invalid_inputs():
    # Capture the output to avoid raising OSError due to stdin reading while output is captured
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    with pytest.raises(TypeError):
        interact(banner=12345)  # Banner is expected to be a string but an integer is provided
    
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

pytutils/Test4DT_tests/test_pytutils_debug_interact_3_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        # Capture the output to avoid raising OSError due to stdin reading while output is captured
        captured_output = io.StringIO()
        sys.stdout = captured_output
    
        with pytest.raises(TypeError):
>           interact(banner=12345)  # Banner is expected to be a string but an integer is provided

pytutils/Test4DT_tests/test_pytutils_debug_interact_3_test_invalid_inputs.py:14: 
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

self = <_pytest.capture.DontReadFromInput object at 0x7f509ef3e310>, size = -1

    def read(self, size: int = -1) -> str:
>       raise OSError(
            "pytest: reading from stdin while output is captured!  Consider using `-s`."
        )
E       OSError: pytest: reading from stdin while output is captured!  Consider using `-s`.

/usr/local/lib/python3.11/site-packages/_pytest/capture.py:208: OSError
----------------------------- Captured stderr call -----------------------------
12345
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_debug_interact_3_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.09s ===============================
"""