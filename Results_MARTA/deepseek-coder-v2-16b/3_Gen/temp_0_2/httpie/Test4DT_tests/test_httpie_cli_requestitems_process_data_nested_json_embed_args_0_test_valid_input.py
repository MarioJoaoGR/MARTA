
import pytest
from unittest.mock import patch
from httpie.cli.requestitems import process_data_nested_json_embed_args

# Define expected JSON types for type checking in the function
JSONType = dict  # Assuming this is the type used by interpret_nested_json

@pytest.mark.parametrize("pairs, expected", [
    (
        [("a.b", "SET 2"), ("a", "SET {'c': 3}"), ("a.d", "SET None")],
        {"a": {"b": 2, "c": 3, "d": None}}
    ),
    (
        [("users[0].name", "SET John Doe"), ("users[1].age", "SET 30")],
        {"users": [{'name': 'John Doe'}, {'age': 30}]}
    ),
    ([], {})
])
def test_valid_input(pairs, expected):
    with patch('httpie.cli.requestitems.interpret_nested_json', return_value=expected):
        result = process_data_nested_json_embed_args(pairs)
        assert result == expected
