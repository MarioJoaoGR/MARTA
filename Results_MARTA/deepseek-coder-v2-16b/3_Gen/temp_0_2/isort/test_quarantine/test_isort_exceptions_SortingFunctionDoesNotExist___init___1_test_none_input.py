 Here's a pytest function that tests the `SortingFunctionDoesNotExist` exception when the input is `None`:

```python
import pytest
from sorting_function import SortingFunctionDoesNotExist

def test_none_input():
    sort_order = None
    available_sort_orders = ["bubble_sort", "quick_sort"]
    
    with pytest.raises(SortingFunctionDoesNotExist) as excinfo:
        raise SortingFunctionDoesNotExist(sort_order, available_sort_orders)
    
    assert str(excinfo.value) == f"Specified sort_order of {sort_order} does not exist. Available sort_orders: bubble_sort,quick_sort."
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_exceptions_SortingFunctionDoesNotExist___init___1_test_none_input
isort/Test4DT_tests/test_isort_exceptions_SortingFunctionDoesNotExist___init___1_test_none_input.py:1:1: E0001: Parsing failed: 'unexpected indent (Test4DT_tests.test_isort_exceptions_SortingFunctionDoesNotExist___init___1_test_none_input, line 1)' (syntax-error)


"""