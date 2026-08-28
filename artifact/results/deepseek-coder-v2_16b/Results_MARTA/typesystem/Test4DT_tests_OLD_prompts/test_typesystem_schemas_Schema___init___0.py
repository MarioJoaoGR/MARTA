
import pytest
from typesystem.schemas import Schema, Field

# Test for valid inputs

# Test for edge cases with None input

# Test for invalid keyword argument
def test_invalid_keyword_argument():
    class SchemaExample(Schema):
        fields = {
            'name': Field(default='Unknown'),
            'age': Field()
        }
    
    with pytest.raises(TypeError) as excinfo:
        SchemaExample(invalid_arg='Invalid')
    assert str(excinfo.value) == "'invalid_arg' is an invalid keyword argument for SchemaExample()."