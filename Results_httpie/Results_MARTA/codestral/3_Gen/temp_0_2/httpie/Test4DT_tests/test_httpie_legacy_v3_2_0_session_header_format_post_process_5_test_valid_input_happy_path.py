
import pytest
from typing import List, Dict, Any, Type
from unittest.mock import patch

def post_process(
    normalized_headers: List[Dict[str, Any]],
    *,
    original_type: Type[Any]
) -> Any:
    """Deserialize given header store into the original form it was
    used in."""

    if issubclass(original_type, dict):
        # For the legacy behavior, preserve the last value.
        return {
            item['name']: item['value']
            for item in normalized_headers
        }
    else:
        return normalized_headers

@pytest.fixture
def valid_input():
    return [{'name': 'Content-Type', 'value': 'application/json'}]

def test_valid_input_happy_path(valid_input):
    result = post_process(valid_input, original_type=dict)
    assert result == {'Content-Type': 'application/json'}

def test_valid_input_custom_header(valid_input):
    class CustomHeader:
        def __init__(self, name, value):
            self.name = name
            self.value = value
    
    result = post_process(valid_input, original_type=CustomHeader)
    assert result == [{'name': 'Content-Type', 'value': 'application/json'}]
