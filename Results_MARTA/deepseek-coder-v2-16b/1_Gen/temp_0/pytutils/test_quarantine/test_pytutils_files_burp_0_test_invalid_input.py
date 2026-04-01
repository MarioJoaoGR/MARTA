
import pytest
from pytutils.files import burp

def test_invalid_input():
    # Invalid filename (not a string)
    with pytest.raises(TypeError) as excinfo:
        burp(123, "test content")
    
    assert str(excinfo.value) == "__init__() missing 1 required positional argument: 'filename'", f"Unexpected error: {str(excinfo.value)}"

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

pytutils/Test4DT_tests/test_pytutils_files_burp_0_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        # Invalid filename (not a string)
        with pytest.raises(TypeError) as excinfo:
            burp(123, "test content")
    
>       assert str(excinfo.value) == "__init__() missing 1 required positional argument: 'filename'", f"Unexpected error: {str(excinfo.value)}"
E       AssertionError: Unexpected error: expected str, bytes or os.PathLike object, not int
E       assert 'expected str...ject, not int' == "__init__() m...t: 'filename'"
E         
E         - __init__() missing 1 required positional argument: 'filename'
E         + expected str, bytes or os.PathLike object, not int

pytutils/Test4DT_tests/test_pytutils_files_burp_0_test_invalid_input.py:10: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_files_burp_0_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.05s ===============================
"""