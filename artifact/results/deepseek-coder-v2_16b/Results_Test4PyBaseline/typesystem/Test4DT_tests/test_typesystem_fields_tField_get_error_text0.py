
import pytest
from typesystem.fields import Field, NO_DEFAULT

def test_field_creation():
    field = Field(title="Name", description="The name of the person")
    assert isinstance(field.title, str)
    assert field.title == "Name"
    assert isinstance(field.description, str)
    assert field.description == "The name of the person"
    assert not hasattr(field, 'default')
    assert not field.allow_null

def test_field_creation_with_default():
    field_with_default = Field(title="Age", default=18)
    assert isinstance(field_with_default.title, str)
    assert field_with_default.title == "Age"
    assert hasattr(field_with_default, 'default')
    assert field_with_default.default == 18
    assert not field_with_default.allow_null

def test_field_creation_allowing_null():
    field_allow_null = Field(title="Email", allow_null=True)
    assert isinstance(field_allow_null.title, str)
    assert field_allow_null.title == "Email"