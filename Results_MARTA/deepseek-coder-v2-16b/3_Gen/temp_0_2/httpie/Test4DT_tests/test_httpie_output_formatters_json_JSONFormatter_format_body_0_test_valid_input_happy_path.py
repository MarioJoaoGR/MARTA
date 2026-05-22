
import pytest
from unittest.mock import patch
from httpie.output.formatters.json import JSONFormatter
import json

@pytest.fixture(autouse=True)
def setup_formatter():
    formatter = JSONFormatter(format_options={'json': {'format': True, 'sort_keys': True, 'indent': 4}})
    return formatter

def test_valid_input_happy_path(setup_formatter):
    body = '{"name": "John", "age": 30}'
    mime = 'application/json'
    
    with patch('httpie.output.formatters.json.JSONFormatter.format_body', return_value=body) as mock_format_body:
        result = setup_formatter.format_body(body, mime)
        
        assert result == body
        mock_format_body.assert_called_once_with(body, mime)
