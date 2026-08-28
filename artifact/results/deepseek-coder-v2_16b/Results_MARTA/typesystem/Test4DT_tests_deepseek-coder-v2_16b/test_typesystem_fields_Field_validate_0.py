
import pytest
from typesystem.fields import Field, NO_DEFAULT

# Scenario 1: Test initialization with required parameters

# Scenario 2: Test initialization with allow_null set to True
def test_init_with_allow_null():
    field = Field(title="Height", description="The height in meters", allow_null=True)
    assert isinstance(field.title, str)
    assert field.title == "Height"
    assert isinstance(field.description, str)
    assert field.description == "The height in meters"
    assert field.default is None