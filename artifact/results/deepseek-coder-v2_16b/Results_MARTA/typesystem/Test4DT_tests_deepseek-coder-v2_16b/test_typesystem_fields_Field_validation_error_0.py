
import pytest
from typesystem.fields import Field

# Scenario 1: Test standard input with valid schema definitions

# Scenario 2: Test creating a Field with allow_null set to True and no default value
def test_field_with_allow_null():
    field = Field(title="Height", description="The height in meters", allow_null=True)
    assert isinstance(field.title, str)
    assert isinstance(field.description, str)
    assert field.default is None
    assert field.allow_null == True

# Scenario 3: Test creating a Field with a specified default value
def test_field_with_default():
    field = Field(title="Weight", description="The weight in kilograms", default=50)
    assert isinstance(field.title, str)
    assert isinstance(field.description, str)
    assert field.default == 50
    assert field.allow_null == False