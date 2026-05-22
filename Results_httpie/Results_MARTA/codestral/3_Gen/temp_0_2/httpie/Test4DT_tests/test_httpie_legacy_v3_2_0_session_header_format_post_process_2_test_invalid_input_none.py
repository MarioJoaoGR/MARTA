
import pytest
from unittest.mock import patch
from typing import List, Dict, Any, Type

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

def test_invalid_input_none():
    with pytest.raises(TypeError):
        post_process(normalized_headers=None, original_type=dict)
