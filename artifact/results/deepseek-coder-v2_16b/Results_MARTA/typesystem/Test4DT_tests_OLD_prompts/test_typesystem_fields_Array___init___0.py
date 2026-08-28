
import pytest
from typesystem.fields import Array, Field

# Test 1: Valid initialization with multiple fields

# Test 2: Invalid initialization with incorrect item type
def test_invalid_item_type():
    field1 = Field()
    invalid_field = "not a Field"
    with pytest.raises(AssertionError):
        Array(items=[field1, invalid_field], additional_items=False, min_items=2, max_items=None, unique_items=True)

# Test 3: Invalid initialization with incorrect additional_items type
def test_invalid_additional_items_type():
    field1 = Field()
    with pytest.raises(AssertionError):
        Array(items=[field1], additional_items="not a bool", min_items=2, max_items=None, unique_items=True)

# Test 4: Invalid initialization with incorrect min_items type
def test_invalid_min_items_type():
    field1 = Field()
    with pytest.raises(AssertionError):
        Array(items=[field1], additional_items=False, min_items="not an int", max_items=None, unique_items=True)

# Test 5: Invalid initialization with incorrect max_items type
def test_invalid_max_items_type():
    field1 = Field()
    with pytest.raises(AssertionError):
        Array(items=[field1], additional_items=False, min_items=2, max_items="not an int", unique_items=True)

# Test 6: Invalid initialization with incorrect unique_items type
def test_invalid_unique_items_type():
    field1 = Field()
    with pytest.raises(AssertionError):
        Array(items=[field1], additional_items=False, min_items=2, max_items=None, unique_items="not a bool")