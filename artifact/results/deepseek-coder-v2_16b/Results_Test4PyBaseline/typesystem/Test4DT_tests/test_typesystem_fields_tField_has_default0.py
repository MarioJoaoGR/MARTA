# Module: typesystem.fields
import pytest
from typesystem.fields import Field, NO_DEFAULT

# Test creating a Field instance with title and description
def test_field_creation_with_title_and_description():
    field = Field(title="Name", description="The name of the person")
    assert isinstance(field.title, str)
    assert field.title == "Name"
    assert isinstance(field.description, str)
    assert field.description == "The name of the person"

# Test creating a Field instance with default value
def test_field_creation_with_default_value():
    field_with_default = Field(title="Age", default=18)
    assert hasattr(field_with_default, "default")
    assert field_with_default.default == 18

# Test creating a Field instance allowing null values
def test_field_creation_allowing_null_values():
    field_allow_null = Field(title="Email", allow_null=True)
    assert field_allow_null.allow_null is True

# Test checking if a Field has a default value when it does
def test_has_default_true():
    field_with_default = Field(title="Age", default=18)
    assert field_with_default.has_default() is True

# Test checking if a Field has a default value when it doesn't
def test_has_default_false():
    field = Field(title="Name", description="The name of the person")
    assert not hasattr(field, "default")
    assert field.has_default() is False

# Test checking if a Field has a default value after changing it
def test_has_default_after_change():
    field = Field(title="Age", default=18)
    field.default = None  # Change the default value to None
    assert field.has_default() is True
