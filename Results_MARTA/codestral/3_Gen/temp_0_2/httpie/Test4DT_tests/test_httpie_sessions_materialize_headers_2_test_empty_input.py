
import pytest
from typing import Dict, List, Any

def materialize_headers(headers: Dict[str, str]) -> List[Dict[str, Any]]:
    return [
        {
            'name': name,
            'value': value
        }
        for name, value in headers.copy().items()
    ]

def test_empty_input():
    headers = {}
    result = materialize_headers(headers)
    assert result == []
