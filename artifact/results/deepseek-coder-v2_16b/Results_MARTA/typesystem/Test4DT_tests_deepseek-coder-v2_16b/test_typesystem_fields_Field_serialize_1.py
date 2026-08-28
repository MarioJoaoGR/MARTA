
import pytest
from typesystem.fields import Field, NO_DEFAULT

# Scenario 1: Test standard input with valid schema definitions

# Scenario 2: Test creation of a Field with allow_null set to True and no default value
def test_allow_null():
    field = Field(title="Height", description="The height in meters", allow_null=True)
    assert isinstance(field.title, str)
    assert field.title == "Height"
    assert isinstance(field.description, str)
    assert field.description == "The height in meters"
    assert field.default is None

# Scenario 3: Test creation of a Field with allow_null set to False and no default value