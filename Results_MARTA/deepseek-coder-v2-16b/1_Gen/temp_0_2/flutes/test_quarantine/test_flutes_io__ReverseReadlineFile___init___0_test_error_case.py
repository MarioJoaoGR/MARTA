
import io
from flutes.io import _ReverseReadlineFile

# Create a mock file-like object with some sample data
fp = io.StringIO("Line1\nLine2\nLine3\n")

# Define a generator function that reads lines from the file in reverse order
def gen():
    yield from reversed(list(fp))

# Initialize the _ReverseReadlineFile with the file-like object and generator
rev_file = _ReverseReadlineFile(fp, gen)

# Now you can read lines from the file in reverse order using standard file methods like readline()
print(rev_file.readline())  # Output: "Line3\n"
print(rev_file.readline())  # Output: "Line2\n"
print(rev_file.readline())  # Output: "Line1\n"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_ ERROR collecting Test4DT_tests/test_flutes_io__ReverseReadlineFile___init___0_test_error_case.py _
flutes/Test4DT_tests/test_flutes_io__ReverseReadlineFile___init___0_test_error_case.py:16: in <module>
    print(rev_file.readline())  # Output: "Line3\n"
flutes/flutes/io.py:232: in readline
    return next(self.gen)
E   TypeError: 'function' object is not an iterator
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR flutes/Test4DT_tests/test_flutes_io__ReverseReadlineFile___init___0_test_error_case.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.17s ===============================
"""