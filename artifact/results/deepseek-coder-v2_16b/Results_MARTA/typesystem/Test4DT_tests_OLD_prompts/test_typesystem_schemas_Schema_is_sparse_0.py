
import pytest
from typesystem.schemas import Schema, Field


def test_edge_cases():
    class SchemaExample(Schema):
        fields = {
            'name': Field(default='Unknown'),
            'age': Field()
        }
    
    with pytest.raises(TypeError):
        SchemaExample(invalid_arg='Invalid')