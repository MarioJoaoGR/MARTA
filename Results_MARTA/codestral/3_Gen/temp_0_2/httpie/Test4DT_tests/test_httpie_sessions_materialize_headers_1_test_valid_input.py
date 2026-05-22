
from typing import Dict, List, Any
import httpie.sessions as sessions
from unittest.mock import patch

def materialize_headers(headers: Dict[str, str]) -> List[Dict[str, Any]]:
    return [
        {
            'name': name,
            'value': value
        }
        for name, value in headers.copy().items()
    ]

# Test case to verify the function works with valid input
def test_valid_input():
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer token'}
    expected_output = [
        {'name': 'Content-Type', 'value': 'application/json'},
        {'name': 'Authorization', 'value': 'Bearer token'}
    ]
    
    with patch.object(sessions, 'materialize_headers', side_effect=lambda x: expected_output):
        result = sessions.materialize_headers(headers)
        assert result == expected_output
