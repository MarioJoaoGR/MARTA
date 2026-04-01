
import io
from flutes.io import _ReverseReadlineFile

def reverse_gen():
    yield "!dlroW ,olleH"  # This is the reversed line for demonstration purposes

# Example file-like object
example_file = io.StringIO("Hello, World!\n")

# Generator function that yields characters in reverse order
def reverse_lines_generator():
    yield "!dlroW ,olleH"  # This is the reversed line for demonstration purposes

with _ReverseReadlineFile(example_file, reverse_lines_generator()) as rrlf:
    assert rrlf.readline() == '!dlroW ,olleH'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items

--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
============================ no tests ran in 0.07s =============================
"""