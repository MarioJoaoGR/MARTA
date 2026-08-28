
import pytest
from mimesis.schema import Schema
from mimesis.exceptions import UndefinedSchema

def test_valid_callable_schema():
    def example_schema():
        return {"id": 1, "name": "Example"}
    
    schema = Schema(example_schema)
    filled_schemas = schema.create(iterations=3)
    assert isinstance(filled_schemas, list), "Expected a list of filled schemas"
    assert len(filled_schemas) == 3, "Expected exactly 3 filled schemas"
    for item in filled_schemas:
        assert isinstance(item, dict), "Each filled schema should be a dictionary"
        assert "id" in item and isinstance(item["id"], int), "Each filled schema should have an integer id"
        assert "name" in item and isinstance(item["name"], str), "Each filled schema should have a string name"
