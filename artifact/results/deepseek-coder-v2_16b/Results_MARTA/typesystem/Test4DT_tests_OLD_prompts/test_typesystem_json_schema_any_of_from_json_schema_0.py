
import pytest
from unittest.mock import patch
from typesystem.json_schema import from_json_schema, SchemaDefinitions, Field, Union, NO_DEFAULT
from typesystem.json_schema import any_of_from_json_schema  # Assuming this is the correct module path



def test_default_value():
    data = {'anyOf': [{'type': 'integer'}, {'type': 'string'}], 'default': 42}
    result = any_of_from_json_schema(data, {})
    assert isinstance(result.default, int), "Expected default value to be an integer"