
import pytest
from flutes.iterator import LazyList

def test_valid_input():
    my_list = [1, 2, 3, 4, 5]
    lazy_list = LazyList(my_list)
    
    # Check the length of the list after iteration
    assert len(lazy_list.list) == 0
    
    # Iterate through the lazy list and check elements
    for i in range(len(my_list)):
        assert next(iter(lazy_list)) == my_list[i]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_iterator_LazyList___init___0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        my_list = [1, 2, 3, 4, 5]
        lazy_list = LazyList(my_list)
    
        # Check the length of the list after iteration
        assert len(lazy_list.list) == 0
    
        # Iterate through the lazy list and check elements
        for i in range(len(my_list)):
>           assert next(iter(lazy_list)) == my_list[i]
E           assert 1 == 2
E            +  where 1 = next(<flutes.iterator.LazyList.LazyListIterator object at 0x7fbd25501710>)
E            +    where <flutes.iterator.LazyList.LazyListIterator object at 0x7fbd25501710> = iter(<flutes.iterator.LazyList object at 0x7fbd255016d0>)

flutes/Test4DT_tests/test_flutes_iterator_LazyList___init___0_test_valid_input.py:14: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_LazyList___init___0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.10s ===============================
"""