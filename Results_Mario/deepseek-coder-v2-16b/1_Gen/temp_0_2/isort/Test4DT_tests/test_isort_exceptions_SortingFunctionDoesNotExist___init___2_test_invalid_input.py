
from isort.exceptions import SortingFunctionDoesNotExist
import pytest

def test_invalid_input():
    sort_order = "invalid_order"
    available_sort_orders = ["ascending", "descending"]
    
    with pytest.raises(SortingFunctionDoesNotExist) as excinfo:
        raise SortingFunctionDoesNotExist(sort_order, available_sort_orders)
    
    assert str(excinfo.value) == f"Specified sort_order of {sort_order} does not exist. Available sort_orders: {','.join(available_sort_orders)}."
