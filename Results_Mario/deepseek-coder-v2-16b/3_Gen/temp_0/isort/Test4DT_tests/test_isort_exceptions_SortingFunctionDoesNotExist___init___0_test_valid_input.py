
import pytest
from isort.exceptions import SortingFunctionDoesNotExist

def test_valid_input():
    sort_order = 'ascending'
    available_sort_orders = ['ascending', 'descending']
    
    with pytest.raises(SortingFunctionDoesNotExist) as exc_info:
        raise SortingFunctionDoesNotExist(sort_order, available_sort_orders)
        
    assert str(exc_info.value) == "Specified sort_order of ascending does not exist. Available sort_orders: ascending,descending."
