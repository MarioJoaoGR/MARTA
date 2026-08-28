
import pytest
from mimesis.schema import Schema
from mimesis.exceptions import UndefinedSchema
from unittest.mock import patch

# Test valid callable schema
def test_valid_callable_schema():
    def example_schema():
        return {'id': 1, 'name': 'Example'}
    
    my_schema = Schema(example_schema)
    filled_schemas = my_schema.create(iterations=3)
    assert isinstance(filled_schemas, list), "Expected a list of filled schemas"
    assert len(filled_schemas) == 3, "Expected 3 filled schemas"
    assert all(isinstance(item, dict) for item in filled_schemas), "All items should be dictionaries"

# Test None input raises UndefinedSchema
def test_none_input():
    with pytest.raises(UndefinedSchema):
        invalid_schema = Schema(None)

# Test non-callable input raises UndefinedSchema
def test_non_callable_input():
    with pytest.raises(UndefinedSchema):
        invalid_schema = Schema('not_a_callable')
