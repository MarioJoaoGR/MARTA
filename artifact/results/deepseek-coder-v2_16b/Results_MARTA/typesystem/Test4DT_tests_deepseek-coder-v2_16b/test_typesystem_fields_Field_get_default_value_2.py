
import pytest
from typesystem.fields import Field

# Scenario 1: Test creating a Field instance with valid inputs

# Scenario 2: Test creating a nullable Field instance without providing a default value
def test_nullable_field():
    field = Field(title="Height", description="The height in meters", allow_null=True)
    assert field.title == "Height"
    assert field.description == "The height in meters"
    assert field.default is None

# Scenario 3: Test creating a Field instance with a provided default value
def test_field_with_default():
    field = Field(title="Age", description="The age of the person", default=30)
    assert field.title == "Age"
    assert field.description == "The age of the person"
    assert field.default == 30

# Scenario 4: Test creating a Field instance with allow_null set to False and providing a default value
def test_field_no_null():
    field = Field(title="Salary", description="Yearly salary", default=50000, allow_null=False)
    assert field.title == "Salary"
    assert field.description == "Yearly salary"
    assert field.default == 50000

# Scenario 5: Test invalid input with missing required parameters