
import unittest
from httpie.plugins.builtin import HTTPBasicAuth
from base64 import b64encode
from unittest.mock import patch

class TestHTTPBasicAuth(unittest.TestCase):
    
    @patch('httpie.plugins.builtin.b64encode')
    def test_make_header_none_input(self, mock_b64encode):
        # Mock the b64encode function to return a fixed value for testing
        mock_b64encode.return_value = b'dXNlcjpwYXNz'  # This is 'user:pass' encoded in base64
        
        # Call the make_header method with None values
        result = HTTPBasicAuth.make_header(None, None)
        
        # Assert that the function returned the expected value
        self.assertEqual(result, 'Basic dXNlcjpwYXNz')
