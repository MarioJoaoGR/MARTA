
import pytest
from typesystem.fields import Field, NO_DEFAULT



def test_field_creation_with_null_and_no_default():
    field = Field(title="Height", description="The height in meters", allow_null=True)
    assert field.allow_null is True
    assert field.default is None

def test_field_has_default():
    field = Field(title="Weight", description="The weight in kilograms", default=50)
    assert field.has_default() is True

def test_field_no_default_but_allow_null():
    field = Field(title="Temperature", description="The temperature in Celsius", allow_null=True)
    assert field.default is None

