
from isort.exceptions import SortingFunctionDoesNotExist
import pytest

def test_none_input():
    with pytest.raises(SortingFunctionDoesNotExist) as excinfo:
        raise SortingFunctionDoesNotExist("invalid_sort", ["bubble_sort", "quick_sort"])
    
    assert str(excinfo.value) == "Specified sort_order of invalid_sort does not exist. Available sort_orders: bubble_sort,quick_sort."
