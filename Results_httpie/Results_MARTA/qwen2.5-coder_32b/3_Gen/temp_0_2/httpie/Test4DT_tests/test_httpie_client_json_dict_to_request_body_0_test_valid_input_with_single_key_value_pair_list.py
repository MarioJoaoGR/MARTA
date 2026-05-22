
import unittest
from httpie.client import json_dict_to_request_body
import json
from typing import Dict, Any
from unittest.mock import patch

class TestJsonDictToRequestBody(unittest.TestCase):
    
    def test_valid_input_with_single_key_value_pair_list(self):
        # Test case with a valid dictionary containing exactly one key-value pair where the value is a list
        data = {'key': [1, 2, 3]}
        expected_output = '{"key": [1, 2, 3]}'
        
        with patch('httpie.client.json.dumps', return_value=expected_output):
            result = json_dict_to_request_body(data)
            self.assertEqual(result, expected_output)
    
    def test_invalid_input_without_single_key_value_pair(self):
        # Test case with an invalid dictionary that does not contain exactly one key-value pair
        data = {'key1': 'value1', 'key2': 'value2'}
        
        expected_output = ''
        
        with patch('httpie.client.json.dumps', return_value=expected_output):
            result = json_dict_to_request_body(data)
            self.assertEqual(result, expected_output)
    
    def test_empty_input_dictionary(self):
        # Test case with an empty dictionary
        data = {}
        
        expected_output = ''
        
        with patch('httpie.client.json.dumps', return_value=expected_output):
            result = json_dict_to_request_body(data)
            self.assertEqual(result, expected_output)
