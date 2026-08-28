
import pytest
from typesystem.fields import Array, Field
from typesystem.base import ValidationError

# Test initialization with specific constraints

# Test validation of an array with specific constraints
def test_validation_of_array():
    field1 = Field()
    field2 = Field()
    array_with_constraints = Array(
        items=[field1, field2],  # List of Field objects
        additional_items=False,   # No additional items allowed
        min_items=2,              # At least 2 items required
        max_items=None,           # Unlimited maximum number of items
        unique_items=True         # All items must be unique
    )
    with pytest.raises(ValidationError):
        array_with_constraints.validate([field1])  # Should raise ValidationError as there are less than min_items

# Test serialization of an array with specific constraints