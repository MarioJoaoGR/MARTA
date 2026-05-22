
import unittest
from unittest.mock import patch, MagicMock
from httpie.adapters import HTTPieHTTPAdapter

class TestHTTPieHTTPAdapter(unittest.TestCase):
    
    @patch('httpie.adapters.HTTPHeadersDict')
    def test_build_response_invalid_input(self, mock_headersdict):
        adapter = HTTPieHTTPAdapter()
        
        # Create a mock request and response object with invalid input
        req = MagicMock()
        resp = MagicMock()
        resp.headers = {"Content-Type": "application/json", "Set-Cookie": ["cookie1=value1", "cookie2=value2"]}
        
        # Call the build_response method
        with self.assertRaises(TypeError):
            adapter.build_response(req, resp)
