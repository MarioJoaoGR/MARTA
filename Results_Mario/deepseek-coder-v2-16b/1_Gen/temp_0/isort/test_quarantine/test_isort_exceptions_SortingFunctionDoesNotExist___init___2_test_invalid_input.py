
import pytest
from sorting_module import SortingFunctionDoesNotExist

def test_invalid_input():
    sort_order = 'unknown'
    available_sort_orders = ['ascending', 'descending']
    
    with pytest.raises(SortingFunctionDoesNotExist) as exc_info:
        raise SortingFunctionDoesNotExist(sort_order, available_sort_orders)
    
    assert str(exc_info.value) == f"Specified sort_order of {sort_order} does not exist. Available sort_orders: {'ascending,descending'}."

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_exceptions_SortingFunctionDoesNotExist___init___2_test_invalid_input
isort/Test4DT_tests/test_isort_exceptions_SortingFunctionDoesNotExist___init___2_test_invalid_input.py:3:0: E0401: Unable to import 'sorting_module' (import-error)


"""