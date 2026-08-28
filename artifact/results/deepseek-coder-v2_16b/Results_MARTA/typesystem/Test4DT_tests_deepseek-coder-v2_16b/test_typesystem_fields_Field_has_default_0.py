
import pytest
from typesystem.fields import Field, NO_DEFAULT

# Scenario 1: Test standard input with valid schema definitions

# Scenario 2: Test Field with allow_null set to True and no default value
def test_allow_null():
    field = Field(title="Height", description="The height in meters", allow_null=True)
    assert isinstance(field.title, str)
    assert isinstance(field.description, str)
    assert field.default is None  # Default should be set to None due to allow_null being True

# Scenario 3: Test Field with a provided default value
def test_provided_default():
    field = Field(title="Weight", description="The weight in kilograms", default=50)
    assert isinstance(field.title, str)
    assert isinstance(field.description, str)
    assert field.default == 50  # Ensure the provided default value is correctly set

# Scenario 4: Test Field with allow_null set to False and a provided default value
def test_no_allow_null():
    field = Field(title="Temperature", description="The temperature in Celsius", default=37, allow_null=False)
    assert isinstance(field.title, str)
    assert isinstance(field.description, str)
    assert field.default == 37  # Ensure the provided default value is correctly set and not null