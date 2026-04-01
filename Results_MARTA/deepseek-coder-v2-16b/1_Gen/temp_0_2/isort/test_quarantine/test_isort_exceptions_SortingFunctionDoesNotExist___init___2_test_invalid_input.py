 Here's the pytest function for testing invalid sort order and valid available orders:

```python
import pytest
from isort.exceptions import SortingFunctionDoesNotExist

def test_invalid_input():
    sort_order = 'unknown'
    available_orders = ['ascending', 'descending']
    
    with pytest.raises(SortingFunctionDoesNotExist) as exc_info:
        raise SortingFunctionDoesNotExist(sort_order, available_orders)
    
    assert str(exc_info.value) == f"Specified sort_order of {sort_order} does not exist. Available sort_orders: {','.join(available_orders)}."
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_exceptions_SortingFunctionDoesNotExist___init___2_test_invalid_input
isort/Test4DT_tests/test_isort_exceptions_SortingFunctionDoesNotExist___init___2_test_invalid_input.py:1:1: E0001: Parsing failed: 'unexpected indent (Test4DT_tests.test_isort_exceptions_SortingFunctionDoesNotExist___init___2_test_invalid_input, line 1)' (syntax-error)


"""