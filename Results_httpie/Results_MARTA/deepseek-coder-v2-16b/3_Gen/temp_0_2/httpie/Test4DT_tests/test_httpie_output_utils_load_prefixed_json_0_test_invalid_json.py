
import unittest
from unittest.mock import patch
from httpie.output.utils import load_prefixed_json, load_json_preserve_order_and_dupe_keys

class TestHttpieOutputUtils(unittest.TestCase):
    
    @patch('httpie.output.utils.load_json_preserve_order_and_dupe_keys')
    def test_invalid_json(self, mock_load_json):
        # Mock the behavior of load_json_preserve_order_and_dupe_keys to raise ValueError
        mock_load_json.side_effect = ValueError("Invalid JSON")
        
        data = "__XSSI_PREFIX__ {'name': 'John', 'age': 30, 'city': 'New York'}"
        
        with self.assertRaises(ValueError):
            load_prefixed_json(data)
