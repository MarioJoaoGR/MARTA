
import pytest
from typesystem.fields import Field, Union

# Test 1: Validate a non-null value against the union type

# Test 2: Add another field to the union and validate a valid address string

# Test 3: Validate a null value against the union type
def test_validate_null():
    field1 = Field()
    field2 = Field(allow_null=True)
    union = Union(any_of=[field1, field2])
    validated_null = union.validate(None)
    assert validated_null is None