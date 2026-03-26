
import pytest
from flutes.iterator import LazyList

def test_valid_inputs():
    # Test with a list of integers
    lst = LazyList([1, 2, 3, 4])
    assert list(lst) == [1, 2, 3, 4]
    
    # Test accessing elements by index
    assert lst[0] == 1
    assert lst[2] == 3
    
    # Test with an iterator that yields values
    def custom_iter():
        yield 10
        yield 20
        yield 30
        yield 40
    
    lazy_list = LazyList(custom_iter())
    assert list(lazy_list) == [10, 20, 30, 40]
    assert lazy_list[0] == 10
    assert lazy_list[2] == 30
    
    # Test with a large dataset (this is more of a stress test to ensure the laziness works)
    large_lst = LazyList(range(1000))
    for i in range(500):  # Access only half of the list
        assert next(iter(large_lst)) == i

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_iterator_LazyList__fetch_until_2_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        # Test with a list of integers
        lst = LazyList([1, 2, 3, 4])
        assert list(lst) == [1, 2, 3, 4]
    
        # Test accessing elements by index
        assert lst[0] == 1
        assert lst[2] == 3
    
        # Test with an iterator that yields values
        def custom_iter():
            yield 10
            yield 20
            yield 30
            yield 40
    
        lazy_list = LazyList(custom_iter())
        assert list(lazy_list) == [10, 20, 30, 40]
        assert lazy_list[0] == 10
        assert lazy_list[2] == 30
    
        # Test with a large dataset (this is more of a stress test to ensure the laziness works)
        large_lst = LazyList(range(1000))
        for i in range(500):  # Access only half of the list
>           assert next(iter(large_lst)) == i
E           assert 0 == 1
E            +  where 0 = next(<flutes.iterator.LazyList.LazyListIterator object at 0x7fc203724910>)
E            +    where <flutes.iterator.LazyList.LazyListIterator object at 0x7fc203724910> = iter(<flutes.iterator.LazyList object at 0x7fc2037248d0>)

flutes/Test4DT_tests/test_flutes_iterator_LazyList__fetch_until_2_test_valid_inputs.py:29: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_LazyList__fetch_until_2_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.10s ===============================

"""