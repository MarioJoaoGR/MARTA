
import pytest
from sorting_module import SortingFunctionDoesNotExist

def test_empty_list_input():
    sort_order = 'bubble_sort'
    available_sort_orders = []
    
    with pytest.raises(SortingFunctionDoesNotExist) as excinfo:
        raise SortingFunctionDoesNotExist(sort_order, available_sort_orders)
    
    assert str(excinfo.value) == f"Specified sort_order of {sort_order} does not exist. Available sort_orders: ."

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_exceptions_SortingFunctionDoesNotExist___init___2_test_empty_list_input
isort/Test4DT_tests/test_isort_exceptions_SortingFunctionDoesNotExist___init___2_test_empty_list_input.py:3:0: E0401: Unable to import 'sorting_module' (import-error)


"""