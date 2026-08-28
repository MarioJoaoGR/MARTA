
import pytest
from unittest.mock import patch, MagicMock
from typesystem.fields import Field, NO_DEFAULT

# Test valid inputs
def test_valid_inputs():
    with patch('typesystem.fields.Field._creation_counter', new=0):
        field = Field(title="Name", description="The name of the person", default="John Doe", allow_null=False)
        assert field.title == "Name"
        assert field.description == "The name of the person"
        assert field.default == "John Doe"
        assert field.allow_null is False

    with patch('typesystem.fields.Field._creation_counter', new=0):
        field = Field(title="Age", description="The age of the person")
        assert field.title == "Age"
        assert field.description == "The age of the person"
        assert getattr(field, 'default', None) is None  # default should be NO_DEFAULT
        assert field.allow_null is False

    with patch('typesystem.fields.Field._creation_counter', new=0):
        field = Field(title="Height", description="The height in meters", allow_null=True)
        assert field.title == "Height"
        assert field.description == "The height in meters"
        assert getattr(field, 'default', None) is None  # default should be NO_DEFAULT
        assert field.allow_null is True

# Test edge cases
def test_edge_cases():
    with pytest.raises(AssertionError):
        Field(title=123, description="The age of the person")
    
    with pytest.raises(AssertionError):
        Field(title="Age", description=123)
    
    field = Field(title="Height", description="The height in meters", allow_null=True)
    assert field.allow_null is True
    field.default = None  # Setting default to None should not raise an error
    assert field.default is None

# Test invalid inputs
def test_invalid_inputs():
    with pytest.raises(AssertionError):
        Field(title=None, description="The name of the person")
    
    with pytest.raises(AssertionError):
        Field(title="Name", description=None)
    
    with pytest.raises(AssertionError):
        Field(title=123, description=123)
