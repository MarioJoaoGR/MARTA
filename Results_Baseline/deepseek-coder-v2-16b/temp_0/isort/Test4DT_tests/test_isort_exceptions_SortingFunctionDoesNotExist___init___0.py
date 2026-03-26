# Module: isort.exceptions
import pytest

from isort.exceptions import SortingFunctionDoesNotExist


# Test Case 1: Raising the exception directly and catching it to print a user-friendly error message.
def test_exception_direct_raise():
    with pytest.raises(SortingFunctionDoesNotExist) as exc_info:
        raise SortingFunctionDoesNotExist("invalid_order", ["ascending", "descending"])
    
    assert str(exc_info.value) == "Specified sort_order of invalid_order does not exist. Available sort_orders: ascending,descending."

# Test Case 2: Simulating fetching data that requires sorting in a function where an unsupported sort order triggers the exception.
def test_exception_in_function(capsys):
    def get_data(sort_order):
        if sort_order == "ascending":
            return sorted([3, 1, 4, 1, 5, 9])
        elif sort_order == "descending":
            return sorted([3, 1, 4, 1, 5, 9], reverse=True)
        else:
            raise SortingFunctionDoesNotExist(sort_order, ["ascending", "descending"])
    
    try:
        get_data("invalid_order")
    except SortingFunctionDoesNotExist as e:
        captured = capsys.readouterr()
        assert str(e) == "Specified sort_order of invalid_order does not exist. Available sort_orders: ascending,descending."

# Test Case 3: Checking the exception message when no available sort orders are provided.
def test_exception_no_available_sort_orders():
    with pytest.raises(SortingFunctionDoesNotExist) as exc_info:
        raise SortingFunctionDoesNotExist("invalid_order", [])
    
    assert str(exc_info.value) == "Specified sort_order of invalid_order does not exist. Available sort_orders: ."

# Test Case 4: Checking the exception message when an empty string is provided as a sort order.
def test_exception_empty_sort_order():
    with pytest.raises(SortingFunctionDoesNotExist) as exc_info:
        raise SortingFunctionDoesNotExist("", ["ascending", "descending"])
    
    assert str(exc_info.value) == "Specified sort_order of  does not exist. Available sort_orders: ascending,descending."
