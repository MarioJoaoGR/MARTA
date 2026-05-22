
import unittest
from httpie.adapters import HTTPieHTTPAdapter
from unittest.mock import patch, MagicMock

class TestHTTPieHTTPAdapter(unittest.TestCase):
    
    @patch('httpie.adapters.requests')
    def test_build_response_valid_input(self, mock_requests):
        # Create a mock request and response object
        req = MagicMock()
        resp = MagicMock()
        
        # Set up the headers for the response
        resp.headers = {"Content-Type": "application/json", "Set-Cookie": ["cookie1=value1", "cookie2=value2"]}
        
        # Create an instance of HTTPieHTTPAdapter
        adapter = HTTPieHTTPAdapter()
        
        # Call the build_response method
        response = adapter.build_response(req, resp)
        
        # Check if the headers are wrapped in HTTPHeadersDict
        self.assertIsInstance(response.headers, HTTPHeadersDict)
        self.assertEqual(response.headers, HTTPHeadersDict({"Content-Type": "application/json", "Set-Cookie": ["cookie1=value1", "cookie2=value2"]}))

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_adapters_HTTPieHTTPAdapter_build_response_0_test_valid_input
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_adapters_HTTPieHTTPAdapter_build_response_0_test_valid_input.py:24:48: E0602: Undefined variable 'HTTPHeadersDict' (undefined-variable)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_adapters_HTTPieHTTPAdapter_build_response_0_test_valid_input.py:25:43: E0602: Undefined variable 'HTTPHeadersDict' (undefined-variable)


"""