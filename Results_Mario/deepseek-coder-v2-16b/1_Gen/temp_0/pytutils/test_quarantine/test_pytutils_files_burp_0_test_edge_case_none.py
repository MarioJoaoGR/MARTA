
import pytest
from pytutils.files import burp
import sys

def test_edge_case_none():
    # Test when filename is '-' and allow_stdout is True
    with pytest.raises(TypeError):  # Since we are not actually writing to a file, this should raise a TypeError
        burp('-', 'Hello, world!', allow_stdout=True)

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

pytutils/Test4DT_tests/test_pytutils_files_burp_0_test_edge_case_none.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_edge_case_none ______________________________

    def test_edge_case_none():
        # Test when filename is '-' and allow_stdout is True
>       with pytest.raises(TypeError):  # Since we are not actually writing to a file, this should raise a TypeError
E       Failed: DID NOT RAISE <class 'TypeError'>

pytutils/Test4DT_tests/test_pytutils_files_burp_0_test_edge_case_none.py:8: Failed
----------------------------- Captured stdout call -----------------------------
Hello, world!
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_files_burp_0_test_edge_case_none.py::test_edge_case_none
============================== 1 failed in 0.05s ===============================
"""