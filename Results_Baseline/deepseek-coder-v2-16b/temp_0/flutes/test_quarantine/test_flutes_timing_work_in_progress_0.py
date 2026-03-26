
import pytest
from flutes.timing import work_in_progress
import time
import pickle

# Test case for decorating a function with a custom description
def test_work_in_progress_decorator():
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)
    
    begin_time = time.time()
    try:
        obj = load_file("/path/to/some/file")  # This will trigger the decorator and print a message
    except FileNotFoundError:
        pytest.fail("File not found error occurred unexpectedly.")
    end_time = time.time()
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

flutes/Test4DT_tests/test_flutes_timing_work_in_progress_0.py F          [100%]

=================================== FAILURES ===================================
_______________________ test_work_in_progress_decorator ________________________

    def test_work_in_progress_decorator():
        @work_in_progress("Loading file")
        def load_file(path):
            with open(path, "rb") as f:
                return pickle.load(f)
    
        begin_time = time.time()
        try:
>           obj = load_file("/path/to/some/file")  # This will trigger the decorator and print a message

flutes/Test4DT_tests/test_flutes_timing_work_in_progress_0.py:16: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/usr/local/lib/python3.11/contextlib.py:81: in inner
    return func(*args, **kwds)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

path = '/path/to/some/file'

    @work_in_progress("Loading file")
    def load_file(path):
>       with open(path, "rb") as f:
E       FileNotFoundError: [Errno 2] No such file or directory: '/path/to/some/file'

flutes/Test4DT_tests/test_flutes_timing_work_in_progress_0.py:11: FileNotFoundError

During handling of the above exception, another exception occurred:

    def test_work_in_progress_decorator():
        @work_in_progress("Loading file")
        def load_file(path):
            with open(path, "rb") as f:
                return pickle.load(f)
    
        begin_time = time.time()
        try:
            obj = load_file("/path/to/some/file")  # This will trigger the decorator and print a message
        except FileNotFoundError:
>           pytest.fail("File not found error occurred unexpectedly.")
E           Failed: File not found error occurred unexpectedly.

flutes/Test4DT_tests/test_flutes_timing_work_in_progress_0.py:18: Failed
----------------------------- Captured stdout call -----------------------------
Loading file... 
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_timing_work_in_progress_0.py::test_work_in_progress_decorator
============================== 1 failed in 0.10s ===============================
"""