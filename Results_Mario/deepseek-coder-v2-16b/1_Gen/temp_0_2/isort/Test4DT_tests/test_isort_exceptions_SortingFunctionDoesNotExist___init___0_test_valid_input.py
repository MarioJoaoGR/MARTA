
from isort.exceptions import SortingFunctionDoesNotExist
import pytest

def test_valid_input():
    with pytest.raises(SortingFunctionDoesNotExist) as excinfo:
        raise SortingFunctionDoesNotExist("invalid_order", ["ascending", "descending"])
    
    assert str(excinfo.value) == "Specified sort_order of invalid_order does not exist. Available sort_orders: ascending,descending."
