
import io
import pytest
from flutes.io import _ReverseReadlineFile

def test_error_case():
    with pytest.raises(StopIteration):
        fp = io.StringIO("Hello, world!\n")
        gen = (line[::-1] for line in fp)  # Generator function to reverse lines
        rev_readline = _ReverseReadlineFile(fp, gen)
    
        # Read the first line and it should raise StopIteration if there's no more data
        next(rev_readline.readline())

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_io__ReverseReadlineFile___exit___0_test_error_case.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_error_case ________________________________

    def test_error_case():
        with pytest.raises(StopIteration):
            fp = io.StringIO("Hello, world!\n")
            gen = (line[::-1] for line in fp)  # Generator function to reverse lines
            rev_readline = _ReverseReadlineFile(fp, gen)
    
            # Read the first line and it should raise StopIteration if there's no more data
>           next(rev_readline.readline())
E           TypeError: 'str' object is not an iterator

flutes/Test4DT_tests/test_flutes_io__ReverseReadlineFile___exit___0_test_error_case.py:13: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_io__ReverseReadlineFile___exit___0_test_error_case.py::test_error_case
============================== 1 failed in 0.10s ===============================
"""