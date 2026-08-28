
import pytest
from typesystem.json_schema import const_from_json_schema, NO_DEFAULT
from typesystem.schemas import SchemaDefinitions

# Scenario 1: Test standard input with valid schema definitions

# Scenario 2: Test with default value present in data
def test_with_default_value():
    data = {"const": 42, "default": None}
    schema_defs = SchemaDefinitions({'key': 'value'})
    const_field = const_from_json_schema(data, schema_defs)
    assert const_field.const == 42
    assert const_field.default is None

# Scenario 3: Test with no default value present in data