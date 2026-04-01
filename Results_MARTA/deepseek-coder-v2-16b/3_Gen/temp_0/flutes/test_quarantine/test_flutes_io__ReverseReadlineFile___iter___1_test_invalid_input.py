
import pytest
from io import StringIO
from flutes.io import _ReverseReadlineFile

def test_invalid_input():
    # Create a mock file-like object with invalid data type (should raise TypeError)
    fp = "not a file-like object"
    
    # Define a generator function to produce lines in reverse order
    def gen():
        yield 'Line 3'
        yield 'Line 2'
        yield 'Line 1'
    
    with pytest.raises(TypeError):
        _ReverseReadlineFile(fp, gen)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_io__ReverseReadlineFile___iter___1_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        # Create a mock file-like object with invalid data type (should raise TypeError)
        fp = "not a file-like object"
    
        # Define a generator function to produce lines in reverse order
        def gen():
            yield 'Line 3'
            yield 'Line 2'
            yield 'Line 1'
    
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

flutes/Test4DT_tests/test_flutes_io__ReverseReadlineFile___iter___1_test_invalid_input.py:16: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_io__ReverseReadlineFile___iter___1_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.11s ===============================
"""