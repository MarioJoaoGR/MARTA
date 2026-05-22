
import json
from typing import Dict, Any
from unittest.mock import patch

def test_valid_input_with_single_key_value_pair_list():
    # Test with a valid dictionary containing exactly one key-value pair where the value is a list
    data = {'key': [1, 2, 3]}
    expected_output = '{"key": [1, 2, 3]}'
    
    result = json_dict_to_request_body(data)
    
    assert result == expected_output

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_client_json_dict_to_request_body_0_test_valid_input_with_single_key_value_pair_list
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_client_json_dict_to_request_body_0_test_valid_input_with_single_key_value_pair_list.py:11:13: E0602: Undefined variable 'json_dict_to_request_body' (undefined-variable)


"""