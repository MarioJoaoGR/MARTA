
import pytest
from flutes.io import _ReverseReadlineFile
from io import StringIO

def reverse_gen(fp):
    lines = []
    for line in fp:
        lines.append(line)
    for i in range(len(lines) - 1, -1, -1):
        yield lines[i]

@pytest.fixture
def setup_reverse_readline():
    data = "line1\nline2\nline3\n"
    fp = StringIO(data)
    rev_file = _ReverseReadlineFile(fp, reverse_gen)
    return rev_file

def test_edge_case(setup_reverse_readline):
    rev_file = setup_reverse_readline
    expected_output = ["line3", "line2", "line1"]
    actual_output = [line.strip() for line in rev_file]
    assert actual_output == expected_output

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

flutes/Test4DT_tests/test_flutes_io__ReverseReadlineFile___iter___0_test_edge_case.py F [100%]

=================================== FAILURES ===================================
________________________________ test_edge_case ________________________________

setup_reverse_readline = <flutes.io._ReverseReadlineFile object at 0x7f6b1905cfd0>

    def test_edge_case(setup_reverse_readline):
        rev_file = setup_reverse_readline
        expected_output = ["line3", "line2", "line1"]
>       actual_output = [line.strip() for line in rev_file]

flutes/Test4DT_tests/test_flutes_io__ReverseReadlineFile___iter___0_test_edge_case.py:23: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
flutes/Test4DT_tests/test_flutes_io__ReverseReadlineFile___iter___0_test_edge_case.py:23: in <listcomp>
    actual_output = [line.strip() for line in rev_file]
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <flutes.io._ReverseReadlineFile object at 0x7f6b1905cfd0>

    def __next__(self):
>       return next(self.gen) + '\n'
E       TypeError: 'function' object is not an iterator

flutes/flutes/io.py:223: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_io__ReverseReadlineFile___iter___0_test_edge_case.py::test_edge_case
============================== 1 failed in 0.09s ===============================
"""