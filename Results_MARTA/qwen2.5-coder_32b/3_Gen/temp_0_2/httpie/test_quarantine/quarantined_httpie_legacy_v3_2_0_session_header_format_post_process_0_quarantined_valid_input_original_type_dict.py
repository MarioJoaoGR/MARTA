
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

@pytest.mark.parametrize("normalized_headers, original_type, expected", [
    (
        [{'name': 'Content-Type', 'value': 'application/json'}], 
        dict, 
        {'Content-Type': 'application/json'}
    ),
    (
        [{'name': 'Custom-Header', 'value': 'example'}], 
        CustomHeader, 
        [{'name': 'Custom-Header', 'value': 'example'}]
    )
])
def test_valid_input_original_type_dict(normalized_headers, original_type, expected):
    with patch('httpie.legacy.v3_2_0_session_header_format.issubclass', return_value=True):
        assert post_process(normalized_headers, original_type=original_type) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_legacy_v3_2_0_session_header_format_post_process_0_test_valid_input_original_type_dict
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_legacy_v3_2_0_session_header_format_post_process_0_test_valid_input_original_type_dict.py:31:8: E0602: Undefined variable 'CustomHeader' (undefined-variable)


"""