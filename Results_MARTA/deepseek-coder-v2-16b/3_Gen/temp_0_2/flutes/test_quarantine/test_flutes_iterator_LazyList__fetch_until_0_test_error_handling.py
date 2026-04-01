
import pytest
from flutes.iterator import LazyList

def test_error_handling():
    with pytest.raises(IndexError):
        lazy_list = LazyList([1, 2, 3])
        next(lazy_list)  # This will raise StopIteration after yielding 1

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

flutes/Test4DT_tests/test_flutes_iterator_LazyList__fetch_until_0_test_error_handling.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_error_handling ______________________________

    def test_error_handling():
        with pytest.raises(IndexError):
            lazy_list = LazyList([1, 2, 3])
>           next(lazy_list)  # This will raise StopIteration after yielding 1
E           TypeError: 'LazyList' object is not an iterator

flutes/Test4DT_tests/test_flutes_iterator_LazyList__fetch_until_0_test_error_handling.py:8: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_LazyList__fetch_until_0_test_error_handling.py::test_error_handling
============================== 1 failed in 0.09s ===============================
"""