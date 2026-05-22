
import pytest
from unittest.mock import patch
from httpie.cli.requestitems import process_data_nested_json_embed_args, interpret_nested_json
from typing import Dict, Iterable, Tuple
from httpie.cli.nested_json.interpret import NestedJSONSyntaxError
from httpie.cli.nested_json.parse import parse
from httpie.cli.nested_json.errors import NestedJSONSyntaxError

# Define the test data
test_data = [
    (['a.b', 'SET 2'], {'a': {'b': 2}}),
    ([('a.b', 'SET 2'), ('a', "SET {'c': 3}"), ('a.d', 'SET None')], {'a': {'b': 2, 'c': 3, 'd': None}}),
    ([('users[0].name', 'SET John Doe'), ('users[1].age', 'SET 30')], {'users': [{'name': 'John Doe'}, {'age': 30}]})
]

@pytest.mark.parametrize("pairs, expected", test_data)
def test_process_data_nested_json_embed_args(pairs, expected):
    with patch('httpie.cli.requestitems.interpret_nested_json', side_effect=lambda x: {'a': {'b': 2}} if x == ['a.b', 'SET 2'] else {'a': {'b': 2, 'c': 3, 'd': None}} if x == [('a.b', 'SET 2'), ('a', "SET {'c': 3}"), ('a.d', 'SET None')] else {'users': [{'name': 'John Doe'}, {'age': 30}]}):
        result = process_data_nested_json_embed_args(pairs)
    assert result == expected
