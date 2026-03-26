# Module: isort.exceptions
import pytest

from isort.exceptions import SortingFunctionDoesNotExist


# Test Case 1: Raising the exception with a non-existent sort order
def test_raising_exception():
    with pytest.raises(SortingFunctionDoesNotExist) as exc_info:
        raise SortingFunctionDoesNotExist("invalid_order", ["ascending", "descending"])
    
    assert str(exc_info.value) == "Specified sort_order of invalid_order does not exist. Available sort_orders: ascending,descending."

# Test Case 2: Handling the exception with a print statement
def test_handling_exception():
    try:
        raise SortingFunctionDoesNotExist("invalid_order", ["ascending", "descending"])
    except SortingFunctionDoesNotExist as e:
        assert str(e) == "Specified sort_order of invalid_order does not exist. Available sort_orders: ascending,descending."

# Test Case 3: Handling the exception with a formatted print statement
def test_formatted_handling_exception():
    try:
        raise SortingFunctionDoesNotExist("invalid_order", ["ascending", "descending"])
    except SortingFunctionDoesNotExist as e:
        assert str(e) == "Specified sort_order of invalid_order does not exist. Available sort_orders: ascending,descending."
