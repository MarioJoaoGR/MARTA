
import pytest
from io import StringIO
from flutes.io import _ReverseReadlineFile

# Import the function from the module
from flutes.io import _ReverseReadlineFile

def test_reverse_readline():
    # Define a generator function that yields reversed lines
    def reverse_lines_generator():
        yield "!dlrow ,olleH"  # This is the reversed line for demonstration purposes

    # Create a file-like object from a string
    fp = StringIO("Hello, world!\n")

    # Instantiate the _ReverseReadlineFile class with the file-like object and generator function
    rev_readline = _ReverseReadlineFile(fp, reverse_lines_generator())

    # Read a line from the reversed file-like object
    assert rev_readline.readline() == "!dlrow ,olleH\n"

def test_reverse_readline_empty():
    # Define an empty generator function
    def empty_generator():
        yield from []

    # Create an empty file-like object
    fp = StringIO("")

    # Instantiate the _ReverseReadlineFile class with the empty file-like object and empty generator
    rev_readline = _ReverseReadlineFile(fp, empty_generator())

    # Read a line from the reversed file-like object should return None or an appropriate value for EOF
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

flutes/Test4DT_tests/test_flutes_io__ReverseReadlineFile___init___0.py F [ 50%]
.                                                                        [100%]

=================================== FAILURES ===================================
____________________________ test_reverse_readline _____________________________

    def test_reverse_readline():
        # Define a generator function that yields reversed lines
        def reverse_lines_generator():
            yield "!dlrow ,olleH"  # This is the reversed line for demonstration purposes
    
        # Create a file-like object from a string
        fp = StringIO("Hello, world!\n")
    
        # Instantiate the _ReverseReadlineFile class with the file-like object and generator function
        rev_readline = _ReverseReadlineFile(fp, reverse_lines_generator())
    
        # Read a line from the reversed file-like object
>       assert rev_readline.readline() == "!dlrow ,olleH\n"
E       AssertionError: assert '!dlrow ,olleH' == '!dlrow ,olleH\n'
E         
E         - !dlrow ,olleH
E         ?              -
E         + !dlrow ,olleH

flutes/Test4DT_tests/test_flutes_io__ReverseReadlineFile___init___0.py:21: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_io__ReverseReadlineFile___init___0.py::test_reverse_readline
========================= 1 failed, 1 passed in 0.09s ==========================
"""