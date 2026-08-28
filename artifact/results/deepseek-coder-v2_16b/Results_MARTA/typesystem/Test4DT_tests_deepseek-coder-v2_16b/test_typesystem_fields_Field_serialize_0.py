
import pytest
from typesystem.fields import Field, NO_DEFAULT

# Test 1: Valid input with all parameters specified
def test_valid_input_with_all_parameters():
    field = Field(title='Name', description='The name of the person', default='John Doe', allow_null=False)
    assert field.title == 'Name'
    assert field.description == 'The name of the person'
    assert field.default == 'John Doe'
    assert field.allow_null is False

# Test 2: Edge case where allow_null is True but no default value is provided
def test_edge_case_missing_default_with_allow_null():
    field = Field(title='Height', description='The height in meters', allow_null=True)
    assert field.title == 'Height'
    assert field.description == 'The height in meters'
    assert field.default is None
    assert field.allow_null is True

# Test 3: Raising AssertionError when title is not a string
def test_invalid_input_non_string_title():
    with pytest.raises(AssertionError):
        Field(title=123, description='The age of the person')
