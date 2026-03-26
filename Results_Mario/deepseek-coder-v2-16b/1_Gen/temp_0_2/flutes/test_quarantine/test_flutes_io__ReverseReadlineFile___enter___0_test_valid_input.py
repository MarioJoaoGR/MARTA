
import io
from flutes.io import _ReverseReadlineFile

def test_valid_input():
    # Create a mock file-like object with some sample data
    fp = io.StringIO("Line1\nLine2\nLine3\n")

    # Define a generator function that reads lines from the file in reverse order
    def gen():
        yield from reversed(list(fp))

    # Initialize the _ReverseReadlineFile with the file-like object and generator
    rev_file = _ReverseReadlineFile(fp, gen)

    # Use the context manager to ensure resources are managed correctly
    with rev_file as rrlf:
        assert rrlf.readline().decode('utf-8') == "Line3\n"

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

flutes/Test4DT_tests/test_flutes_io__ReverseReadlineFile___enter___0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        # Create a mock file-like object with some sample data
        fp = io.StringIO("Line1\nLine2\nLine3\n")
    
        # Define a generator function that reads lines from the file in reverse order
        def gen():
            yield from reversed(list(fp))
    
        # Initialize the _ReverseReadlineFile with the file-like object and generator
        rev_file = _ReverseReadlineFile(fp, gen)
    
        # Use the context manager to ensure resources are managed correctly
        with rev_file as rrlf:
>           assert rrlf.readline().decode('utf-8') == "Line3\n"

flutes/Test4DT_tests/test_flutes_io__ReverseReadlineFile___enter___0_test_valid_input.py:18: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <flutes.io._ReverseReadlineFile object at 0x7fc13b4aead0>

    def readline(self):
>       return next(self.gen)
E       TypeError: 'function' object is not an iterator

flutes/flutes/io.py:232: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_io__ReverseReadlineFile___enter___0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.09s ===============================
"""