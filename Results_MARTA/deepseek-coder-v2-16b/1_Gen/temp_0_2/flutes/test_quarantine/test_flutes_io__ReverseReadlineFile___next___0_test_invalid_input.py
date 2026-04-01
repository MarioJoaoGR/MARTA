
import pytest
from flutes.io import _ReverseReadlineFile
from io import StringIO

def test_invalid_input():
    # Test with non-file-like object for 'fp'
    fp = "not a file-like object"
    gen = (line for line in ["Line1", "Line2", "Line3"])
    
    with pytest.raises(TypeError):
        _ReverseReadlineFile(fp, gen)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_io__ReverseReadlineFile___next___0_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        # Test with non-file-like object for 'fp'
        fp = "not a file-like object"
        gen = (line for line in ["Line1", "Line2", "Line3"])
    
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

flutes/Test4DT_tests/test_flutes_io__ReverseReadlineFile___next___0_test_invalid_input.py:11: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_io__ReverseReadlineFile___next___0_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.09s ===============================
"""