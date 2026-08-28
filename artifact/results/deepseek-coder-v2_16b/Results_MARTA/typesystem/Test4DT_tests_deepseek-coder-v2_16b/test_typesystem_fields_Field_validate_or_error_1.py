
import pytest
from typesystem.fields import Field, NO_DEFAULT, ValidationResult, ValidationError

# Test 1: Valid input with all parameters specified
def test_valid_input_with_all_parameters():
    field = Field(title="Name", description="The name of the person", default="John Doe", allow_null=False)
    assert field.title == "Name"
    assert field.description == "The name of the person"
    assert field.default == "John Doe"
    assert not field.allow_null

# Test 2: Edge case with no default value and allow_null set to True
def test_edge_case_with_none_default_and_allow_null():
    field = Field(title="Age", description="The age of the person", allow_null=True)
    assert field.title == "Age"
    assert field.description == "The age of the person"
    assert getattr(field, 'default', None) is None  # Default should be set to None due to allow_null=True
    assert field.allow_null

# Test 3: Invalid input with incorrect type for title and description parameters
def test_invalid_input_with_incorrect_type():
    with pytest.raises(AssertionError):
        Field(title=123, description=[], default="John Doe", allow_null=False)
