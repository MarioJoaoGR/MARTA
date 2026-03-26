
import pytest
from flutes.iterator import LazyList

def test_lazylist():
    # Test creating a LazyList from an iterable
    lazy_list = LazyList([1, 2, 3, 4])
    
    # Check that the list is populated lazily
    assert len(lazy_list) == 0  # Initially empty
    
    # Access elements to trigger fetching
    for i in range(len(lazy_list)):
        lazy_list._fetch_until(i)
    
    # Check that the list has been populated correctly
    assert len(lazy_list.list) == 4
    assert lazy_list[0] == 1
    assert lazy_list[1] == 2
    assert lazy_list[2] == 3
    assert lazy_list[3] == 4

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_iterator_LazyList__fetch_until_1_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
________________________________ test_lazylist _________________________________

    def test_lazylist():
        # Test creating a LazyList from an iterable
        lazy_list = LazyList([1, 2, 3, 4])
    
        # Check that the list is populated lazily
>       assert len(lazy_list) == 0  # Initially empty

flutes/Test4DT_tests/test_flutes_iterator_LazyList__fetch_until_1_test_edge_cases.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <flutes.iterator.LazyList object at 0x7f1d3bdabe10>

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
FAILED flutes/Test4DT_tests/test_flutes_iterator_LazyList__fetch_until_1_test_edge_cases.py::test_lazylist
============================== 1 failed in 0.11s ===============================
"""