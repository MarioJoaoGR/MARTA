
import unittest
from httpie.adapters import HTTPieHTTPAdapter
from unittest.mock import patch, MagicMock
import requests

class TestHTTPieHTTPAdapter(unittest.TestCase):
    
    @patch('httpie.adapters.requests')
    def test_build_response_valid_input(self, mock_requests):
        # Create a mock request object
        req = MagicMock()
        req.method = "GET"
        req.url = "http://example.com"
        
        # Create a mock response object with headers
        resp = MagicMock()
        resp.headers = {"Content-Type": "application/json", "Set-Cookie": ["cookie1=value1", "cookie2=value2"]}
        
        # Instantiate the adapter
        adapter = HTTPieHTTPAdapter()
        
        # Call the build_response method
        response = adapter.build_response(req, resp)
        
        # Assert that the headers are preserved in HTTPHeadersDict
        self.assertIsInstance(response.headers, HTTPHeadersDict)
        self.assertEqual(response.headers, {"Content-Type": "application/json", "Set-Cookie": ["cookie1=value1", "cookie2=value2"]})

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_adapters_HTTPieHTTPAdapter_build_response_0_test_valid_input
httpie/Test4DT_tests_codestral/test_httpie_adapters_HTTPieHTTPAdapter_build_response_0_test_valid_input.py:27:48: E0602: Undefined variable 'HTTPHeadersDict' (undefined-variable)


"""