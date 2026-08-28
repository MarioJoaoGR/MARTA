
# Module: typesystem.fields
import pytest
from typesystem.fields import Field, NO_DEFAULT

# Test Case 1: Creating a Field with Title and Description
def test_field_creation_with_title_and_description():
    field = Field(title="Name", description="The name of the person")
    assert isinstance(field.title, str), "Title should be a string"
    assert field.title == "Name", "Title should be 'Name'"
    assert isinstance(field.description, str), "Description should be a string"
    assert field.description == "The name of the person", "Description should be 'The name of the person'"