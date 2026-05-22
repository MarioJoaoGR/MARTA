
import pytest
from unittest.mock import patch
from httpie.cli.nested_json.interpret import unwrap_top_level_list_if_needed, NestedJSONArray

# Define a mock NestedJSONArray class for testing
class MockNestedJSONArray(list):
    pass

@pytest.fixture(autouse=True)
def setup_mock():
    with patch('httpie.cli.nested_json.interpret.NestedJSONArray', new=MockNestedJSONArray):
        yield

def test_invalid_input_more_than_one_key_value_pair():
    data = {'key1': 'value1', 'key2': 'value2'}
    assert unwrap_top_level_list_if_needed(data) == data
