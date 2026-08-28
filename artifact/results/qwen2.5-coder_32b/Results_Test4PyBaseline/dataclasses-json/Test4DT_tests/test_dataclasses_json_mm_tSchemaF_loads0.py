
import pytest
from dataclasses_json.mm import SchemaF

class MySchema(SchemaF):
    def __init__(self):
        # Avoid calling super().__init__() to prevent NotImplementedError
        pass

    def loads(self, json_data, many=False, partial=False, unknown='raise', **kwargs):
        # Mock implementation for testing purposes
        if isinstance(json_data, str):
            import json
            data = json.loads(json_data)
        else:
            data = json_data

        if many:
            return [self._load_item(item, partial, unknown) for item in data]
        else:
            return self._load_item(data, partial, unknown)

    def _load_item(self, data, partial, unknown):
        # Mock implementation to simulate loading a single item
        if unknown == 'raise' and any(key not in ['name', 'age'] for key in data.keys()):
            raise ValueError("Unknown field encountered")
        elif unknown == 'exclude':
            data = {key: value for key, value in data.items() if key in ['name', 'age']}
        # Create a mock object with attributes
        obj = type('MockObject', (object,), data)()
        return obj

def test_schemaf_initialization():
    with pytest.raises(NotImplementedError):
        SchemaF()

def test_my_schema_loads_single_object():
    schema = MySchema()
    data = '{"name": "John", "age": 30}'
    result = schema.loads(data)
    assert result.name == "John"
    assert result.age == 30

def test_my_schema_loads_multiple_objects():
    schema = MySchema()
    data_list = '[{"name": "John"}, {"name": "Jane"}]'
    results = schema.loads(data_list, many=True)
    assert len(results) == 2
    assert results[0].name == "John"
    assert results[1].name == "Jane"

def test_my_schema_loads_partial_data():
    schema = MySchema()
    partial_data = '{"name": "John"}'
    result = schema.loads(partial_data, partial=True)
    assert result.name == "John"
    # Assuming 'age' is optional and not present

def test_my_schema_excludes_unknown_fields():
    schema = MySchema()
    unknown_data = '{"name": "John", "extra_field": "value"}'
    result = schema.loads(unknown_data, unknown='exclude')
    assert result.name == "John"
    with pytest.raises(AttributeError):
        _ = result.extra_field

def test_my_schema_includes_unknown_fields():
    schema = MySchema()
    unknown_data = '{"name": "John", "extra_field": "value"}'
    result = schema.loads(unknown_data, unknown='include')
    assert result.name == "John"
    assert result.extra_field == "value"

def test_my_schema_raises_on_unknown_fields():
    schema = MySchema()
    unknown_data = '{"name": "John", "extra_field": "value"}'
    with pytest.raises(ValueError):
        schema.loads(unknown_data, unknown='raise')

def test_my_schema_with_custom_kwargs():
    schema = MySchema()
    data = '{"name": "John", "age": 30}'
    result = schema.loads(data, some_custom_arg='value')