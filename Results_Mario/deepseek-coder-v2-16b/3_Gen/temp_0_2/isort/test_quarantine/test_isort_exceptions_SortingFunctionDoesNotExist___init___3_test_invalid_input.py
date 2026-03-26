 Here's a pytest function that tests the `SortingFunctionDoesNotExist` exception when an invalid sort order is provided:

```python
import pytest
from sorting_function import SortingFunctionDoesNotExist

def test_invalid_input():
    with pytest.raises(SortingFunctionDoesNotExist) as excinfo:
        raise SortingFunctionDoesNotExist("invalid_sort", ["bubble_sort", "quick_sort"])
    
    assert str(excinfo.value) == "Specified sort_order of invalid_sort does not exist. Available sort_orders: bubble_sort,quick_sort."
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_exceptions_SortingFunctionDoesNotExist___init___3_test_invalid_input
isort/Test4DT_tests/test_isort_exceptions_SortingFunctionDoesNotExist___init___3_test_invalid_input.py:1:1: E0001: Parsing failed: 'unexpected indent (Test4DT_tests.test_isort_exceptions_SortingFunctionDoesNotExist___init___3_test_invalid_input, line 1)' (syntax-error)


"""