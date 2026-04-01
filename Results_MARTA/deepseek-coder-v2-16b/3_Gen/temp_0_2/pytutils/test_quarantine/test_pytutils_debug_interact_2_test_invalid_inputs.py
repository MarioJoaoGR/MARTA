
import pytest
from io import StringIO
import sys
import inspect
import pytutils.debug
from unittest.mock import patch

def test_invalid_inputs():
    # Capture stdout and stderr to avoid printing banner and invalid input error message
    captured_stdout = StringIO()
    captured_stderr = StringIO()
    sys.stdout = captured_stdout
    sys.stderr = captured_stderr
    
    with pytest.raises(TypeError):
        with patch('sys.stdin', StringIO()):  # Mock stdin to avoid actual input reading
            pytutils.debug.interact(banner=123)

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

pytutils/Test4DT_tests/test_pytutils_debug_interact_2_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        # Capture stdout and stderr to avoid printing banner and invalid input error message
        captured_stdout = StringIO()
        captured_stderr = StringIO()
        sys.stdout = captured_stdout
        sys.stderr = captured_stderr
    
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

pytutils/Test4DT_tests/test_pytutils_debug_interact_2_test_invalid_inputs.py:16: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_debug_interact_2_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.07s ===============================
"""