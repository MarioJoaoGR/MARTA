
import pytest
from typesystem.fields import Field, NO_DEFAULT

def test_field_creation():
    field = Field(title="Name", description="The name of the person")
    assert isinstance(field.title, str)
    assert field.title == "Name"
    assert isinstance(field.description, str)
    assert field.description == "The name of the person"