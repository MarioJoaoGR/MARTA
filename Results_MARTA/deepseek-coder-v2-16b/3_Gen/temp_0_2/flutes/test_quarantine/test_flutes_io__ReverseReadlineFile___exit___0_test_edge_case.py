
import pytest
from flutes.io import _ReverseReadlineFile

def test_reverse_readline_none_input():
    with pytest.raises(ValueError):
        reverse_readline = _ReverseReadlineFile(None, None)
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

flutes/Test4DT_tests/test_flutes_io__ReverseReadlineFile___exit___0_test_edge_case.py F [100%]

=================================== FAILURES ===================================
_______________________ test_reverse_readline_none_input _______________________

    def test_reverse_readline_none_input():
        with pytest.raises(ValueError):
            reverse_readline = _ReverseReadlineFile(None, None)
>           reverse_readline.readline()

flutes/Test4DT_tests/test_flutes_io__ReverseReadlineFile___exit___0_test_edge_case.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <flutes.io._ReverseReadlineFile object at 0x7efdc4f6e990>

    def readline(self):
>       return next(self.gen)
E       TypeError: 'NoneType' object is not an iterator

flutes/flutes/io.py:232: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_io__ReverseReadlineFile___exit___0_test_edge_case.py::test_reverse_readline_none_input
============================== 1 failed in 0.10s ===============================
"""