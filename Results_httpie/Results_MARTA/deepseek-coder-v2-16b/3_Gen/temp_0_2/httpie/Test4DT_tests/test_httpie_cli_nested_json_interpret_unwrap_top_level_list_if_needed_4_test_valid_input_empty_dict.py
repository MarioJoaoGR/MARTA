
import pytest
from unittest.mock import patch
from httpie.cli.nested_json.interpret import unwrap_top_level_list_if_needed, NestedJSONArray

# Assuming EMPTY_STRING is a predefined constant in the module 'httpie.cli.nested_json.interpret'
EMPTY_STRING = ""

@pytest.fixture(autouse=True)
def mock_constants():
    with patch('httpie.cli.nested_json.interpret.EMPTY_STRING', new=""):
        yield

def test_valid_input_empty_dict():
    input_data = {}
    result = unwrap_top_level_list_if_needed(input_data)
    assert result == {}
