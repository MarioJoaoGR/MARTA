
import json
from typing import Dict, Any
from unittest.mock import patch

def test_valid_input_with_single_key_value_pair_list():
    data = {'key': [1, 2, 3]}
    
    with patch('json.dumps', return_value='{"key": [1, 2, 3]}'):
        result = json_dict_to_request_body(data)
        assert result == '{"key": [1, 2, 3]}'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_client_json_dict_to_request_body_0_test_valid_input_with_single_key_value_pair_list
httpie/Test4DT_tests_codestral/test_httpie_client_json_dict_to_request_body_0_test_valid_input_with_single_key_value_pair_list.py:10:17: E0602: Undefined variable 'json_dict_to_request_body' (undefined-variable)


"""