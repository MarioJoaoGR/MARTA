
import io
import os
from flutes.io import _ReverseReadlineFile

def test_edge_case():
    fp = io.StringIO("Line1\nLine2\nLine3\n")
    
    def gen():
        yield from reversed(list(fp))
    
    rev_file = _ReverseReadlineFile(fp, gen)
    
    assert next(rev_file.gen()) == "Line3\n"
    assert next(rev_file.gen()) == "Line2\n"
    assert next(rev_file.gen()) == "Line1\n"

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

flutes/Test4DT_tests/test_flutes_io__ReverseReadlineFile_generator_0_test_edge_case.py F [100%]

=================================== FAILURES ===================================
________________________________ test_edge_case ________________________________

    def test_edge_case():
        fp = io.StringIO("Line1\nLine2\nLine3\n")
    
        def gen():
            yield from reversed(list(fp))
    
        rev_file = _ReverseReadlineFile(fp, gen)
    
        assert next(rev_file.gen()) == "Line3\n"
>       assert next(rev_file.gen()) == "Line2\n"
E       StopIteration

flutes/Test4DT_tests/test_flutes_io__ReverseReadlineFile_generator_0_test_edge_case.py:15: StopIteration
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_io__ReverseReadlineFile_generator_0_test_edge_case.py::test_edge_case
============================== 1 failed in 0.09s ===============================
"""