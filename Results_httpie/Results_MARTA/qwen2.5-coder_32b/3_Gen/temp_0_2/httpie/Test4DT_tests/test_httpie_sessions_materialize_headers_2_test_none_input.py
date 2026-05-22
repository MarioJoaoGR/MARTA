
import pytest
from typing import Dict, List, Any

def materialize_headers(headers: Dict[str, str]) -> List[Dict[str, Any]]:
    if headers is None:
        raise TypeError("Headers must be a dictionary")
    return [
        {
            'name': name,
            'value': value
        }
        for name, value in headers.copy().items()
    ]

def test_none_input():
    with pytest.raises(TypeError):
        materialize_headers(None)
