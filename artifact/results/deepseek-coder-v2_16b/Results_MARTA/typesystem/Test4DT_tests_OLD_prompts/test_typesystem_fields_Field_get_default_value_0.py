
import pytest
from typesystem.fields import Field, NO_DEFAULT


def test_field_creation_with_default():
    field = Field(title="Name", description="The name of the person", default="John Doe")
    assert field.title == "Name"
    assert field.description == "The name of the person"
    assert field.get_default_value() == "John Doe"

def test_nullable_field_with_no_default():
    field = Field(title="Height", description="The height in meters", allow_null=True)
    assert field.title == "Height"
    assert field.description == "The height in meters"
    assert field.get_default_value() is None
