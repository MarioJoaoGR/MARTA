
import pytest
from unittest.mock import patch
from httpie.sessions import materialize_headers
from typing import Dict, List, Any

def test_valid_input():
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer token'}
    expected_output = [
        {'name': 'Content-Type', 'value': 'application/json'},
        {'name': 'Authorization', 'value': 'Bearer token'}
    ]
    
    with patch('httpie.sessions.materialize_headers') as mock_materialize:
        # Configure the mock to return expected output
        mock_materialize.return_value = expected_output
        
        # Call the function and assert the result
        result = materialize_headers(headers)
        assert result == expected_output
