
import unittest
from unittest.mock import patch
from httpie.client import json_dict_to_request_body
import json
from typing import Dict, Any

class TestJsonDictToRequestBody(unittest.TestCase):
    def test_valid_input_with_single_key_value_pair_list(self):
        with patch('httpie.client.json.dumps', return_value='{"key": [1, 2, 3]}'):
            result = json_dict_to_request_body({'key': [1, 2, 3]})
            self.assertEqual(result, '{"key": [1, 2, 3]}')

    def test_invalid_input_without_single_key_value_pair(self):
        with patch('httpie.client.json.dumps', return_value=''):
            result = json_dict_to_request_body({'key1': 'value1', 'key2': 'value2'})
            self.assertEqual(result, '')

    def test_empty_input(self):
        with patch('httpie.client.json.dumps', return_value=''):
            result = json_dict_to_request_body({})
            self.assertEqual(result, '')
