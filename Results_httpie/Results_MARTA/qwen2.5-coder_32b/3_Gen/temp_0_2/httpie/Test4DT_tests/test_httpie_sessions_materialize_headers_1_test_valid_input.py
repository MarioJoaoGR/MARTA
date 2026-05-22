
from httpie.sessions import materialize_headers
import pytest
from typing import Dict, List, Any

def test_materialize_headers():
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer token'}
    expected_output = [{'name': 'Content-Type', 'value': 'application/json'}, {'name': 'Authorization', 'value': 'Bearer token'}]
    
    result = materialize_headers(headers)
    
    assert result == expected_output
