
import pytest
from typesystem.schemas import Schema, Field

# Scenario 1: Test initialization with a dictionary

# Scenario 2: Test initialization with keyword arguments

# Scenario 3: Test initialization with invalid keyword argument
def test_schema_init_with_invalid_kwargs():
    class SchemaExample(Schema):
        fields = {
            'name': Field(default='Unknown'),
            'age': Field()
        }
    
    with pytest.raises(TypeError) as excinfo:
        SchemaExample(invalid_arg='Invalid')
    assert str(excinfo.value) == "'invalid_arg' is an invalid keyword argument for SchemaExample()."

# Scenario 4: Test iteration over schema fields