
import pytest
from flutes.iterator import LazyList

def test_valid_case():
    lazy_list = LazyList([1, 2, 3, 4])
    assert len(lazy_list) == 4

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

flutes/Test4DT_tests/test_flutes_iterator_LazyList___len___0_test_valid_case.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_case ________________________________

    def test_valid_case():
        lazy_list = LazyList([1, 2, 3, 4])
>       assert len(lazy_list) == 4

flutes/Test4DT_tests/test_flutes_iterator_LazyList___len___0_test_valid_case.py:7: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <flutes.iterator.LazyList object at 0x7f31ef8ea390>

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
FAILED flutes/Test4DT_tests/test_flutes_iterator_LazyList___len___0_test_valid_case.py::test_valid_case
============================== 1 failed in 0.09s ===============================
"""