
import pytest
from isort.exceptions import SortingFunctionDoesNotExist

def test_edge_case():
    sort_order = "invalid_order"
    available_sort_orders = ["ascending", "descending"]
    
    with pytest.raises(SortingFunctionDoesNotExist) as exc_info:
        raise SortingFunctionDoesNotExist(sort_order, available_sort_orders)
    
    assert str(exc_info.value) == f"Specified sort_order of {sort_order} does not exist. Available sort_orders: {','.join(available_sort_orders)}."
