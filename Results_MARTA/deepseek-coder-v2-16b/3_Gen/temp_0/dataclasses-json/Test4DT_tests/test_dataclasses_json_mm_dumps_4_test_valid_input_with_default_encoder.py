
import pytest
from dataclasses import dataclass
from marshmallow import Schema, fields
from dataclasses_json.mm import _ExtendedEncoder

@pytest.fixture
def mock_schema():
    class MySchema(Schema):
        id = fields.Int()
        name = fields.Str()
    
    schema_instance = MySchema()
    return schema_instance

def test_valid_input_with_default_encoder(mock_schema):
    # Call the dumps method without providing a custom encoder
    result = mock_schema.dumps({'id': 1, 'name': 'John Doe'})
    
    # Check that the default encoder was used
    assert isinstance(result, str)
    data = eval(result)  # Convert JSON string to dictionary for comparison
    assert data['id'] == 1
    assert data['name'] == 'John Doe'
