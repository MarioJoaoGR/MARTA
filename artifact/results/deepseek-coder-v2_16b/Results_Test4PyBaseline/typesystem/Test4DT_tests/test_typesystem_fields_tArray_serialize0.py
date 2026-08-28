
import pytest
from typesystem import Array, Field

# Test Case 1: Creating an Array instance with specific constraints
def test_array_creation_with_specific_constraints():
    items = [Field(), Field()]
    array = Array(items=items, min_items=2, max_items=5, unique_items=True)
    
    assert isinstance(array.items, list), "Items must be a list."
    assert len(array.items) == 2, "The list should have exactly 2 items."
    assert array.min_items == 2, "Minimum number of items should be 2."
    assert array.max_items == 5, "Maximum number of items should be 5."
    assert array.unique_items is True, "Items must be unique."

# Test Case 2: Creating an Array instance without specifying constraints explicitly
def test_array_creation_without_constraints():
    items = [Field(), Field()]
    array = Array(items=items)
    
    assert isinstance(array.items, list), "Items must be a list."
    assert len(array.items) == 2, "The default minimum number of items should be 2."
    assert array.min_items == 2, "Minimum number of items should be 2."
    assert array.max_items == 2, "Maximum number of items should match the length of provided items if not specified."