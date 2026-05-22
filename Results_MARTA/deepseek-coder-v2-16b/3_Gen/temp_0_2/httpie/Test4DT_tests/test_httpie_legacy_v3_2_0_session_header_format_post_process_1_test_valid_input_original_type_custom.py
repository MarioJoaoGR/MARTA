
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

# Test function for test_valid_input_original_type_custom
@pytest.mark.parametrize("normalized_headers, original_type, expected", [
    ([{'name': 'Custom-Header', 'value': 'example'}], type(None), [{'name': 'Custom-Header', 'value': 'example'}]),
    ([{'name': 'Content-Type', 'value': 'application/json'}], dict, {'Content-Type': 'application/json'}),
])
def test_valid_input_original_type_custom(normalized_headers, original_type, expected):
    with patch('httpie.legacy.v3_2_0_session_header_format.issubclass', return_value=False):
        assert post_process(normalized_headers, original_type=original_type) == expected
