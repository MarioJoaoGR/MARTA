
import pytest
from flutes.iterator import Range

def test_edge_case_none():
    r = Range()
    with pytest.raises(ValueError):
        list(r)

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

flutes/Test4DT_tests/test_flutes_iterator_Range___iter___3_test_edge_case_none.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_edge_case_none ______________________________

    def test_edge_case_none():
>       r = Range()

flutes/Test4DT_tests/test_flutes_iterator_Range___iter___3_test_edge_case_none.py:6: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <flutes.iterator.Range object at 0x7ff7b29f58d0>, args = ()

    def __init__(self, *args):
        if len(args) == 0 or len(args) > 3:
>           raise ValueError("Range should be called the same way as the builtin `range`")
E           ValueError: Range should be called the same way as the builtin `range`

flutes/flutes/iterator.py:318: ValueError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_Range___iter___3_test_edge_case_none.py::test_edge_case_none
============================== 1 failed in 0.10s ===============================
"""