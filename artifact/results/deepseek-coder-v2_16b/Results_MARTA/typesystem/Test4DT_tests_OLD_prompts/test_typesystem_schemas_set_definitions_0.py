
import pytest
from typesystem.schemas import Field, Array, Object, SchemaDefinitions, Reference, set_definitions

def test_valid_input():
    properties = {
        'name': Field(default='Unknown'),
        'age': Field(),
        'addresses': Array(items=[Object(properties={'street': Field(), 'city': Field()})])
    }
    schema = Object(properties=properties)
    definitions = SchemaDefinitions({
        'name': Field(default='Unknown'),
        'age': Field(),
        'addresses': Array(items=[Object(properties={'street': Field(), 'city': Field()})])
    })
    
    set_definitions(schema, definitions)
    assert schema.properties['name'].default == 'Unknown'

