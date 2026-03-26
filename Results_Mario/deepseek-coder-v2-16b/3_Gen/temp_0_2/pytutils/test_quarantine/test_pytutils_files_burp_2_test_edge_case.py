
import os
import tempfile
from pytutils.files import burp
import pytest

def test_edge_case():
    # Create a temporary file to simulate writing to a file
    with tempfile.NamedTemporaryFile(delete=False, mode='w+') as tmp_file:
        filename = tmp_file.name
        contents = "Test content"
        
        # Call the burp function with the edge case scenario (filename is '-')
        burp('-', contents)
        
        # Read the file to check if it contains the expected content
        tmp_file.seek(0)
        written_content = tmp_file.read()
        
        # Assert that the written content matches the expected content
        assert written_content == "Test content"
        
    # Ensure the temporary file is removed after the test
    os.remove(filename)

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

pytutils/Test4DT_tests/test_pytutils_files_burp_2_test_edge_case.py F    [100%]

=================================== FAILURES ===================================
________________________________ test_edge_case ________________________________

    def test_edge_case():
        # Create a temporary file to simulate writing to a file
        with tempfile.NamedTemporaryFile(delete=False, mode='w+') as tmp_file:
            filename = tmp_file.name
            contents = "Test content"
    
            # Call the burp function with the edge case scenario (filename is '-')
            burp('-', contents)
    
            # Read the file to check if it contains the expected content
            tmp_file.seek(0)
            written_content = tmp_file.read()
    
            # Assert that the written content matches the expected content
>           assert written_content == "Test content"
E           AssertionError: assert '' == 'Test content'
E             
E             - Test content

pytutils/Test4DT_tests/test_pytutils_files_burp_2_test_edge_case.py:21: AssertionError
----------------------------- Captured stdout call -----------------------------
Test content
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_files_burp_2_test_edge_case.py::test_edge_case
============================== 1 failed in 0.07s ===============================
"""