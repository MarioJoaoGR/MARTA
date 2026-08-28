
import pytest
from typesystem.fields import Field, NO_DEFAULT

def test_valid_input_with_all_parameters():
    field = Field(title="Name", description="The name of the person", default="John Doe", allow_null=False)
    assert field.title == "Name"
    assert field.description == "The name of the person"
    assert field.default == "John Doe"
    assert field.allow_null is False

def test_edge_case_none_values():
    with pytest.raises(AssertionError):
        Field(title=None, description=None, default=None, allow_null=True)

def test_invalid_input_assertions():
    with pytest.raises(AssertionError):
        Field(title=123, description=[], default="John Doe", allow_null=False)
