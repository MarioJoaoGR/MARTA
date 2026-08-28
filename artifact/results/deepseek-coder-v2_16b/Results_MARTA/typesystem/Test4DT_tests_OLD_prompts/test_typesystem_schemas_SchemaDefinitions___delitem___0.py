
import pytest
from typesystem.schemas import SchemaDefinitions


def test_invalid_input_delitem():
    schema_defs = SchemaDefinitions({'key1': 'value1', 'key2': 'value2'})
    with pytest.raises(KeyError):
        del schema_defs['non_existent_key']