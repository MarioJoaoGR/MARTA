
import pytest
import sys
import os
from pytutils.files import burp

@pytest.mark.parametrize("mode", ['r+'])
def test_error_handling(mode):
    with pytest.raises(IOError):
        # Test the function with a mode that should raise an IOError
        with pytest.raises(OSError):  # Expecting OSError instead of IOError
            burp('non_existent_file', 'contents', mode=mode)

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

pytutils/Test4DT_tests/test_pytutils_files_burp_1_test_error_handling.py F [100%]

=================================== FAILURES ===================================
___________________________ test_error_handling[r+] ____________________________

mode = 'r+'

    @pytest.mark.parametrize("mode", ['r+'])
    def test_error_handling(mode):
>       with pytest.raises(IOError):
E       Failed: DID NOT RAISE <class 'OSError'>

pytutils/Test4DT_tests/test_pytutils_files_burp_1_test_error_handling.py:9: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_files_burp_1_test_error_handling.py::test_error_handling[r+]
============================== 1 failed in 0.05s ===============================
"""