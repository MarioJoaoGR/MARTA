
import pytest
from unittest.mock import patch
from httpie.cli.nested_json.interpret import unwrap_top_level_list_if_needed, NestedJSONArray

# Define a mock NestedJSONArray class for testing
class MockNestedJSONArray(list):
    pass

def test_error_case_multiple_items():
    data = {'key1': 'value1', 'key2': 'value2'}
    
    with patch('httpie.cli.nested_json.interpret.NestedJSONArray', MockNestedJSONArray):
        result = unwrap_top_level_list_if_needed(data)
        
        assert isinstance(result, dict), "Expected a dictionary but got something else"
        assert len(result) == 2, "Expected the dictionary to have exactly two key-value pairs"
