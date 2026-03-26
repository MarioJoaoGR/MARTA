
import pytest
from sorting_module import SortingFunctionDoesNotExist

def test_valid_input():
    sort_order = 'ascending'
    available_orders = ['ascending', 'descending']
    
    # Test that no exception is raised when the sort order exists in the list of available orders
    try:
        raise SortingFunctionDoesNotExist(sort_order, available_orders)
    except SortingFunctionDoesNotExist as e:
        pytest.fail(f"Unexpected SortingFunctionDoesNotExist exception: {e}")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_exceptions_SortingFunctionDoesNotExist___init___0_test_valid_input
isort/Test4DT_tests/test_isort_exceptions_SortingFunctionDoesNotExist___init___0_test_valid_input.py:3:0: E0401: Unable to import 'sorting_module' (import-error)


"""