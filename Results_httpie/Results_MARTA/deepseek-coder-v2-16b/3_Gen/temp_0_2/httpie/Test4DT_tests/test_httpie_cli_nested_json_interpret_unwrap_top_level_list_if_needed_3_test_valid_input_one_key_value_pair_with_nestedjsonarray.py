
import pytest
from httpie.cli.nested_json.interpret import unwrap_top_level_list_if_needed, NestedJSONArray
from unittest.mock import patch

def test_valid_input_one_key_value_pair_with_nestedjsonarray():
    data = {'key': NestedJSONArray([1, 2, 3])}
    with patch('httpie.cli.nested_json.interpret.EMPTY_STRING', 'key'):
        result = unwrap_top_level_list_if_needed(data)
        assert isinstance(result, list), "Expected a top-level list to be returned"
