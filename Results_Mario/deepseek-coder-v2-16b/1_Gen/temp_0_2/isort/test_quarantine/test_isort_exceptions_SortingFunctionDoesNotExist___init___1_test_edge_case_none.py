 Here's the pytest function for testing the edge case where `sort_order` is `None`:

```python
import pytest
from sorting_module import SortingFunctionDoesNotExist

def test_edge_case_none():
    sort_order = None
    available_orders = ['ascending', 'descending']
    
    with pytest.raises(SortingFunctionDoesNotExist) as exc_info:
        raise SortingFunctionDoesNotExist(sort_order, available_orders)
    
    assert str(exc_info.value) == "Specified sort_order of None does not exist. Available sort_orders: ascending,descending."
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_exceptions_SortingFunctionDoesNotExist___init___1_test_edge_case_none
isort/Test4DT_tests/test_isort_exceptions_SortingFunctionDoesNotExist___init___1_test_edge_case_none.py:1:1: E0001: Parsing failed: 'unexpected indent (Test4DT_tests.test_isort_exceptions_SortingFunctionDoesNotExist___init___1_test_edge_case_none, line 1)' (syntax-error)


"""