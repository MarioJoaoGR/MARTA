
import sys
import os
import contextlib
import pytest
from flutes.io import shut_up

def test_shut_up_decorator():
    @shut_up(stderr=True)
    def verbose_func():
        print("This should not be printed")
    
    with pytest.raises(IOError):  # Since output is suppressed, accessing sys.stdout should raise an error
        verbose_func()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_io_shut_up_1_test_edge_case.py F        [100%]

=================================== FAILURES ===================================
____________________________ test_shut_up_decorator ____________________________

    def test_shut_up_decorator():
        @shut_up(stderr=True)
        def verbose_func():
            print("This should not be printed")
    
>       with pytest.raises(IOError):  # Since output is suppressed, accessing sys.stdout should raise an error
E       Failed: DID NOT RAISE <class 'OSError'>

flutes/Test4DT_tests/test_flutes_io_shut_up_1_test_edge_case.py:13: Failed
----------------------------- Captured stdout call -----------------------------
This should not be printed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_io_shut_up_1_test_edge_case.py::test_shut_up_decorator
============================== 1 failed in 0.10s ===============================
"""