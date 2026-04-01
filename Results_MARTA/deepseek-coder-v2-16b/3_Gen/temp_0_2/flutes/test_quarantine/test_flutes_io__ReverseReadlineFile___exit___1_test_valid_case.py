
import pytest
from flutes.io import _ReverseReadlineFile
import io

@pytest.fixture
def setup_reverse_readline():
    file_content = "Line1\nLine2\nLine3\n"
    fp = io.StringIO(file_content)
    gen = (line[::-1] for line in fp)  # Reversing each line read from the file
    return _ReverseReadlineFile(fp, gen)

def test_valid_case(setup_reverse_readline):
    reverse_readline = setup_reverse_readline
    while True:
        line = reverse_readline.readline()
        if not line:
            break
        print(line, end='')

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

flutes/Test4DT_tests/test_flutes_io__ReverseReadlineFile___exit___1_test_valid_case.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_case ________________________________

setup_reverse_readline = <flutes.io._ReverseReadlineFile object at 0x7f47f5fbc390>

    def test_valid_case(setup_reverse_readline):
        reverse_readline = setup_reverse_readline
        while True:
>           line = reverse_readline.readline()

flutes/Test4DT_tests/test_flutes_io__ReverseReadlineFile___exit___1_test_valid_case.py:16: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <flutes.io._ReverseReadlineFile object at 0x7f47f5fbc390>

    def readline(self):
>       return next(self.gen)
E       StopIteration

flutes/flutes/io.py:232: StopIteration
----------------------------- Captured stdout call -----------------------------

1eniL
2eniL
3eniL
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_io__ReverseReadlineFile___exit___1_test_valid_case.py::test_valid_case
============================== 1 failed in 0.11s ===============================
"""