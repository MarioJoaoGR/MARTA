
import pytest
from typesystem.fields import Field

# Scenario 1: Test standard input with valid schema definitions

# Scenario 2: Test creation with allow_null set to True and no default value provided
def test_allow_null_no_default():
    field = Field(title="Height", description="The height in meters", allow_null=True)
    assert field.title == "Height"
    assert field.description == "The height in meters"
    assert field.default is None
    assert field.allow_null is True

# Scenario 3: Test creation with default value provided
def test_with_default():
    field = Field(title="Age", description="The age of the person", default=18)
    assert field.title == "Age"
    assert field.description == "The age of the person"
    assert field.default == 18
    assert field.allow_null is False