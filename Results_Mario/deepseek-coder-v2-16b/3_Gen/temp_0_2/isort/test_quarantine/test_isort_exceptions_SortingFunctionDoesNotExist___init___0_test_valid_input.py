
import pytest
from sorting_function import SortingFunctionDoesNotExist

def test_valid_input():
    sort_order = 'bubble_sort'
    available_sort_orders = ['bubble_sort', 'quick_sort']
    
    with pytest.raises(SortingFunctionDoesNotExist) as exc_info:
        raise SortingFunctionDoesNotExist(sort_order, available_sort_orders)
    
    assert str(exc_info.value) == f"Specified sort_order of {sort_order} does not exist. Available sort_orders: bubble_sort,quick_sort."

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_exceptions_SortingFunctionDoesNotExist___init___0_test_valid_input
isort/Test4DT_tests/test_isort_exceptions_SortingFunctionDoesNotExist___init___0_test_valid_input.py:3:0: E0401: Unable to import 'sorting_function' (import-error)


"""