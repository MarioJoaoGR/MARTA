
import pytest
from httpie.sessions import materialize_headers
from typing import Dict, List, Any

def test_materialize_headers():
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer token'}
    expected_output = [
        {'name': 'Content-Type', 'value': 'application/json'},
        {'name': 'Authorization', 'value': 'Bearer token'}
    ]
    
    assert materialize_headers(headers) == expected_output
