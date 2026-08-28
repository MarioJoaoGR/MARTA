
import pytest
from typesystem.schemas import Schema, Field  # Assuming these classes are defined in 'typesystem.schemas'

# Test initialization with a dictionary as positional argument

# Test initialization with keyword arguments only

# Test initialization with an invalid keyword argument
def test_schema_init_with_invalid_kwargs():
    class SchemaExample(Schema):
        fields = {
            'name': Field(default='Unknown'),
            'age': Field()
        }
    
    with pytest.raises(TypeError) as excinfo:
        schema = SchemaExample(invalid_arg='Invalid')
    assert str(excinfo.value) == "'invalid_arg' is an invalid keyword argument for SchemaExample()."

# Test initialization using a dictionary and default values

# Test equality comparison between two Schema instances