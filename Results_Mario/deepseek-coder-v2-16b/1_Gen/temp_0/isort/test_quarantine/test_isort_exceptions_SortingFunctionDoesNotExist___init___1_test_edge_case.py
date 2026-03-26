
import pytest
from your_module import SortingFunctionDoesNotExist  # Replace 'your_module' with the actual module name where SortingFunctionDoesNotExist is defined

def test_edge_case():
    sort_order = None
    available_sort_orders = []
    
    with pytest.raises(SortingFunctionDoesNotExist) as exc_info:
        raise SortingFunctionDoesNotExist(sort_order, available_sort_orders)
    
    assert str(exc_info.value) == "Specified sort_order of None does not exist. Available sort_orders: ."

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_exceptions_SortingFunctionDoesNotExist___init___1_test_edge_case
isort/Test4DT_tests/test_isort_exceptions_SortingFunctionDoesNotExist___init___1_test_edge_case.py:3:0: E0401: Unable to import 'your_module' (import-error)


"""