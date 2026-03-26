
import pytest
from flutes.io import _ReverseReadlineFile
from io import StringIO

def test_invalid_input():
    data = "Line 1\nLine 2\nLine 3\n"
    gen = iter(data.splitlines())
    rev_readline = _ReverseReadlineFile(StringIO(data), gen)
    
    with pytest.raises(StopIteration):
        next(rev_readline)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_io__ReverseReadlineFile___next___1_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        data = "Line 1\nLine 2\nLine 3\n"
        gen = iter(data.splitlines())
        rev_readline = _ReverseReadlineFile(StringIO(data), gen)
    
>       with pytest.raises(StopIteration):
E       Failed: DID NOT RAISE <class 'StopIteration'>

flutes/Test4DT_tests/test_flutes_io__ReverseReadlineFile___next___1_test_invalid_input.py:11: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_io__ReverseReadlineFile___next___1_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.10s ===============================
"""