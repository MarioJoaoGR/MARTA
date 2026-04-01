
import pytest
from flutes.iterator import LazyList

def test_edge_cases():
    lazy_list = LazyList([1, 2, 3, 4])
    
    # Check initial length before any elements are accessed
    assert len(lazy_list) == 0

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

flutes/Test4DT_tests/test_flutes_iterator_LazyList___len___1_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        lazy_list = LazyList([1, 2, 3, 4])
    
        # Check initial length before any elements are accessed
>       assert len(lazy_list) == 0

flutes/Test4DT_tests/test_flutes_iterator_LazyList___len___1_test_edge_cases.py:9: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <flutes.iterator.LazyList object at 0x7f47b4a3b1d0>

    def __len__(self):
        if self.exhausted:
            return len(self.list)
        else:
>           raise TypeError("__len__ is not available before the iterable is depleted")
E           TypeError: __len__ is not available before the iterable is depleted

flutes/flutes/iterator.py:292: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_LazyList___len___1_test_edge_cases.py::test_edge_cases
============================== 1 failed in 0.11s ===============================
"""