
import pytest
from unittest.mock import patch
from typesystem.json_schema import enum_from_json_schema, SchemaDefinitions, Choice, NO_DEFAULT
from typesystem.fields import Field


def test_missing_values():
    data = {}
    with patch('typesystem.json_schema.Choice') as mock_choice:
        with pytest.raises(KeyError):
            enum_from_json_schema(data, SchemaDefinitions())