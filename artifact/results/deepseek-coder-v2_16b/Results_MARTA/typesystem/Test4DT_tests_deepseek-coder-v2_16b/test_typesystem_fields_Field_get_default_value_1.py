
import pytest
from typesystem.fields import Field, NO_DEFAULT

# Scenario 1: Test standard input with valid schema definitions

# Scenario 2: Test creating a nullable field without providing a default value
def test_nullable_field():
    field = Field(title="Height", description="The height in meters", allow_null=True)
    assert field.title == "Height"
    assert field.description == "The height in meters"
    assert field.default is None
    assert field.allow_null

# Scenario 3: Test creating a field with a provided default value
def test_field_with_default():
    field = Field(title="Age", description="The age of the person", default=30)
    assert field.title == "Age"
    assert field.description == "The age of the person"
    assert field.default == 30
    assert not field.allow_null

# Scenario 4: Test creating a non-nullable field without providing a default value