
import pytest
from pytutils.pretty import pp
import sys
import os

@pytest.mark.skipif(sys.platform == "win32", reason="Does not run on Windows")
def test_invalid_output():
    # Define an invalid file path that does not exist
    invalid_file_path = 'nonexistentfile.txt'
    
    # Use pytest to check if the function raises a FileNotFoundError when given an invalid file path
    with pytest.raises(FileNotFoundError):
        pp('invalid content', outfile=invalid_file_path)

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

pytutils/Test4DT_tests/test_pytutils_pretty_pp_2_test_invalid_output.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_output ______________________________

    @pytest.mark.skipif(sys.platform == "win32", reason="Does not run on Windows")
    def test_invalid_output():
        # Define an invalid file path that does not exist
        invalid_file_path = 'nonexistentfile.txt'
    
        # Use pytest to check if the function raises a FileNotFoundError when given an invalid file path
>       with pytest.raises(FileNotFoundError):
E       Failed: DID NOT RAISE <class 'FileNotFoundError'>

pytutils/Test4DT_tests/test_pytutils_pretty_pp_2_test_invalid_output.py:13: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_pretty_pp_2_test_invalid_output.py::test_invalid_output
============================== 1 failed in 0.11s ===============================
"""