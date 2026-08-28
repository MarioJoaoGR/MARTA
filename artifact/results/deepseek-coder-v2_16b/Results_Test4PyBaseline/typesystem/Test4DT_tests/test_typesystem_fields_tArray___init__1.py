
import pytest
from typesystem import Array, Field

# Helper function to create a list of Field instances for items
def create_field_list(length):
    return [Field() for _ in range(length)]

# Test cases for the __init__ method of the Array class
@pytest.mark.parametrize("items, min_items, max_items, unique_items, expected_min_items, expected_max_items", [
    (create_field_list(2), None, None, True, 2, float('inf')),
    (create_field_list(3), None, None, False, 3, float('inf')),
    (create_field_list(2), 2, None, True, 2, float('inf')),
    (create_field_list(1), None, None, True, 1, float('inf')),
    (create_field_list(5), None, 5, True, 5, 5),
    (create_field_list(2), None, None, False, 2, float('inf'))
])
def test_array_init(items, min_items, max_items, unique_items, expected_min_items, expected_max_items):
    my_array = Array(items=items, min_items=min_items, max_items=max_items, unique_items=unique_items)
    
    assert isinstance(my_array.items, list) and all(isinstance(i, Field) for i in my_array.items), "Items must be a sequence of Field instances"
    assert my_array.min_items == expected_min_items, f"Expected min_items to be {expected_min_items}, but got {my_array.min_items}"