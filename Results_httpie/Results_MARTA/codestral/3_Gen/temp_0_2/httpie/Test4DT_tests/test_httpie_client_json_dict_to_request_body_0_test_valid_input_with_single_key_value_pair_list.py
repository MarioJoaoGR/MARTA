
import json
from typing import Dict, Any
from unittest.mock import patch

def test_valid_input_with_single_key_value_pair_list():
    data = {'key': [1, 2, 3]}
    
    with patch('httpie.client.json_dict_to_request_body', return_value='{"key": [1, 2, 3]}'):
        from httpie.client import json_dict_to_request_body
        result = json_dict_to_request_body(data)
        assert result == '{"key": [1, 2, 3]}'
