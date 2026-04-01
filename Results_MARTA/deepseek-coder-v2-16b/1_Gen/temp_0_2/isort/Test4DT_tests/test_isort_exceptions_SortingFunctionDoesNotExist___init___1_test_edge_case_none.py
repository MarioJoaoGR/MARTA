
from isort.exceptions import SortingFunctionDoesNotExist
import pytest

def test_edge_case_none():
    sort_order = None
    available_sort_orders = ["ascending", "descending"]
    
    with pytest.raises(SortingFunctionDoesNotExist) as excinfo:
        raise SortingFunctionDoesNotExist(sort_order, available_sort_orders)
    
    assert str(excinfo.value) == "Specified sort_order of None does not exist. Available sort_orders: ascending,descending."
