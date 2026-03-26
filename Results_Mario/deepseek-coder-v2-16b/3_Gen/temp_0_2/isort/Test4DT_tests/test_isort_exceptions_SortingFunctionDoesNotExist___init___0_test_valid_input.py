
# Import the SortingFunctionDoesNotExist class from isort.exceptions
from isort.exceptions import SortingFunctionDoesNotExist

def test_valid_input():
    try:
        # Raise an instance of SortingFunctionDoesNotExist with a valid sort order and available sort orders
        raise SortingFunctionDoesNotExist("bubble_sort", ["bubble_sort", "quick_sort"])
    except SortingFunctionDoesNotExist as e:
        # Assert that the exception message is correct
        assert str(e) == "Specified sort_order of bubble_sort does not exist. Available sort_orders: bubble_sort,quick_sort."
