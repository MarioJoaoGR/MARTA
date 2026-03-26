
import pytest
from flutes.io import _ReverseReadlineFile
import io

@pytest.fixture
def setup_reverse_readline():
    file_content = "Line1\nLine2\nLine3\n"
    fp = io.StringIO(file_content)
    gen = (line[::-1] for line in fp)  # Reversing each line read from the file
    reverse_readline = _ReverseReadlineFile(fp, gen)
    return reverse_readline

def test_edge_case(setup_reverse_readline):
    reverse_readline = setup_reverse_readline
    assert reverse_readline.readline() == "3Line\n"
    assert reverse_readline.readline() == "2Line\n"
    assert reverse_readline.readline() == "1Line\n"
    with pytest.raises(StopIteration):
        reverse_readline.readline()

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

flutes/Test4DT_tests/test_flutes_io__ReverseReadlineFile___exit___1_test_edge_case.py F [100%]

=================================== FAILURES ===================================
________________________________ test_edge_case ________________________________

setup_reverse_readline = <flutes.io._ReverseReadlineFile object at 0x7fe3f8b70d90>

    def test_edge_case(setup_reverse_readline):
        reverse_readline = setup_reverse_readline
>       assert reverse_readline.readline() == "3Line\n"
E       AssertionError: assert '\n1eniL' == '3Line\n'
E         
E         - 3Line
E         + 
E         + 1eniL

flutes/Test4DT_tests/test_flutes_io__ReverseReadlineFile___exit___1_test_edge_case.py:16: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_io__ReverseReadlineFile___exit___1_test_edge_case.py::test_edge_case
============================== 1 failed in 0.10s ===============================
"""