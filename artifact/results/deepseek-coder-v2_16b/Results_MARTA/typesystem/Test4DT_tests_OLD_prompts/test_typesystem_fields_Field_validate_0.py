
import pytest
from typesystem.fields import Field, NO_DEFAULT

def test_field_creation_with_all_parameters():
    field = Field(title="Name", description="The name of the person", default="John Doe", allow_null=False)
    assert field.title == "Name"
    assert field.description == "The name of the person"
    assert field.default == "John Doe"
    assert field.allow_null is False




def test_field_creation_invalid_title_type():
    with pytest.raises(AssertionError):
        Field(title=123, description="Invalid title type")

def test_field_creation_invalid_description_type():
    with pytest.raises(AssertionError):
        Field(title="Valid Title", description=None)